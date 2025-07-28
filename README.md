# Challenge 1B: Multi-Collection PDF Analysis

## 🔍 Overview

This project implements an advanced PDF content analysis pipeline that processes **multiple document collections**. It extracts and ranks relevant information based on specific **personas** and **real-world tasks**, delivering structured output for each collection.

---

## 🗂️ Project Structure

CHALLENGE-1B/
├── app/
│ ├── extractor.py # Core logic to extract content from PDFs
│ ├── main.py # Orchestrates the overall pipeline
│ └── ranker.py # Ranks sections based on relevance
├── Collection 1/ # Travel Planning
│ ├── pdfs/ # 7 South of France travel guides
│ ├── challenge1b_input.json
│ └── challenge1b_output.json
├── Collection 2/ # Adobe Acrobat Learning
│ ├── pdfs/ # 15 Acrobat learning guides
│ ├── challenge1b_input.json
│ └── challenge1b_output.json
├── Collection 3/ # Recipe Collection
│ ├── pdfs/ # 9 Vegetarian cooking guides
│ ├── challenge1b_input.json
│ └── challenge1b_output.json
├── requirements.txt # Python dependencies
└── README.md # Project documentation

# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the main analysis
python app/main.py --collection "Collection 1"

---

## 🐳 Docker: Build and Run

### 🔨 Build the Docker image

```bash
docker build -t challenge1b:v1 .

# Run the app inside a container

docker run --rm -v "$(pwd)":/app challenge1b:v1
The -v "$(pwd)":/app option mounts your project directory, ensuring the input/output files work correctly.

# Run with specific collection (optional)

docker run --rm -v "$(pwd)":/app challenge1b:v1 python app/main.py --collection "Collection 1"
