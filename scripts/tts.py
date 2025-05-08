#!/usr/bin/env python3
from gtts import gTTS
import os

INPUT = "scripts/today.txt"
OUTPUT = "audio/narration.mp3"  # gTTS outputs MP3 files

def main():
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    
    # Read input text
    with open(INPUT, "r") as f:
        text = f.read()
    
    # Generate speech using Google TTS
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Save to file
    tts.save(OUTPUT)
    print(f"TTS output saved to {OUTPUT}")

if __name__ == "__main__":
    main()
