from fastapi import FastAPI
from orm import engine
from object_vault import vault


app = FastAPI()


@app.get("/api/{name}")
async def main(name: str) -> dict:
    return {"message": f"pozdravlyaem, {name}, backend rabotaet, ti ne debil"}
