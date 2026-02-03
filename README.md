# PostgreSQL 18 Documentation RAG Agent

## Overview

This project implements a Retrieval-Augmented Generation (RAG) agent designed to answer questions using the official PostgreSQL 18 documentation. The system retrieves relevant sections from the documentation and uses them as grounded context for a large language model (LLM).
The agent is intended for technical question answering, such as SQL behavior, configuration parameters, performance tuning, and internal PostgreSQL concepts, while avoiding hallucinated answers.

## Purpose

The goal of this RAG agent is to provide accurate, documentation-backed responses to PostgreSQL 18 queries. Instead of relying solely on a language model’s training data, the system ensures that every answer is derived from the PostgreSQL 18 reference material.

This is particularly useful for:
* Learning PostgreSQL internals
* Verifying syntax and configuration options

## Data Source

* Official PostgreSQL 18 documentation
* Documentation is ingested from PDF sources and stored locally
* Content is chunked to preserve semantic meaning while enabling efficient retrieval

## Architecture

### Document Ingestion
* PostgreSQL 18 documentation is loaded and parsed
* Text is split into overlapping chunks to prevent loss of context across sections
* Each chunk retains metadata for traceability

### Embeddings
* Sentence-transformer based embeddings are used
* Embeddings are generated on CPU for portability
* Vectors are normalized to enable cosine similarity search


### Vector Storage
* Vector embeddings are stored in a searchable vector index
* The design uses FAISS indexing


### Retrieval
* Similarity-based retrieval is used to find the most relevant documentation chunks
* Top-k retrieval ensures multiple relevant passages are considered
* Retrieved chunks are concatenated into a single context window


### Generation
* A large language model receives the retrieved context and the user’s question
* The system prompt enforces strict grounding in the retrieved documentation
* Answers are generated only from PostgreSQL 18 reference content


## Query Flow
1. User submits a PostgreSQL-related question
2. The query is embedded using the same embedding model
3. Relevant documentation chunks are retrieved from the vector store
4. Retrieved text is passed as context to the language model
5. The final answer is returned to the user

