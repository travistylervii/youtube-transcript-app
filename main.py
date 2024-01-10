from fastapi import FastAPI
from typing import Union
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ytid/{item_id}")
def read_item(item_id: str):

    #processes youtube transcript from id
    print("Get Transcript")
    data = YouTubeTranscriptApi.get_transcript("M6DNOpQcCjs")

    transcriptText = ""

    #Extract transcript text
    for item in data:
        transcriptText = transcriptText + " " + item["text"]

    return {"item_id": item_id, "transcript": transcriptText}