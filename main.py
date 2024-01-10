from fastapi import FastAPI
from typing import Union
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ytid/{vid_id}")
def read_item(vid_id: str):

    #processes youtube transcript from id
    data = YouTubeTranscriptApi.get_transcript(vid_id)

    transcriptText = ""

    #Extract transcript text
    for item in data:
        transcriptText = transcriptText + " " + item["text"]

    return {"item_id": vid_id, "transcript": transcriptText}
