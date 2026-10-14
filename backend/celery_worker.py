import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CELERY_BACKEND = os.getenv("CELERY_RESULT_BACKEND", REDIS_URL)

celery_app = Celery(
    "earth_detective_worker",
    broker=REDIS_URL,
    backend=CELERY_BACKEND,
)

# Example periodic / background task
@celery_app.task(bind=True)
def fetch_nasa_task(self, lat=0.0, lon=0.0):
    # Import here to avoid circular imports in worker context
    from app.routes.nasa_connector import earth_imagery
    # NOTE: earth_imagery is an async FastAPI route; in production create a shared connector module
    return {"status": "scheduled", "lat": lat, "lon": lon}
