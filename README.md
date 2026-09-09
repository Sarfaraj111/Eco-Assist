# 🌿 EcoAssist — AI-Powered RAG Assistant for Pollution Awareness & Sustainable Development

An intelligent Retrieval-Augmented Generation (RAG) chatbot that answers questions about
pollution, climate change, and sustainability — grounded in a curated knowledge base aligned
to four UN Sustainable Development Goals.

## 🎯 SDG Coverage

| SDG | Theme | Topics |
|-----|-------|--------|
| **SDG 13** 🌍 | Climate Action | Carbon emissions, Paris Agreement, mitigation, adaptation, net-zero |
| **SDG 11** 🏙️ | Sustainable Cities | Air pollution, urban transport, waste management, green buildings, UHI |
| **SDG 12** ♻️ | Responsible Consumption | Plastic pollution, food waste, fast fashion, circular economy |
| **SDG 3** 💚 | Good Health & Well-being | Health effects of air/water/soil/noise/light pollution, PFAS, heavy metals |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    EcoAssist                        │
│                                                     │
│  ┌───────────────┐       ┌────────────────────┐    │
│  │  React + Vite │ ───── │  FastAPI Backend    │    │
│  │  (Tailwind)   │       │  (Python)           │    │
│  └───────────────┘       └────────────────────┘    │
│                                    │                │
│                          ┌─────────▼──────────┐    │
│                          │   RAG Pipeline      │    │
│                          │ ┌────────────────┐  │    │
│                          │ │ FAISS VectorDB │  │    │
│                          │ │ HuggingFace    │  │    │
│                          │ │ Embeddings     │  │    │
│                          │ └────────────────┘  │    │
│                          │ ┌────────────────┐  │    │
│                          │ │  OpenAI GPT-4o │  │    │
│                          │ │  mini LLM      │  │    │
│                          │ └────────────────┘  │    │
│                          └────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

### RAG Pipeline
1. **Query** arrives from the user
2. **Embedding** model (`all-MiniLM-L6-v2`) converts query to vector
3. **FAISS** retrieves the top-4 most relevant knowledge base chunks
4. **Prompt** is constructed with retrieved context + conversation history
5. **GPT-4o-mini** generates a grounded, SDG-tagged response with eco tips
6. **Sources** are returned alongside the answer for transparency

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **OpenAI API key** (get one at https://platform.openai.com)

---

### Backend Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env
# Edit .env and set your OPENAI_API_KEY

# 5. Run the server
uvicorn main:app --reload --port 8000
```

The backend will:
- Build the FAISS vector index on first run (takes ~30 seconds)
- Save the index to `backend/rag/faiss_index/` for fast subsequent starts
- Serve the API at `http://localhost:8000`

**API Docs:** http://localhost:8000/docs

---

### Frontend Setup

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev
```

Open **http://localhost:5173** in your browser.

---

## 🔧 Configuration

### `backend/.env`
```env
OPENAI_API_KEY=sk-...           # Your OpenAI API key
MODEL_NAME=gpt-4o-mini          # OpenAI model (gpt-4o-mini recommended)
EMBEDDING_MODEL=all-MiniLM-L6-v2  # HuggingFace sentence-transformer model
```

### Running without an OpenAI API key
EcoAssist works in **Demo Mode** without an API key — it retrieves relevant knowledge base
entries and shows them directly. Set your API key in `.env` for full AI-generated responses.

---

## 📁 Project Structure

```
Eco-Assist/
├── backend/
│   ├── main.py                      # FastAPI app & routes
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment template
│   ├── knowledge_base/
│   │   └── sdg_knowledge.py         # Curated SDG knowledge corpus (20 topics)
│   └── rag/
│       ├── engine.py                # RAG pipeline (FAISS + LangChain + OpenAI)
│       └── faiss_index/             # Auto-generated vector index (gitignored)
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.ts
    ├── tailwind.config.js
    └── src/
        ├── App.tsx                  # Root component
        ├── main.tsx                 # Entry point
        ├── index.css                # Global styles + Tailwind
        ├── types.ts                 # TypeScript types & SDG config
        ├── api/
        │   └── chat.ts              # Backend API client
        ├── hooks/
        │   └── useChat.ts           # Chat state management hook
        └── components/
            ├── Header.tsx           # Top navigation bar
            ├── WelcomeScreen.tsx    # Landing screen with suggestions
            ├── ChatBubble.tsx       # User & assistant message bubbles
            ├── ChatInput.tsx        # Text input with auto-resize
            └── SDGBadge.tsx         # Coloured SDG category badge
```

---

## 🌐 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | API info |
| `GET` | `/health` | Health check |
| `POST` | `/api/chat` | Send a message, get AI response + sources |
| `POST` | `/api/reset` | Clear conversation memory |
| `GET` | `/api/topics` | List all knowledge base topics |

### Chat request/response
```json
// POST /api/chat
{ "question": "How does air pollution affect health?", "session_id": null }

// Response
{
  "answer": "📌 SDG 3 – Good Health\n\n...",
  "sources": [
    { "title": "Health Effects of Air Pollution", "sdg": "SDG 3", "tags": "health, PM2.5..." }
  ],
  "session_id": "abc123"
}
```

---

## 📚 Knowledge Base Topics

The built-in knowledge base covers 20 expert-curated topics:

**SDG 13 – Climate Action**
- Understanding Climate Change
- Carbon Emissions and Mitigation Strategies
- Climate Change Adaptation

**SDG 11 – Sustainable Cities**
- Air Pollution in Cities (WHO guidelines)
- Sustainable Urban Transport
- Waste Management in Urban Areas
- Green Buildings and Sustainable Architecture
- Urban Heat Islands and Green Infrastructure

**SDG 12 – Responsible Consumption**
- Plastic Pollution: Causes, Effects, Solutions
- Sustainable Food Systems and Food Waste
- Fast Fashion and Textile Pollution
- Circular Economy Principles
- Marine and Ocean Pollution

**SDG 3 – Good Health**
- Health Effects of Air Pollution
- Water Pollution and Human Health
- Soil Pollution and Health Effects
- Noise Pollution and Mental Health
- Light Pollution and Its Effects
- Chemical Pollution and Human Health (PFAS, EDCs)
- Climate Change and Health Impacts

---

## 🤝 Contributing

To extend the knowledge base, add new entries to `backend/knowledge_base/sdg_knowledge.py`
following the existing schema, then delete `backend/rag/faiss_index/` to trigger a rebuild.

---

## 📄 License

MIT License — built for the UN SDG Hackathon 2024.
