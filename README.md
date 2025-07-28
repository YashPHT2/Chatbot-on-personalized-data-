# 📚 College Information Assistant

A powerful and intuitive **Streamlit** application that uses **Google's Generative AI** and **LangChain** to answer questions about college information from uploaded PDF documents. This tool allows users to upload multiple PDFs and interact with a conversational AI to get detailed, context-aware answers.

---

## ✨ Features

- **Multiple PDF Upload:** Upload one or more PDF documents containing college information.
- **Intelligent Q&A:** Ask questions in natural language and receive detailed answers based on the content of the uploaded PDFs.
- **Retrieval-Augmented Generation (RAG):** Utilizes a robust RAG pipeline with LangChain for accurate and contextually relevant responses.
- **Customizable AI Personality:** Choose from different response styles (Formal, Creative, Concise) to tailor the AI's output.
- **Efficient Processing:** Text is extracted, split into manageable chunks, and stored in a FAISS vector store for fast retrieval.
- **Secure API Key Handling:** Uses a `.env` file to securely manage your Google API key.
- **User-Friendly Interface:** Built with Streamlit for a clean, interactive, and easy-to-use web interface.
- **Robust Error Handling:** Provides clear feedback if PDFs cannot be processed or if text extraction fails.

---

## 🛠 Tech Stack

- **Backend:** Python
- **Web Framework:** Streamlit
- **AI/LLM Framework:** LangChain
- **Generative AI Model:** Google Gemini (via `langchain-google-genai`)
- **PDF Processing:** PyMuPDF
- **Vector Store:** FAISS (`faiss-cpu`)
- **Environment Variables:** `python-dotenv`

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.8 or higher
- pip package manager

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/college-information-assistant.git
cd college-information-assistant
```

### 3. Create a Virtual Environment

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit google-generativeai langchain langchain-google-genai langchain-community faiss-cpu python-dotenv PyMuPDF
```

### 5. Configure Environment Variables

You need a Google API key to use the Gemini models.

1. Obtain your API key from [Google AI Studio](https://makersuite.google.com/app/).
2. In the root directory of the project, create a `.env` file and add:
```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

---

## 🏃‍♀️ How to Run the Application

Run the following command:

```bash
streamlit run app.py
```

The browser should open at `http://localhost:8501`.

---

## 📝 How to Use

1. **Upload PDFs:** Use the file uploader to select one or more PDFs.
2. **Wait for Processing:** The app processes the PDFs and prepares the knowledge base.
3. **Select a Style:** Use the sidebar to choose a response style.
4. **Ask a Question:** Enter your question and click **Submit**.
5. **View the Answer:** The AI’s response will appear below. Chat history is saved during the session.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`
3. Make your changes.
4. Commit: `git commit -m 'Add some amazing feature'`
5. Push: `git push origin feature/YourFeatureName`
6. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

