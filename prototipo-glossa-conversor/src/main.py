import os
from parser import parse_srt
from glossa import text_to_glossa
from utils import save_json

INPUT_DIR = "data"
OUTPUT_DIR = "output"

def main():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".srt"):
            path = os.path.join(INPUT_DIR, file)

            subtitles = parse_srt(path)
            result = []

            for item in subtitles:
                glossa = text_to_glossa(item["text"])

                result.append({
                    "index": item["index"],
                    "start": item["start"],
                    "end": item["end"],
                    "original": item["text"],
                    "glossa": glossa
                })

            output_file = os.path.join(OUTPUT_DIR, file.replace(".srt", ".json"))
            save_json(result, output_file)

            print(f"✅ Convertido: {file} -> {output_file}")

if __name__ == "__main__":
    main()