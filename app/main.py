from fastapi import FastAPI

app = FastAPI(
    title="WebFare",
    version="0.0.1",
    description="A Web-Based FanFicFare Implementation."
    )


@app.get('/')
async def index():
    return {"Real": "Python"}