  
import streamlit as st  
from utils import process_document, process_image  
from faiss_index import search_documents  
  
st.set_page_config(page_title="RAG AI App", layout="wide", theme="dark")  

st.sidebar.title("AI Options")  
app_mode = st.sidebar.radio("Choose AI Type", ["Document Q&A", "Image Analysis", "Generative AI"])  

if app_mode == "Document Q&A":  
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])  
    if uploaded_file:  
        text = process_document(uploaded_file)  
        query = st.text_input("Ask a question about the document")  
        if st.button("Get Answer") and query:  
            answer = search_documents(query, text)  
            st.write(answer)  

elif app_mode == "Image Analysis":  
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])  
    if uploaded_image:  
        extracted_text = process_image(uploaded_image)  
        st.write("Extracted Text:", extracted_text)  

elif app_mode == "Generative AI":  
    user_input = st.text_area("Enter your prompt")  
    if st.button("Generate Response") and user_input:  
        st.write("AI Response:", "Generated text here")  # Placeholder for Llama API call  
    