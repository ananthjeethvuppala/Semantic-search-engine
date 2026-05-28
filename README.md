# Semantic Search Engine

A Python-based NLP project that performs **semantic search** using **Sentence Transformers embeddings** and **Cosine Similarity**.

Unlike keyword-based search, this project understands the **meaning of text** and returns the most relevant results.

---

## Features

- Load text corpus from file
- Generate sentence embeddings
- Semantic similarity search
- Meaning-based document retrieval
- Top relevant results with similarity score

---

## Project Structure

```txt
semantic-search-engine/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
│   └── corpus.txt
│
└── modules/
    ├── __init__.py
    ├── loader.py
    ├── embedder.py
    ├── similarity.py
    └── search.py
```

---

## Technologies Used

- Python
- Sentence Transformers
- Scikit-learn
- Cosine Similarity
- NLP Embeddings

---

## Installation

Clone repository:

```bash
git clone <your-github-link>
```

Go to folder:

```bash
cd semantic-search-engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run:

```bash
python main.py
```

Enter search query:

Example:

```txt
I want to learn AI
```

Output:

```txt
Top Results

1. Machine learning is a subset of artificial intelligence.
Similarity Score: 46.13%

2. Artificial intelligence is transforming industries.
Similarity Score: 42.21%

3. Deep learning helps in computer vision.
Similarity Score: 38.21%
```

---

## Example Use Cases

- AI search systems
- Document retrieval
- Chatbots
- RAG applications
- Knowledge search

---

## Future Improvements

- PDF support
- Search over large datasets
- Vector database integration
- Web UI
- Chat-based retrieval

---

## Author

Ananth Jeeth Vuppala