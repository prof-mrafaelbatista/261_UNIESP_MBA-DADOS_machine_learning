from fastapi import FastAPI

app = FastAPI(title="API Server")

@app.get("/")
async def root():
    return {"message": "Hello World"}