import sys
import json
import os
from datetime import datetime
from extractor import extract_sections
from ranker import rank_sections

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_json_path> <pdf_folder_path>")
        return

    input_json_path = sys.argv[1]
    pdf_folder_path = sys.argv[2]
    output_json_path = os.path.join(os.path.dirname(input_json_path), "challenge1b_output.json")

    try:
        with open(input_json_path, "r", encoding="utf-8") as f:
            input_data = json.load(f)
    except Exception as e:
        print(f"Error reading input JSON: {e}")
        return

    documents = input_data.get("documents", [])
    persona = input_data.get("persona", "")
    job = input_data.get("job_to_be_done", "")

    sections = extract_sections(documents, pdf_folder_path)
    ranked_sections = rank_sections(sections, persona, job)

    output = {
        "metadata": {
            "documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": ranked_sections
    }

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
