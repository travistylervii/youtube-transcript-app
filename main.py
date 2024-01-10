from fastapi import FastAPI
from typing import Union
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/yt-transcribe/")
def read_item(videoId: str = None):

    if(videoId == "None"):
        return {"item_id": videoId, "error": "No Video Id"}
    
    #processes youtube transcript from id
    data = YouTubeTranscriptApi.get_transcript(videoId)

    transcriptText = ""

    #Extract transcript text
    for item in data:
        transcriptText = transcriptText + " " + item["text"]

    return {"item_id": videoId, "transcript": transcriptText}
