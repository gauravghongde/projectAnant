#!/usr/bin/env python3
from TTS.api import TTS
import os

INPUT = "scripts/today.txt"
OUTPUT = "audio/narration.wav"
MODEL = "tts_models/en/ljspeech/tacotron2-DDC"  # English-only model

def main():
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    
    # Initialize TTS with English-only model
    tts = TTS(MODEL, progress_bar=False)
    
    # Read input text
    with open(INPUT, "r") as f:
        text = f.read()
    
    # Generate speech
    tts.tts_to_file(text=text, file_path=OUTPUT)
    print(f"TTS output saved to {OUTPUT}")

if __name__ == "__main__":
    main()
