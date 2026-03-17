import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_community.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

load_dotenv()

try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
except:
    openai_api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt_template = """You are a helpful customer support assistant.
Use ONLY the context below to answer the question.
If the answer is not in the context, say:
"I don't have information on that. Please contact support@acmesaas.com"

Context:
{context}

Question: {question}

Answer:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    openai_api_key=openai_api_key
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

def get_answer(question: str) -> dict:
    result = qa_chain.invoke({"query": question})
    sources = []
    for doc in result["source_documents"]:
        page = doc.metadata.get("page", "unknown")
        source = doc.metadata.get("source", "unknown")
        sources.append(f"{source} (page {page + 1})")
    return {
        "answer": result["result"],
        "sources": list(set(sources))
    }
