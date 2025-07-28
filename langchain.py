import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyMuPDFLoader 
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import textwrap
import os
import tempfile 
from dotenv import load_dotenv




GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def page_setup():
    st.set_page_config(page_title="College Information Assistant", layout="wide")
    st.markdown("""
        <style>
        .stApp {
            background-color: #f0f0f5;
            color: #003366;
        }
        .stButton>button {
            background-color: #003366;
            color: #ffffff;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-size: 16px;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            border: 2px solid #003366;
        }
        .stButton>button:hover {
            background-color: #002244;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stTextInput>div>input {
            border-radius: 5px;
            padding: 0.5rem;
            border: 2px solid #003366;
            transition: border-color 0.3s ease;
            width: 100%;
        }
        .stTextInput>div>input:focus {
            border-color: #002244;
        }
        .stMarkdown {
            font-family: 'Roboto', sans-serif;
        }
        .stProgress>div>div>div {
            background-color: #003366;
        }
        .stSidebar {
            background-color: #e0e0e0;
            padding: 20px;
            border-right: 2px solid #003366;
        }
        .stSidebar h2 {
            color: #003366;
        }
        .header-border {
            border-top: 2px solid #003366;
            padding-top: 10px;
            margin-top: 20px;
        }
        .input-container {
            display: flex;
            flex-direction: column;
            margin-bottom: 20px;
        }
        .input-container > button {
            margin-top: 10px;
            align-self: flex-end;
        }
        .chat-history, .contact-info {
            border: 1px solid #003366;
            border-radius: 5px;
            padding: 10px;
            background-color: #ffffff;
            margin-top: 20px;
        }
        .chat-item {
            border-bottom: 1px solid #e0e0e0;
            padding: 10px;
        }
        .chat-item:last-of-type {
            border-bottom: none;
        }
        .footer {
            margin-top: 20px;
            border-top: 2px solid #003366;
            padding: 10px 0;
            text-align: center;
        }
        .footer-button {
            background-color: #003366;
            color: #ffffff;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-size: 16px;
            transition: background-color 0.3s ease;
            border: none;
            cursor: pointer;
        }
        .footer-button:hover {
            background-color: #002244;
        }
        </style>
    """, unsafe_allow_html=True)
    st.title("📚 College Information Assistant (LangChain Version)")
    st.markdown("<div class='header-border'></div>", unsafe_allow_html=True)
    st.markdown("### Upload your PDFs and ask questions about college information. Let's get started!")

def get_preset():
    st.sidebar.header("🎨 Preset Options")
    preset = st.sidebar.radio(
        "Select response style:",
        ("Formal", "Creative", "Concise"),
        index=0
    )
    st.sidebar.info("Select a style to tailor the AI responses to your preference.")
    return preset

def apply_preset(preset):
    presets = {
        "Creative": ("gemini-1.5-flash", 1.0, 0.95, 2500),
        "Concise": ("gemini-1.5-pro", 0.3, 0.8, 1000),
        "Formal": ("gemini-1.5-pro", 0.7, 0.9, 2000)
    }
    return presets.get(preset, presets["Formal"])

def get_pdf_documents_and_chunks(uploaded_files):
    """Extracts text from PDFs using PyMuPDF and splits them into chunks."""
    docs = []
    for uploaded_file in uploaded_files:
       
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            print(f"[INFO] Loading file: {uploaded_file.name}")

            
            try:
                loader = PyMuPDFLoader(tmp_file_path)
                loaded_docs = loader.load()
                
                if not loaded_docs:
                    st.error(f"No readable text found in {uploaded_file.name}. The file might be image-based or corrupted.")
                    print(f"[WARNING] Empty content from {uploaded_file.name}")
                else:
                    docs.extend(loaded_docs)
                    print(f"[DEBUG] Total documents loaded so far: {len(docs)}")

            except Exception as e:
                st.error(f"Failed to process {uploaded_file.name}: {e}")
                print(f"[ERROR] PDF Load Failed for {uploaded_file.name}: {e}")
                continue 
        finally:
            
            if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)

    if not docs:
        return []

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_documents(docs)
    return chunks

@st.cache_resource(show_spinner="Creating knowledge base...")
def get_vector_store(_chunks):
    """Creates and caches the vector store."""
    if not _chunks:
        return None
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(_chunks, embedding=embeddings)
    return vector_store

def get_conversational_chain(model, temperature, top_p, max_tokens):
    """Creates the LangChain conversational chain."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. If the answer is not in
    the provided context, just say, "The answer is not available in the provided documents". Don't provide a wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_output_tokens=max_tokens,
        google_api_key=GOOGLE_API_KEY
    )
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    return chain

def main():
    if not GOOGLE_API_KEY:
        st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
        st.stop()
    
    page_setup()
    preset = get_preset()
    model, temperature, top_p, max_tokens = apply_preset(preset)

    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None
    if 'processed_files_id' not in st.session_state:
        st.session_state.processed_files_id = None

    st.sidebar.header("")
    uploaded_files = st.file_uploader("Upload PDF files here", type='pdf', accept_multiple_files=True)

    if uploaded_files:
        current_files_id = tuple((file.name, file.size) for file in uploaded_files)
        if st.session_state.processed_files_id != current_files_id:
            with st.spinner("Processing PDFs... This may take a moment."):
                pdf_chunks = get_pdf_documents_and_chunks(uploaded_files)
                if pdf_chunks:
                    st.session_state.vector_store = get_vector_store(pdf_chunks)
                else:
                    st.session_state.vector_store = None
                st.session_state.processed_files_id = current_files_id
            
            if st.session_state.vector_store:
                st.success("PDFs processed successfully. You can now ask questions.")
            else:
                # FIX: Updated UI warning message as you suggested
                st.warning("No text content found in the uploaded PDFs. Please upload readable (text-based) files.")
    
    if st.session_state.vector_store:
        with st.container():
            st.markdown("### Ask your question:")
            with st.form(key='question_form', clear_on_submit=True):
                question = st.text_input("Enter your question here:")
                submit_button = st.form_submit_button("Submit")
                if submit_button and question:
                    with st.spinner("Generating answer..."):
                        docs = st.session_state.vector_store.similarity_search(question)
                        chain = get_conversational_chain(model, temperature, top_p, max_tokens)
                        response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
                        answer = response['output_text']
                        st.session_state.history.append((question, answer))

    st.subheader("ANSWERS")
    chat_container = st.container()
    with chat_container:
        if st.session_state.history:
            with st.expander("View ANSWERS", expanded=True):
                for q, a in reversed(st.session_state.history):
                    st.markdown(f"<div class='chat-item'><strong>You:</strong> {q}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='chat-item'><strong>Assistant:</strong> {textwrap.fill(a, width=100)}</div>", unsafe_allow_html=True)

    with st.expander("Contact Us"):
        st.markdown("""
            <div class='contact-info'>
                <p><strong>Mobile No.:</strong> 9811XXXXX</p>
                <p><strong>Email:</strong> <a href='mailto:gh@gmail.com'>gh@gmail.com</a></p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
