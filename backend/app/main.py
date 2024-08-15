from fastapi import FastAPI

app = FastAPI()


@app.get("/api/{name}")
async def main(name: str) -> dict:
    return {"message": f"pozdravlyaem, {name}, backend rabotaet, ti ne debil"}
