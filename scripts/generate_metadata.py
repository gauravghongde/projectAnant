#!/usr/bin/env python3
import os
import json
from gpt4all import GPT4All

# Paths and models
MODEL = "orca-mini-3b-gguf2-q4_0"  # Updated to a reliable available model
SCRIPT_PATH = "scripts/today.txt"
META_OUT = "scripts/metadata.json"

def run_gpt4all(prompt, max_tokens=200):
    """Use GPT4All Python API with a prompt and return generated text."""
    model = GPT4All(MODEL)
    return model.generate(prompt, max_tokens=max_tokens)

def generate_titles(script):
    prompt = (
        f"Based on the following YouTube script, suggest 5 engaging, SEO-optimized video titles (one per line):\n\n"
        f"{script}"
    )
    titles = run_gpt4all(prompt).splitlines()
    return [t.strip() for t in titles if t.strip()][:5]

def generate_description(script):
    prompt = (
        "Create a YouTube video description that summarizes the following script, "
        "includes chapter timestamps in HH:MM:SS format, and adds a call-to-action:\n\n"
        + script
    )
    return run_gpt4all(prompt, max_tokens=500)

def extract_tags(script, n=10):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(script)
    # count noun chunks
    freq = {}
    for chunk in doc.noun_chunks:
        key = chunk.text.lower().strip()
        freq[key] = freq.get(key, 0) + 1
    # pick top-n
    tags = sorted(freq, key=freq.get, reverse=True)[:n]
    # clean commas
    return [t.replace(",", "") for t in tags]

def main():
    script = open(SCRIPT_PATH, "r").read()
    metadata = {
        "titles": generate_titles(script),
        "description": generate_description(script),
        "tags": extract_tags(script, n=12)
    }
    os.makedirs(os.path.dirname(META_OUT), exist_ok=True)
    with open(META_OUT, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Metadata written to {META_OUT}")

if __name__ == "__main__":
    main()
