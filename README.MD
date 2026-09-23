PDF RAG Chatbot using LlamaIndex and Ollama
Project Overview

This project is an initial-stage Retrieval-Augmented Generation (RAG) application that answers questions based on information available in a PDF document.

The project uses LlamaIndex for document processing, chunking, embeddings, indexing, and retrieval.

Ollama is used to run the Llama 3.2 language model and the Nomic embedding model locally.



RAG Workflow
PDF Document
     ↓
PDF Reader
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Embeddings
     ↓
Vector Store Index
     ↓
Similarity Search
     ↓
Llama 3.2
     ↓
   Answer 


Technologies Used

Python
LlamaIndex
Ollama
Llama 3.2
Nomic Embed Text
PDFReader
SentenceSplitter
VectorStoreIndex
Retrieval-Augmented Generation (RAG)