#!/usr/bin/env python3
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def main():
    clips = []
    for i in range(1, 3):
        clips.append(VideoFileClip(f"visuals/scene{i}.mp4"))
    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip("audio/narration.wav")
    final = video.set_audio(audio)
    os.makedirs("output", exist_ok=True)
    final.write_videofile("output/output.mp4", codec="libx264")
    print("Video assembled at output/output.mp4")

if __name__ == "__main__":
    main()
