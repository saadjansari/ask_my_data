# Project Plan – Ask My Data

## Phase 0: Project Setup
- [x] Install Git if not already installed
- [x] Create GitHub repository and clone locally
- [x] Initialize Python project with uv
- [x] Add .gitignore for Python, virtual environment, and data
- [x] Create project folder structure
- [ ] Write initial README
- [x] Commit initial structure

## Phase 1: Core Environment & Dependencies
- [x] Install core project dependencies
- [x] Install development tools (formatter, linter, testing)
- [ ] Verify that all libraries import correctly
- [x] Configure linting and formatting

## Phase 2: Document Ingestion
- [ ] Implement CSV, PDF, and text file parsing
- [ ] Implement chunking of documents
- [ ] Save processed chunks
- [ ] Test ingestion on sample documents

## Phase 3: Embedding & Vector Store
- [ ] Convert document chunks into embeddings
- [ ] Store embeddings in vector database
- [ ] Build vector store from processed documents
- [ ] Test retrieval of relevant chunks

## Phase 4: Query Pipeline (RAG)
- [ ] Implement query pipeline connecting embeddings to LLM
- [ ] Test queries on sample documents
- [ ] Validate accuracy and relevance of answers

## Phase 5: Backend API
- [ ] Build API for document upload
- [ ] Build API for querying documents
- [ ] Test API endpoints locally
- [ ] Validate full API flow with sample queries

## Phase 6: Frontend (Optional)
- [ ] Build a simple frontend for document upload
- [ ] Build a simple frontend for querying
- [ ] Connect frontend to backend
- [ ] Test full workflow

## Phase 7: Deployment
- [ ] Dockerize backend
- [ ] Deploy backend to hosting platform
- [ ] (Optional) Deploy frontend
- [ ] Verify deployment works end-to-end

## Phase 8: Polish & Extras
- [ ] Add logging and error handling
- [ ] Write unit tests
- [ ] Update README with usage instructions
- [ ] Record demo video or screenshots
