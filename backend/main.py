from fastapi import FastAPI, File, UploadFile, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import pandas as pd
import jwt
import io
import os
from typing import List, Dict

from .trend import analyze_trend_from_dataframe

app = FastAPI(title="Earth Detective API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JWT_SECRET = os.environ.get("JWT_SECRET", "super-secret-key-change-me")
JWT_ALGORITHM = "HS256"

# NOTE: In this scaffold users are stored in-memory. Replace with a database in production.
users: Dict[str, Dict] = {}

class UserCreate(BaseModel):
    email: str
    password: str

class TrendPayload(BaseModel):
    data: List[Dict]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/signup")
async def signup(user: UserCreate):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.email] = {"password": user.password}
    token = jwt.encode({"sub": user.email, "exp": datetime.utcnow() + timedelta(days=7)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token, "user": {"email": user.email}}

@app.post("/login")
async def login(user: UserCreate):
    saved = users.get(user.email)
    if not saved or saved["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.email, "exp": datetime.utcnow() + timedelta(days=7)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token, "user": {"email": user.email}}

@app.post("/api/trend/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    contents = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV format: {str(e)}")

    # Accept common column names
    col_candidates = [("date", "value"), ("Date", "Value"), ("time", "value")] 
    found = False
    for dcol, vcol in col_candidates:
        if dcol in df.columns and vcol in df.columns:
            df = df[[dcol, vcol]].rename(columns={dcol: 'date', vcol: 'value'})
            found = True
            break
    if not found:
        # try to auto-detect
        if df.shape[1] >= 2:
            df = df.iloc[:, :2]
            df.columns = ['date', 'value']
        else:
            raise HTTPException(status_code=400, detail="CSV must contain at least two columns (date,value)")

    result = analyze_trend_from_dataframe(df, date_col='date', value_col='value')
    return result

@app.post("/api/trend/analyze")
async def analyze_json(payload: TrendPayload = Body(...)):
    # payload.data expected as list of {date, value}
    df = pd.DataFrame(payload.data)
    result = analyze_trend_from_dataframe(df, date_col='date', value_col='value')
    return result

@app.get("/api/datasets/list")
async def list_datasets():
    # Simple static list for scaffold; wire to a catalog/db in production
    return [
        {"id": "sample_co2", "name": "Sample CO2 (Synthetic)", "description": "Demo CO2 monthly series"}
    ]

@app.get("/api/datasets/sample_co2")
async def sample_co2():
    path = os.path.join(os.path.dirname(__file__), 'sample_data', 'co2_sample.csv')
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Sample dataset not found")
    return fastapi.responses.FileResponse(path, media_type='text/csv', filename='co2_sample.csv')
