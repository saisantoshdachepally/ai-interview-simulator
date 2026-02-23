
# 🤖 AI Interview Simulator

An AI-powered interview preparation platform that generates role-based interview questions and evaluates candidate answers using Large Language Models.

🚀 **Live Demo:**  
👉 https://huggingface.co/spaces/santosh0223/ai-interview-simulator

---

## 📌 Features

- 🎯 Role-based interview questions (ML Engineer, Backend, Data, etc.)
- 📊 Difficulty selection (Easy / Medium / Hard)
- 🤖 AI-powered answer evaluation
- ⚡ Instant feedback with score & suggestions
- 🌐 Live deployed on Hugging Face Spaces

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **LLM Provider:** Groq (LLaMA 3.3 70B)  
- **Deployment:** Hugging Face Spaces  
- **Backend (Local Version):** FastAPI  

---

## 🖥 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-interview-simulator.git
cd ai-interview-simulator
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key_here
5️⃣ Run App
streamlit run app.py
🎯 Project Goals

This project was built to:

Help students prepare for technical interviews

Simulate real-world AI interview environments

Demonstrate full-stack AI application development

Showcase LLM integration skills

🌍 Live Deployment

Hosted on Hugging Face Spaces:

👉 https://huggingface.co/spaces/santosh0223/ai-interview-simulator
