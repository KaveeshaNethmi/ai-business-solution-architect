from fastapi import FastAPI

app = FastAPI(
    title="AI Business Discovery & Solution Architect API",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "AI Business Discovery & Solution Architect"
    }