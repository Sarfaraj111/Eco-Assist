"""
EcoAssist RAG Engine
Retrieval-Augmented Generation pipeline using FAISS + HuggingFace embeddings + OpenAI GPT
"""

import os
import json
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

import sys
sys.path.append(str(Path(__file__).parent.parent))
from knowledge_base.sdg_knowledge import SDG_DOCUMENTS

load_dotenv()

# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────
VECTOR_STORE_PATH = Path(__file__).parent / "faiss_index"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
OPENAI_MODEL = os.getenv("MODEL_NAME", "gpt-4o-mini")


SYSTEM_PROMPT = """You are EcoAssist 🌿, an expert AI assistant specializing in:
- SDG 13: Climate Action & Carbon Emissions
- SDG 11: Sustainable Cities & Air/Noise/Light Pollution
- SDG 12: Responsible Consumption, Plastic Pollution & Circular Economy
- SDG 3: Good Health & Environmental Health Impacts

Your role:
1. Answer questions about pollution, sustainability, and environmental health using the retrieved context.
2. Always cite the SDG category your answer relates to (e.g., "📌 SDG 13 – Climate Action").
3. Provide actionable, practical advice alongside factual information.
4. Use friendly but authoritative language — like a knowledgeable eco-consultant.
5. If the retrieved context doesn't contain enough information, use your general knowledge
   but clearly note that the answer is from general knowledge.
6. Structure longer answers with bullet points or numbered lists for clarity.
7. End responses with a relevant eco-action tip when appropriate (prefix with 💡 Eco Tip:).

Context from EcoAssist Knowledge Base:
{context}

Chat History:
{chat_history}
"""

HUMAN_PROMPT = "{question}"


def build_documents() -> list[Document]:
    """Convert SDG knowledge base entries to LangChain Documents."""
    docs = []
    for entry in SDG_DOCUMENTS:
        doc = Document(
            page_content=entry["content"].strip(),
            metadata={
                "id": entry["id"],
                "sdg": entry["sdg"],
                "title": entry["title"],
                "tags": ", ".join(entry["tags"]),
            }
        )
        docs.append(doc)
    return docs


def get_or_create_vectorstore() -> FAISS:
    """Load existing FAISS index or build a new one from the knowledge base."""
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    if VECTOR_STORE_PATH.exists():
        print(f"Loading existing FAISS index from {VECTOR_STORE_PATH}")
        return FAISS.load_local(
            str(VECTOR_STORE_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )

    print("Building new FAISS index from knowledge base...")
    documents = build_documents()
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(str(VECTOR_STORE_PATH))
    print(f"FAISS index saved to {VECTOR_STORE_PATH}")
    return vectorstore


class EcoAssistRAG:
    """Main RAG assistant for EcoAssist."""

    def __init__(self):
        self.vectorstore = get_or_create_vectorstore()
        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key or api_key == "your_openai_api_key_here":
            print("WARNING: No valid OpenAI API key found. Using mock responses.")
            self.llm = None
        else:
            self.llm = ChatOpenAI(
                model=OPENAI_MODEL,
                temperature=0.3,
                openai_api_key=api_key,
                max_tokens=1024,
            )

        self.memory = ConversationBufferWindowMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
            k=5  # keep last 5 exchanges
        )

        if self.llm:
            combine_docs_chain_kwargs = {
                "prompt": ChatPromptTemplate.from_messages([
                    SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
                    HumanMessagePromptTemplate.from_template(HUMAN_PROMPT),
                ])
            }
            self.chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=self.retriever,
                memory=self.memory,
                return_source_documents=True,
                combine_docs_chain_kwargs=combine_docs_chain_kwargs,
                verbose=False,
            )
        else:
            self.chain = None

    def _mock_response(self, query: str, docs: list[Document]) -> dict:
        """Fallback response when no API key is available."""
        sources = [
            {"title": d.metadata.get("title", ""), "sdg": d.metadata.get("sdg", "")}
            for d in docs
        ]
        excerpt = docs[0].page_content[:400] if docs else "No relevant documents found."
        return {
            "answer": (
                f"⚠️ **Demo Mode** (no OpenAI API key configured)\n\n"
                f"Your query: *{query}*\n\n"
                f"**Most relevant knowledge base entry:** {sources[0]['title'] if sources else 'N/A'} "
                f"({sources[0]['sdg'] if sources else ''})\n\n"
                f"{excerpt}...\n\n"
                f"💡 **Eco Tip:** Set your `OPENAI_API_KEY` in `backend/.env` to get full AI-powered answers."
            ),
            "sources": sources,
        }

    def query(self, question: str, session_id: Optional[str] = None) -> dict:
        """Process a user query and return answer with sources."""
        # Always retrieve relevant docs for source attribution
        retrieved_docs = self.retriever.invoke(question)

        if self.chain is None:
            return self._mock_response(question, retrieved_docs)

        result = self.chain.invoke({"question": question})
        source_docs = result.get("source_documents", retrieved_docs)

        sources = []
        seen_ids = set()
        for doc in source_docs:
            doc_id = doc.metadata.get("id", "")
            if doc_id not in seen_ids:
                seen_ids.add(doc_id)
                sources.append({
                    "title": doc.metadata.get("title", ""),
                    "sdg": doc.metadata.get("sdg", ""),
                    "tags": doc.metadata.get("tags", ""),
                })

        return {
            "answer": result.get("answer", ""),
            "sources": sources,
        }

    def reset_memory(self):
        """Clear conversation memory."""
        self.memory.clear()


# ──────────────────────────────────────────────
# Singleton instance
# ──────────────────────────────────────────────
_rag_instance: Optional[EcoAssistRAG] = None


def get_rag_engine() -> EcoAssistRAG:
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = EcoAssistRAG()
    return _rag_instance
