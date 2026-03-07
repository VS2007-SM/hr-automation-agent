# 🤖 HR Automation Agent — Nasiko Buildathon

An all-in-one AI agent that automates the most time-consuming HR workflows:
**Recruitment**, **Onboarding**, and **HR Helpdesk**.

---

## 💡 Problem It Solves

HR teams spend hours on repetitive tasks — screening resumes, writing emails,
answering the same policy questions, onboarding new hires. This agent handles
all of that automatically using natural language, so HR can focus on people.

---

## ⚙️ Features

### 🎯 Recruitment
- **Screen resumes** — Score a candidate (0–100) against a job description with strengths, gaps, and a shortlist recommendation
- **Draft interview emails** — Generate personalized interview invitation emails instantly

### 🚀 Onboarding
- **Onboarding checklists** — Role-specific plans covering Pre-Arrival, Day 1, Week 1, and Month 1
- **New hire Q&A** — Answer common questions from employees joining the company

### 🙋 HR Helpdesk
- **Policy queries** — Answer questions about leave, payroll, benefits, and more
- **Issue escalation** — Create structured escalation tickets with urgency levels for complex issues

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker Desktop
- OpenAI API Key

### Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/hr-automation-agent.git
cd hr-automation-agent

# 2. Build the Docker image
docker build -t hr-automation-agent .

# 3. Run the agent
docker run -p 5000:5000 -e OPENAI_API_KEY=your_key_here hr-automation-agent
```

### Test It

```bash
# Screen a resume
curl -X POST http://localhost:5000/ \
-H "Content-Type: application/json" \
-d '{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [{"kind": "text", "text": "Screen this candidate: Job requires 3 years Python experience and team leadership. Candidate has 4 years Python, built 2 products, led a team of 5."}]
    }
  }
}'

# Generate onboarding checklist
curl -X POST http://localhost:5000/ \
-H "Content-Type: application/json" \
-d '{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [{"kind": "text", "text": "Generate an onboarding checklist for Priya Sharma, joining as Backend Engineer in the Engineering department on March 15."}]
    }
  }
}'

# Answer HR policy question
curl -X POST http://localhost:5000/ \
-H "Content-Type: application/json" \
-d '{
  "jsonrpc": "2.0",
  "id": "3",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [{"kind": "text", "text": "How many sick leaves am I entitled to per year?"}]
    }
  }
}'
```

---

## 📁 Project Structure

```
hr-automation-agent/
├── src/
│   ├── __main__.py     # FastAPI server + A2A JSON-RPC handler
│   ├── agent.py        # LangChain agent with HR system prompt
│   ├── tools.py        # 6 HR automation tools
│   ├── models.py       # A2A protocol data models
│   └── __init__.py
├── Dockerfile
├── docker-compose.yml
├── AgentCard.json
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.11** + FastAPI + Uvicorn
- **LangChain** (tool-calling agent)
- **OpenAI GPT-4o**
- **Docker** (containerized deployment)
- **A2A Protocol** (JSON-RPC 2.0)
- **Nasiko Infrastructure**

---

## 👥 Team

Built for the **Nasiko AI Agent Buildathon**
