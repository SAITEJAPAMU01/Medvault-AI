🛡️ MedVault AI
Secure Medical Record Management with RAG-powered AI Insights

MedVault AI is a full-stack application designed to help users securely store medical records and interact with them using Artificial Intelligence. By combining AES-256 encryption with Retrieval-Augmented Generation (RAG), the platform ensures that sensitive health data remains private while still being accessible for AI-driven analysis.

🌟 Key Features
End-to-End Encryption: All uploaded documents are encrypted using cryptography.fernet (AES-256) before being saved to disk.

AI-Powered Chat: Interact with your medical history using Google Gemini. Ask questions like "What were my blood test results from last June?"

Vectorized Memory: Uses Pinecone Vector Database to index medical notes, allowing for fast and relevant information retrieval.

Secure Backend: Built with FastAPI for high-performance, asynchronous API management.

Interactive UI: (Planned/Current) A user-friendly interface built with Streamlit for seamless file uploads and chat.

🏗️ Technical Architecture
The system follows a modern AI pipeline:

Ingestion: User uploads a .txt or .pdf file.

Encryption: The file is encrypted with a unique Master Key and stored locally.

Indexing: Plaintext chunks are converted into embeddings using gemini-3-flash and stored in Pinecone.

Retrieval: When a user asks a question, the system finds the relevant medical context in Pinecone.

Generation: Gemini generates a natural language response based only on the retrieved medical data.

🚀 Getting Started
1. Prerequisites
Python 3.12+

Google AI Studio API Key (Gemini)

Pinecone API Key & Environment

A 32-bit Fernet Master Key

2. Installation
Bash
git clone https://github.com/SAITEJAPAMU01/Medvault-AI.git
cd Medvault-AI
pip install -r requirements.txt
3. Environment Setup
Create a .env file in the root directory:

Code snippet
GOOGLE_API_KEY=your_gemini_key
PINECONE_API_KEY=your_pinecone_key
MASTER_KEY=your_generated_fernet_key
4. Running the Application
Bash
# Start the Backend
uvicorn main:app --reload

# Start the Frontend (if using Streamlit)
streamlit run app_ui.py
🛠️ Tech Stack
Language: Python

Framework: FastAPI

AI Models: Google Gemini (Generative AI & Embeddings)

Database: Pinecone (Vector DB)

Security: Cryptography (Fernet/AES)

Orchestration: LangChain
