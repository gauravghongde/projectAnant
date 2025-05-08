#!/usr/bin/env python3
import subprocess, os, datetime

TOPIC = os.getenv("VIDEO_TOPIC", "Latest AI Trends")
OUT_PATH = "scripts/today.txt"

def main():
    prompt = f"Write a detailed 10-minute YouTube script on {TOPIC}."
    # Assumes gpt4all-cli is installed on the runner (we install via pip in workflow)
    subprocess.run([
        "gpt4all-cli",
        "--model", "models/gpt4all-lora-unfiltered.bin",
        "--prompt", prompt,
        "--outfile", OUT_PATH
    ], check=True)
    print(f"Script saved to {OUT_PATH}")

if __name__ == "__main__":
    main()
