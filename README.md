📚 College Information Assistant
A powerful and intuitive Streamlit application that uses Google's Generative AI and LangChain to answer questions about college information from uploaded PDF documents. This tool allows users to upload multiple PDFs and interact with a conversational AI to get detailed, context-aware answers.

✨ Features
Multiple PDF Upload: Upload one or more PDF documents containing college information.

Intelligent Q&A: Ask questions in natural language and receive detailed answers based on the content of the uploaded PDFs.

Retrieval-Augmented Generation (RAG): Utilizes a robust RAG pipeline with LangChain for accurate and contextually relevant responses.

Customizable AI Personality: Choose from different response styles (Formal, Creative, Concise) to tailor the AI's output.

Efficient Processing: Text is extracted, split into manageable chunks, and stored in a FAISS vector store for fast retrieval.

Secure API Key Handling: Uses a .env file to securely manage your Google API key.

User-Friendly Interface: Built with Streamlit for a clean, interactive, and easy-to-use web interface.

Robust Error Handling: Provides clear feedback if PDFs cannot be processed or if text extraction fails.

🛠️ Tech Stack
Backend: Python

Web Framework: Streamlit

AI/LLM Framework: LangChain

Generative AI Model: Google Gemini (via langchain-google-genai)

PDF Processing: PyMuPDF

Vector Store: FAISS (faiss-cpu)

Environment Variables: python-dotenv

🚀 Getting Started
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
Python 3.8 or higher

pip package manager

2. Clone the Repository
git clone [https://github.com/your-username/college-information-assistant.git](https://github.com/your-username/college-information-assistant.git)
cd college-information-assistant

3. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
Install all the required Python packages using the single command below:

pip install streamlit google-generativeai langchain langchain-google-genai langchain-community faiss-cpu python-dotenv PyMuPDF

5. Configure Environment Variables
You need a Google API key to use the Gemini models.

Obtain your API key from Google AI Studio.

In the root directory of the project, create a new file named .env.

Add your API key to the .env file as follows:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with your actual Google API key.

🏃‍♀️ How to Run the Application
Once you have completed the setup, you can run the Streamlit application with the following command:

streamlit run app.py

Your web browser should automatically open to the application's URL (usually http://localhost:8501).

📝 How to Use
Upload PDFs: Use the file uploader to select one or more PDF files from your computer.

Wait for Processing: The application will process the PDFs and create a knowledge base. You will see a success message when it's ready.

Select a Style: Use the sidebar to choose a response style (Formal, Creative, or Concise).

Ask a Question: Type your question into the input box and click "Submit".

View the Answer: The AI's response will appear in the "ANSWERS" section below. Your conversation history is saved for the current session.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to fix a bug, please feel free to open an issue or submit a pull request.

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Make your changes.

Commit your changes (git commit -m 'Add some amazing feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.
