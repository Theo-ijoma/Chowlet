from fastapi import FastAPI

app = FastAPI(
    title="Chowlet API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Chowlet API"
    }