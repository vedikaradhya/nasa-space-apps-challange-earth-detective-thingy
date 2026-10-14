from fastapi import APIRouter
import os
import httpx

router = APIRouter()

NASA_API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://api.nasa.gov"

@router.get("/earth_imagery")
async def earth_imagery(lat: float, lon: float, dim: float = 0.1):
    """Fetch NASA Earth imagery (placeholder).
    Example API: /planetary/earth/imagery
    """
    if not NASA_API_KEY:
        return {"error": "NASA_API_KEY not configured"}
    url = f"{BASE_URL}/planetary/earth/imagery"
    params = {"lat": lat, "lon": lon, "dim": dim, "api_key": NASA_API_KEY}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        # The API returns an image or JSON depending on params — return JSON/body placeholder
        return {"status": "ok", "url": str(resp.url)}

@router.get("/example_gldas")
async def example_gldas():
    """Placeholder for GLDAS or other Earth system data connectors.
    Implement data fetching, caching, and normalization here.
    """
    return {"status": "not_implemented", "message": "Add connector logic in backend/app/routes/nasa_connector.py"}
