# ⚖ Legal Document Analyzer

## 📜 Overview
The **Legal Document Analyzer** is a Streamlit-based web application that allows users to extract key insights from legal documents using AI-driven analysis. Users can either **paste legal text** or **upload Word/PDF files** for processing.

## 🚀 Features
- **📄 Summarization**: Generates concise summaries of legal documents.
- **📌 Key Clauses Extraction**: Identifies important legal terms (e.g., Termination, Liability, Payment).
- **🔍 Named Entity Recognition (NER)**: Extracts relevant entities like people, organizations, and locations.
- **⚡ FastAPI Integration**: Uses a backend LLM to process legal text.

## 🛠 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/NicholasTheGeek/legal-analyzer.git
cd legal-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run app.py

📌 Usage
- Upload a legal document (.docx or .pdf) OR paste text manually.
- Click "Analyze" to process the document.
- View results categorized into Summary, Key Clauses, and Named Entities.
🏗 Tech Stack
- Frontend: Streamlit
- Backend: FastAPI + Llama2
- Processing: NER, Summarization, Clause Extraction
- Deployment: GitHub, Streamlit Cloud
🎯 Future Enhancements
- [ ] 📝 Support for PDFs with embedded images (OCR)
- [ ] 🚀 API access for bulk document analysis
- [ ] 🎨 Advanced UI for better visualization
- [ ] 📊 Data export options (CSV, JSON)
📜 License
This project is open-source under the MIT License.
