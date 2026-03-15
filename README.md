# AI Customer Support Chatbot (RAG-based)

A production-ready customer support chatbot that answers questions from your company's PDF documentation using Retrieval Augmented Generation (RAG).

## Demo
Ask questions like:
- "How do I cancel my subscription?"
- "Do you offer refunds?"
- "How do I reset my password?"

## Tech Stack
- **LLM:** OpenAI GPT-4o-mini
- **RAG Framework:** LangChain
- **Vector Store:** ChromaDB
- **Frontend:** Streamlit
- **Language:** Python 3.9+

## Features
- Upload any company PDF documentation
- Instant answers with source citations
- Conversational chat interface
- Hallucinates — only answers from your documents

## Setup

1. Clone the repo
```bash
git clone https://github.com/rajeshvalluri/customer-support-bot.git
cd customer-support-bot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key
```bash
echo "OPENAI_API_KEY=your-key-here" > .env
```

4. Add your PDF files to `data/sample_docs/`

5. Run ingestion
```bash
python3 ingest.py
```

6. Launch the app
```bash
streamlit run app.py
```

## Use Cases
- SaaS product support bots
- Internal HR/policy document Q&A
- Healthcare compliance document search
- Legal document Q&A

## Author
Built by Rajesh Valluri — AI Engineer & Python Developer
