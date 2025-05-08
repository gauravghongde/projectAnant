#!/usr/bin/env python3
from TTS.api import TTS
import os

INPUT = "scripts/today.txt"
OUTPUT = "audio/narration.wav"
MODEL = "tts_models/en/ljspeech/tacotron2-DDC"

def main():
    tts = TTS(MODEL)
    with open(INPUT, "r") as f:
        text = f.read()
    tts.tts_to_file(text=text, file_path=OUTPUT)
    print(f"TTS output saved to {OUTPUT}")

if __name__ == "__main__":
    main()
