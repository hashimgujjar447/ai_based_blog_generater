# AI Blog Generator & RAG API

A FastAPI-powered AI application that combines content generation, Retrieval-Augmented Generation (RAG), semantic search, and multi-model fallback using OpenRouter, ChromaDB, and Sentence Transformers.

---

## Features

### AI Content Generation

- Generate structured meal plans and AI-generated content.
- Multi-model fallback support using OpenRouter.
- Automatic failover when a model becomes unavailable.

### Retrieval-Augmented Generation (RAG)

- Document chunking.
- Embedding generation using Sentence Transformers.
- ChromaDB vector storage.
- Semantic similarity search.
- Context-aware answer generation.

### Intelligent Query Routing

The system automatically decides whether a query should:

1. Use RAG retrieval from stored documents.
2. Use a general-purpose LLM response.

This is done using semantic similarity scores from vector search.

---

## Tech Stack

### Backend

- FastAPI
- Python

### LLM Gateway

- OpenRouter

### Models

- OpenAI GPT OSS 120B
- OpenAI GPT OSS 20B
- Meta Llama 3.3 70B
- Qwen3 Next 80B
- Google Gemma 4 31B
- Google Gemma 4 26B

### RAG Components

- ChromaDB
- Sentence Transformers
- all-MiniLM-L6-v2 Embedding Model

---

## Architecture

User Request
↓
Question Routing
↓
Semantic Similarity Search
↓
Relevant?
├── Yes → RAG Retrieval → Context Injection → LLM
└── No → Direct LLM Response

---

## Project Structure

```text
project/
│
├── main.py
├── services.py
├── llm_services.py
├── open_routes.py
├── schemas.py
│
├── rag/
│   ├── chunker.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── retrieval.py
│   ├── rag_service.py
│   ├── vector_store.py
│   └── search.py
│
└── data/
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd <project-name>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Git Bash:

```bash
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
OPEN_ROUTER_API=your_api_key_here
```

---

## Running the Application

```bash
uvicorn main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Generate Blog

```http
POST /generate-blog
```

Request:

```json
{
  "prompt": "My height is 164cm and weight is 72kg. I want to lose weight."
}
```

---

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "prompt": "What is Hashim's secret protein food?"
}
```

Response:

```json
{
  "success": true,
  "answer": "Dragon chicken."
}
```

---

## RAG Workflow

1. Load document.
2. Split into chunks.
3. Generate embeddings.
4. Store embeddings in ChromaDB.
5. Generate query embedding.
6. Perform vector similarity search.
7. Retrieve relevant chunks.
8. Inject context into the prompt.
9. Generate final answer using the LLM.

---

## Future Improvements

- PDF Upload Support
- Metadata Storage
- Source Citation Support
- User-Based Memory
- Persistent Conversation History
- Hybrid Search (Vector + Keyword)
- Reranking Pipeline

---

## Author

Muhammad Hashim

Built as a learning project to understand the internal mechanics of Retrieval-Augmented Generation (RAG), semantic search, vector databases, embeddings, and LLM integration without relying on high-level frameworks such as LangChain.
