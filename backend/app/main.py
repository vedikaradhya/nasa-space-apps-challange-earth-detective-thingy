from fastapi import FastAPI
from app.routes import oauth, nasa_connector

app = FastAPI(title="Earth Detective - Backend")

app.include_router(oauth.router, prefix="/auth", tags=["auth"])
app.include_router(nasa_connector.router, prefix="/nasa", tags=["nasa"])


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
