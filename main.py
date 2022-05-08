from dotenv import dotenv_values
config = dotenv_values(".env")

from fastapi import FastAPI, HTTPException, Depends, Response
from modules import data_processing as DataProcessing
from modules import image_manipulation as ImageManipulation
from starlette.responses import StreamingResponse
import io

import aioredis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url(config["REDIS_URL"], encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)

rate_limit = [150, 60]
if config["RATE_LIMITED"] == "FALSE":
    rate_limit = [1000000000, 1]

@app.get("/api/board", dependencies=[Depends(RateLimiter(times=rate_limit[0], seconds=rate_limit[1]))])
def getBoard(FEN: str, size: int, dark: str, light: str):
    if size > 1300:
        raise HTTPException(status_code=400, detail="Image size should be equal or lower to 1300px")
    dark = "#" + dark
    light = "#" + light
    
    board_data = DataProcessing.convertFENTo2DArray(FEN)
    board_image = ImageManipulation.generateBoard(board_data, size, dark, light)
    
    buffer = io.BytesIO()
    board_image.save(buffer, "PNG")
    buffer.seek(0)

    return StreamingResponse(content=buffer, media_type="image/png")

#stress testing urls
@app.get(f"/{config['LOADER_IO_TOKEN']}")
def loaderioAuthentication():
    return Response(content = config["LOADER_IO_TOKEN"])