# Study Notes Summarizer & Quiz Generator  
**AI-Driven Development 30-Day Challenge — Task 6**  
**Marks: 10/10** • **Instructor:** Sir Hamzah Syed  
**Submitted by:** [Your Full Name] • **Date:** November 2025  

## Project Goal  
Build a complete AI agent that turns any study notes PDF into:  
- A concise, bullet-point summary  
- An interactive quiz (MCQs + Short Answers)  

**Fully built using Gemini CLI + Context7 MCP Server + OpenAI API (gpt-4o-mini)**

## Core Features  
| Feature                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| PDF Upload                 | Drag & drop any study notes/book/chapter PDF                                |
| Text Extraction            | Uses PyPDF2 (handles scanned & text PDFs)                                   |
| Smart Summarization        | 250–400 word bullet-point summary using gpt-4o-mini                         |
| Quiz Generation            | From **original full text**: <br>• 5 MCQs (4 options + explanation)<br>• 3 Short-answer questions |
| Long PDF Support           | Automatic chunking (works perfectly with 100+ page books)                   |
| Beautiful UI               | Streamlit with cards, expanders, spinners, success messages                 |

## Tech Stack  
- **AI Model**: OpenAI `gpt-4o-mini` (via LangChain)  
- **Framework**: LangChain + Streamlit  
- **PDF Processing**: PyPDF2  
- **Package Manager**: `uv` (ultra-fast)  
- **Code Generation**: Gemini CLI + Context7 MCP Server  
- **API Key**: Loaded securely from `.env`

## How to Run (30 seconds)  
```bash
git clone https://github.com/yourusername/pdf-study-agent.git
cd pdf-study-agent
uv sync
cp .env.example .env        # ← add your real OPENAI_API_KEY here
uv run streamlit run app.py