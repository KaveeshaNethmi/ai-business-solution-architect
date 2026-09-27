# 🤖 AI Business Discovery & Solution Architect

An **agentic AI engineering project** designed to understand how businesses operate, identify processes, pain points, and bottlenecks, and eventually recommend appropriate **software, automation, AI, or agentic AI solutions**.

The project is being developed progressively as both a practical system and a hands-on exploration of **production-oriented AI engineering**.

---

## 🎯 Vision

Many business problems do **not** require AI.

The long-term goal of this project is to build an intelligent system capable of interviewing a business owner, understanding how their business operates, identifying problems and their root causes, and determining whether each problem is best addressed through:

- 💻 Conventional software
- ⚙️ Workflow automation
- 🧠 AI-assisted functionality
- 🤖 AI agents
- 🔗 A combination of these approaches

The final system will generate a prioritized **Business AI Audit and Implementation Roadmap**.

---

## ✨ Planned Capabilities

The system will progressively support:

- 💬 Conversational business discovery
- 🗺️ Business process identification
- 🔍 Pain-point and bottleneck analysis
- 📊 Structured business knowledge extraction
- 🧩 Solution classification
- 🛠️ Tool and function calling
- 🧠 Persistent conversation state and memory
- 📚 Agentic RAG
- 👤 Human-in-the-loop workflows
- 🔌 MCP integrations
- 🤝 Multi-agent orchestration
- 🔀 Supervisor and agent handoffs
- 📋 Business AI audit generation
- 🛣️ Prioritized implementation roadmaps
- 📈 AI evaluation and observability
- ☁️ Production deployment

---

## 🏗️ Architecture

The project maintains separate **frontend** and **backend** applications.

```text
ai-business-solution-architect/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── graphs/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── .env.example
│   └── pyproject.toml
│
├── frontend/
│
├── docs/
├── .gitignore
└── README.md
```

---

## 🧰 Technology Stack

### Backend

- 🐍 Python
- ⚡ FastAPI
- 🕸️ LangGraph
- 🦜 LangChain
- 🧠 OpenAI
- 📦 Pydantic
- 🧪 pytest

### Frontend

- ⚛️ React
- 🔷 TypeScript
- ⚡ Vite

### Planned Infrastructure

- 🗄️ Database persistence
- 🔎 Vector search
- 🐳 Docker
- ☁️ AWS
- 📊 AI observability and evaluation tooling

---

## 🛣️ Development Roadmap

The system is intentionally being built **progressively**, rather than starting with a complex multi-agent architecture.

Each milestone introduces new AI engineering concepts while extending the system's capabilities.

### 🚧 Milestone 1 — Agent Fundamentals

**Current focus**

- [x] Project initialization
- [x] Separate frontend and backend applications
- [x] Business discovery agent state
- [x] LangGraph nodes and edges
- [x] Structured LLM output with Pydantic
- [x] Conversation message state
- [x] LangGraph message reducers
- [x] Multi-turn discovery
- [x] Thread-based checkpointing
- [ ] Business discovery FastAPI endpoint
- [ ] Frontend/backend integration

### 🧠 Milestone 2 — Persistent State & Memory

- [ ] Persistent checkpoint storage
- [ ] Business discovery sessions
- [ ] Long-term business memory
- [ ] Database integration

### 🛠️ Milestone 3 — Tool Calling

- [ ] Tool definitions
- [ ] LLM tool selection
- [ ] Tool execution
- [ ] Tool result handling
- [ ] Error handling and guardrails

### 🔍 Milestone 4 — Structured Business Analysis

- [ ] Process mapping
- [ ] Pain-point analysis
- [ ] Root-cause identification
- [ ] Solution classification
- [ ] Prioritization

### 📚 Milestone 5 — Agentic RAG

- [ ] Business document ingestion
- [ ] Embeddings
- [ ] Vector search
- [ ] Context retrieval
- [ ] Agent-controlled retrieval

### 👤 Milestone 6 — Human in the Loop

- [ ] Approval points
- [ ] Interruptible workflows
- [ ] Human review and correction

### 🔌 Milestone 7 — Model Context Protocol (MCP)

- [ ] MCP concepts
- [ ] MCP servers and clients
- [ ] External system integrations

### 🤝 Milestone 8 — Multi-Agent Architecture

The initial single-agent architecture will progressively evolve into specialized agents where specialization provides a clear engineering benefit.

```text
Business Owner
      │
      ▼
┌─────────────────┐
│   Supervisor    │
└────────┬────────┘
         │
         ├──► Discovery Agent
         │
         ├──► Process Analyst
         │
         ├──► Pain-Point Analyst
         │
         ├──► Solution Architect
         │
         └──► Roadmap / ROI Agent
```

The project deliberately avoids introducing multiple agents simply for architectural complexity.

Multi-agent orchestration will be introduced only when **specialization, routing, or independent reasoning provides a meaningful engineering advantage**.

### 📊 Milestone 9 — Evaluation & Observability

- [ ] Agent traces
- [ ] Structured evaluation
- [ ] Prompt evaluation
- [ ] Workflow evaluation
- [ ] Failure analysis
- [ ] Cost monitoring
- [ ] Latency monitoring

### 🚀 Milestone 10 — Production Deployment

- [ ] Docker
- [ ] Persistent databases
- [ ] Production API architecture
- [ ] AWS deployment
- [ ] Monitoring
- [ ] Security
- [ ] Configuration management

---

## 🔄 Current Discovery Flow

The current **Milestone 1** workflow is intentionally simple.

```text
Business Owner
      │
      ▼
 HumanMessage
      │
      ▼
BusinessDiscoveryState
      │
      ▼
   LangGraph
      │
      ▼
Discovery Agent Node
      │
      ├── System Instructions
      ├── Conversation History
      └── Structured Business State
      │
      ▼
 OpenAI Model
      │
      ▼
DiscoveryResult
      │
      ▼
 State Update
      │
      ▼
  Checkpoint
```

The Discovery Agent currently extracts structured information including:

- 🏢 Industry
- 💼 Business model
- 👥 Employee count
- 🛒 Order/customer channels
- 🔄 Business processes
- ⚠️ Pain points
- ✅ Discovery completion status

The agent also generates the **next appropriate discovery question** based on the information already collected.

---

## ⚙️ Backend Setup

### 1. Navigate to the backend

```bash
cd backend
```

### 2. Install dependencies

The backend uses `uv` for Python dependency management.

```bash
uv sync
```

### 3. Configure Environment Variables

Create your local `.env` file from the provided example.

**macOS / Linux**

```bash
cp .env.example .env
```

**Windows PowerShell**

```powershell
Copy-Item .env.example .env
```

Then add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the Development Server

```bash
uv run fastapi dev app/main.py
```

Once the server is running, FastAPI's interactive API documentation is available through the local Swagger interface.

---

## 💻 Frontend Setup

### 1. Navigate to the frontend

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start the Development Server

```bash
npm run dev
```

---

## 🔐 Security

Secrets must **never** be committed to Git.

Local environment files such as:

```text
.env
```

are excluded through the root `.gitignore`.

Only:

```text
.env.example
```

containing placeholder configuration values should be committed.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

Before committing changes, always verify that `.env` is ignored:

```bash
git status
```

Your actual API key should **never appear in staged files or Git history**.

---

## 🧪 Testing

Backend tests are written using **pytest**.

From the `backend` directory:

```bash
uv run pytest
```

For more detailed output:

```bash
uv run pytest -v
```

Tests will progressively cover:

- Agent state behavior
- Discovery nodes
- Structured LLM responses
- Graph execution
- State transitions
- API behavior
- Tool execution
- Persistence
- Agent workflows

---

## 🌿 Development & Git Workflow

Development follows a **feature-branch workflow** to maintain a clear and meaningful Git history.

The `main` branch should represent stable project progress.

New work should be developed on dedicated branches such as:

```text
feature/discovery-api
feature/persistent-memory
feature/tool-calling
feature/business-analysis
feature/agentic-rag
feature/human-in-the-loop
feature/mcp-integration
feature/multi-agent
```

Example workflow:

```bash
git checkout main
git pull origin main

git checkout -b feature/discovery-api
```

After implementing and testing the feature:

```bash
git add .
git commit -m "feat: add business discovery API endpoint"
git push -u origin feature/discovery-api
```

The feature can then be reviewed and merged into `main`.

This approach keeps the repository history aligned with the architectural evolution of the project.

---

## 🧭 Development Philosophy

This project deliberately avoids jumping directly into a large multi-agent architecture.

Each milestone introduces a new AI engineering concept only after the underlying concepts are understood, implemented, and tested.

The goal is **not simply to build an application that calls an LLM**.

The goal is to understand and engineer the systems surrounding intelligent applications:

```text
State
  ↓
Reasoning
  ↓
Tools
  ↓
Memory
  ↓
Orchestration
  ↓
Evaluation
  ↓
Deployment
```

This progression allows the project to evolve from a simple conversational discovery agent into a production-oriented **AI Business Discovery & Solution Architecture platform**.

---

## 📌 Project Status

🚧 **Currently under active development — Milestone 1: Agent Fundamentals**

The current focus is completing the Business Discovery workflow and exposing it through FastAPI before connecting it to the frontend.

---

## 🔮 Long-Term Goal

The final system should be capable of moving from:

> **"Tell me how your business works."**

to:

> **"Here are the highest-impact problems in your business, their likely root causes, which ones should be solved first, and whether each requires software, automation, AI, or an agentic solution."**

The output will ultimately become a structured:

### 📋 Business AI Audit

and

### 🛣️ Prioritized Implementation Roadmap

designed to help businesses adopt technology based on **actual operational needs rather than AI hype**.

---

## 📄 License

This project is currently being developed for learning, experimentation, and portfolio purposes.

License information will be added as the project evolves.