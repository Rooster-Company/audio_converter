from fastapi import FastAPI, Response, File, UploadFile
from urllib.request import urlopen
from pydub import AudioSegment
from io import BytesIO
from pydantic import BaseModel
import os
from typing import Annotated


def convert_to_mp3_url(file_url):
    file = BytesIO(urlopen(file_url).read())
    converted = BytesIO()
    AudioSegment.from_file(file).export(converted, format='mp3')
    return converted

def convert_to_mp3_file(file_bytes):
    file = BytesIO(file_bytes)
    converted = BytesIO()
    AudioSegment.from_file(file).export(converted, format='mp3')
    return converted


class UrlAudio(BaseModel):
    url: str


app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI audio converter!"}


@app.post("/convert/url")
async def convert_url(item: UrlAudio):
    converted = convert_to_mp3_url(item.url).read1()
    return Response(content=converted, media_type="audio/mp3")

@app.post("/convert/file")
async def convert_file(
    file: UploadFile
):
    file = await file.read()
    converted = convert_to_mp3_file(file).read1()
    return Response(content=converted, media_type="audio/mp3")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
    
