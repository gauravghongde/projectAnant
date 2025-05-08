#!/usr/bin/env python3
import subprocess, os

SCENES = [
    ("A dynamic infographic illustrating AI adoption in 2025", "visuals/scene1.mp4"),
    ("Animated diagram of how neural networks work",       "visuals/scene2.mp4"),
]

def main():
    os.makedirs("visuals", exist_ok=True)
    for prompt, out in SCENES:
        subprocess.run([
            "genmo", "--model", "mochi-1",
            "--prompt", prompt,
            "--length", "10",
            "--out", out
        ], check=True)
        print(f"Generated {out}")

if __name__ == "__main__":
    main()
