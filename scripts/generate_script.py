#!/usr/bin/env python3
import csv
import os
from gpt4all import GPT4All

# Paths
TOPICS_CSV   = "scripts/topics.csv"
SCRIPT_FILE  = "scripts/today.txt"

# LLM model
MODEL = "orca-mini-3b-gguf2-q4_0"  # Updated to a reliable available model

def pick_and_mark_topic(csv_path):
    """Read CSV, pick first TBD topic, mark it DEPLOYED, and rewrite CSV."""
    rows = []
    selected = None

    # Read all rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not selected and row["status"].upper() == "TBD":
                selected = row["topic"]
                row["status"] = "DEPLOYED"
            rows.append(row)

    if selected is None:
        raise RuntimeError("No topics with status TBD remaining in topics.csv")

    # Write back updated statuses
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["topic", "status"])
        writer.writeheader()
        writer.writerows(rows)

    return selected

def generate_script_for(topic, out_path):
    """Use GPT4All Python API to generate a script for the given topic."""
    prompt = f"Write a detailed 10-minute YouTube script on the topic: {topic}"
    
    # Initialize the model
    model = GPT4All(MODEL)
    
    # Generate text
    output = model.generate(prompt, max_tokens=2000)
    
    # Write to file
    with open(out_path, "w") as f:
        f.write(output)
    
    print(f"Script for '{topic}' written to {out_path}")

def main():
    # Ensure scripts directory exists
    os.makedirs(os.path.dirname(SCRIPT_FILE), exist_ok=True)

    # 1. Pick topic and mark deployed
    topic = pick_and_mark_topic(TOPICS_CSV)
    print(f"[INFO] Selected topic: {topic}")

    # 2. Generate the script
    generate_script_for(topic, SCRIPT_FILE)

if __name__ == "__main__":
    main()
