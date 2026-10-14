from fastapi import APIRouter, Request, Response, HTTPException
import os
import httpx
from urllib.parse import urlencode

router = APIRouter()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
APP_URL = os.getenv("APP_URL", "http://localhost:8000")

@router.get("/github/login")
async def github_login():
    if not (GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET):
        raise HTTPException(status_code=503, detail="GitHub OAuth not configured")
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "scope": "read:user user:email",
        "redirect_uri": f"{APP_URL}/auth/github/callback",
    }
    url = f"https://github.com/login/oauth/authorize?{urlencode(params)}"
    return {"url": url}

@router.get("/github/callback")
async def github_callback(code: str):
    """
    Exchange code for access token and return a minimal session response.
    Production: validate state, set secure cookies, and persist user record.
    """
    token_url = "https://github.com/login/oauth/access_token"
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            token_url,
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={"Accept": "application/json"},
        )
        resp.raise_for_status()
        token_data = resp.json()
    access_token = token_data.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Failed to obtain access token")

    # Example: fetch GitHub user
    async with httpx.AsyncClient() as client:
        user_resp = await client.get("https://api.github.com/user", headers={"Authorization": f"token {access_token}"})
        user_resp.raise_for_status()
        profile = user_resp.json()

    # TODO: Create or update user in DB and set session cookie
    return {"profile": {"login": profile.get("login"), "id": profile.get("id")}}
