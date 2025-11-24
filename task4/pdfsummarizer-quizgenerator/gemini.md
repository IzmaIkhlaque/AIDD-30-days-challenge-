You are an expert Python agent developer using OpenAI API + LangChain.

Project: Study Notes Summarizer & Quiz Generator

Requirements:
- User uploads PDF → extract text with PyPDF2
- Button "Generate Summary" → beautiful bullet-point summary (250–400 words) using gpt-4o-mini or gpt-4o
- Button "Create Quiz" → from ORIGINAL full text, generate:
  → 5 high-quality MCQs (4 options, 1 correct, with explanation)
  → 3 short-answer questions
- Use proper text chunking for long PDFs (>50 pages)
- Use OpenAI API directly (via langchain-openai or openai python package)
- Load OPENAI_API_KEY from .env
- Full Streamlit UI with nice cards, expanders, success messages
- Dependencies installable via uv add
- Generate two files: agent.py (core logic) + app.py (Streamlit)

Always output complete, runnable code that works with:
uv run streamlit run app.py