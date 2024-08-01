# 📚 College Information Assistant

A powerful Streamlit web application that acts as a personal assistant for college-related queries. Upload college brochures, course catalogs, and other informational PDFs, and ask questions in natural language to get instant, AI-powered answers.

---

### ✨ Key Features

-   **Multi-PDF Upload**: Upload one or more PDF documents simultaneously.
-   **AI-Powered Q&A**: Uses Google's Gemini Pro model to understand and answer questions based on the content of the uploaded documents.
-   **Customizable Responses**: Choose from different response styles (Formal, Creative, Concise) to tailor the AI's personality.
-   **Chat History**: Keeps a record of your questions and the AI's answers for the current session.
-   **Modern UI**: Clean and responsive user interface built with Streamlit, with custom styling for a polished look.
-   **Secure**: API keys are loaded from environment variables, not hardcoded in the source.

### 🛠️ Tech Stack

-   **Frontend**: Streamlit
-   **Backend**: Python
-   **AI Model**: Google Gemini Pro & Flash
-   **PDF Processing**: PyPDF

### 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

#### Prerequisites

-   Python 3.8+
-   A Google API Key for the Gemini API. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a `.env` file in the root of your project directory and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
    *Alternatively, you can set it directly in your terminal:*
    ```bash
    # For Windows
    set GOOGLE_API_KEY="YOUR_API_KEY_HERE"

    # For macOS/Linux
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

#### Running the Application

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

---

### 📝 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
