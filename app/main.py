from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse("index.html")


@app.get("/geo-data")
async def get_geo_data():
    return {"latitude": 51.5074, "longitude": 0.1278}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)