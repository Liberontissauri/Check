from fastapi import FastAPI
from modules import data_processing as DataProcessing
from modules import image_manipulation as ImageManipulation
from starlette.responses import StreamingResponse
import io
import time
app = FastAPI()


@app.get("/api/board")
async def getBoard(FEN: str, size: int, dark: str, light: str):
    dark = "#" + dark
    light = "#" + light
    
    board_data = DataProcessing.convertFENTo2DArray(FEN)
    board_image = ImageManipulation.generateBoard(board_data, size, dark, light)
    
    buffer = io.BytesIO()
    board_image.save(buffer, "PNG")
    buffer.seek(0)

    return StreamingResponse(content=buffer, media_type="image/png")
