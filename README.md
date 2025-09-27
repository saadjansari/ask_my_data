# Ask My Data

Query your own documents (PDFs, CSVs, TXT) using LLMs with Retrieval-Augmented Generation (RAG).
Built with FastAPI, LangChain, and FAISS.

## Features
- Upload your documents.
- Automatically chunk + embed content.
- Query with natural language.
- Powered by OpenAI embeddings + LangChain.

## Setup
```bash
# Install dependencies
uv sync

# Run FastAPI server
uv run uvicorn src.app:app --reload
