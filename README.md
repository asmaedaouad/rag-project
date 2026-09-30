# RAG

This is a minimal implementation of a Retrieval-Augmented Generation (RAG) system for question answering over documents.

The project demonstrates the main steps of a RAG pipeline:

- Document loading
- Text splitting
- Embeddings generation
- Vector storage
- Similarity search
- Context retrieval
- LLM-based question answering

## Requirements

- Python 3.11 or later
- Miniconda
- Git

## Setup

### 1. Install Miniconda

Download and install Miniconda from:

https://docs.anaconda.com/miniconda/install/

### 2. Create a Conda environment

```bash
conda create -n mini-rag-app python=3.11
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

conda activate mini-rag-app
$ uvicorn main:app -- reload -- host 0.0.0.0 -- port 5000
