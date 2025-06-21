import streamlit as st
import fitz  # PyMuPDF
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Extract text from PDF
def extract_text(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Ask the LLM
def ask_question(question, context):
    prompt = f"Answer the following based only on this context:\n\n{context}\n\nQ: {question}\nA:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("🧠 AskPDF - Chat with any PDF")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    pdf_text = extract_text(uploaded_file)
    st.success("✅ PDF processed successfully!")

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = ask_question(question, pdf_text[:3000])  # Limit context
        st.markdown("### 📘 Answer:")
        st.write(answer)
