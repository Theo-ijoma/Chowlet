from fastapi import FastAPI  # type: ignore[import]
from app.api.v1.auth.routes import router as auth_router

app = FastAPI(
    title="Chowlet API",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Chowlet API"
    }