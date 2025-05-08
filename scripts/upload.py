#!/usr/bin/env python3
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.client import OAuth2Credentials

def get_credentials():
    return OAuth2Credentials.from_json(os.getenv("YT_CREDENTIALS_JSON"))

def main():
    creds = get_credentials()
    youtube = build('youtube', 'v3', credentials=creds)
    media = MediaFileUpload('output/output.mp4', chunksize=-1, resumable=True)
    req = youtube.videos().insert(
        part='snippet,status',
        body={
            'snippet': {
                'title': os.getenv("VIDEO_TITLE", "Daily AI Video"),
                'description': os.getenv("VIDEO_DESC", ""),
                'tags': os.getenv("VIDEO_TAGS", "AI,Automation").split(",")
            },
            'status': {'privacyStatus': 'public'}
        },
        media_body=media
    )
    res = req.execute()
    print(f"Uploaded video ID: {res['id']}")

if __name__ == "__main__":
    main()
