from fastapi import FastAPI, Response
from urllib.request import urlopen
from pydub import AudioSegment
from io import BytesIO
from pydantic import BaseModel


def convert_to_mp3(file_url):
    file = BytesIO(urlopen(file_url).read())
    converted = BytesIO()
    AudioSegment.from_file(file).export(converted, format='mp3')
    return converted


class UrlAudio(BaseModel):
    url: str

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI audio converter!"}


@app.post("/convert")
async def convert(item: UrlAudio):
    converted = convert_to_mp3(item.url).read1()
    return Response(content=converted, media_type="audio/mp3")
