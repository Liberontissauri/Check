from fastapi import FastAPI, HTTPException
from modules import data_processing as DataProcessing
from modules import image_manipulation as ImageManipulation
from starlette.responses import StreamingResponse
import io
import time
app = FastAPI()


@app.get("/api/board")
async def getBoard(FEN: str, size: int, dark: str, light: str):
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
