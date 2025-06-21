# 🧠 AskPDF — Chat with Any PDF Using OpenAI

AskPDF is a lightweight AI-powered web app that lets users upload a PDF and ask natural language questions about its content. It uses OpenAI's GPT model to generate context-aware answers based on the extracted text.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenAI-GPT--3.5-informational?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PDF-PyMuPDF-yellow?style=for-the-badge" />
</div>

---

## 🚀 Features

- 📄 Upload any PDF document
- 🤖 Ask questions in plain English
- 🔍 Extracts and processes text using PyMuPDF
- 💬 Generates AI-powered answers using GPT-3.5
- ⚡ Built with Python and Streamlit

---

## 📸 Demo

<img src="https://github.com/yourusername/askpdf/assets/demo.gif" alt="AskPDF demo" width="600"/>

*(Add a GIF or screenshot of your app running locally here)*

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: OpenAI GPT-3.5
- **PDF Parsing**: PyMuPDF (fitz)

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/askpdf.git
cd askpdf

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
