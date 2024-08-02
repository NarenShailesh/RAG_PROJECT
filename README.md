# RAG-LLM-PROJECT

# SafetySensei Techno-Bot

Welcome to SafetySensei Techno-Bot, an intelligent chatbot designed to help drivers and pedestrians navigate traffic rules and vehicle regulations. This project is part of the IBM SkillsBuild Internship for AICTE EduNet.

## Overview

SafetySensei Techno-Bot is an AI-powered FAQ system that provides quick and accurate answers to questions about traffic policies, rules, and regulations. Leveraging the power of Google Palm LLM, HuggingFace embeddings, and FAISS vector stores, SafetySensei Techno-Bot ensures that users have access to reliable information at their fingertips.

![image](https://github.com/user-attachments/assets/1e0ad024-c6aa-4d07-ac93-ce07b07051cf)



## Features

- **Intelligent Query Handling:** Uses advanced language models to understand and respond to user queries.
- **Comprehensive Knowledge Base:** Covers a wide range of topics related to campus rules and regulations.
- **Interactive Interface:** Built with Streamlit for an engaging user experience.
- **Scalable and Extendable:** Designed to be easily extendable with additional documents and data sources.

## Project Structure

- `Helper.py`: Contains functions for creating the vector database and setting up the QA chain.
- `Main.py`: The main entry point for the Streamlit application.
- `rules.txt`: Contains the rules and regulations document used for creating the vector database.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- HuggingFace Transformers
- FAISS
- Google API Key

Note: Use .env file for providing API Key.
