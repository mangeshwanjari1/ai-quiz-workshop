# AI Quiz Workshop — Module 3

Adds quiz submission, deterministic marking, per-question feedback, SQLite attempt history, and the Module 2 material-path fix.

## Setup

1. Open a terminal in this folder.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: Windows PowerShell `.venv\Scripts\Activate.ps1`; macOS/Linux `source .venv/bin/activate`
4. Install: `python -m pip install -r requirements.txt`
5. Set your API key: PowerShell `$env:OPENAI_API_KEY="..."`; macOS/Linux `export OPENAI_API_KEY="..."`. Never commit secrets.
6. Run: `streamlit run app.py`
7. Student: ID `ST001`, LO `LO1`, Chapter `Introduction`, Topic `Basics`, count `3`. Create quiz, answer, submit, inspect score and attempt history.

## Important

`quiz_attempts.db` is created locally and excluded from Git. Teacher-uploaded material is stored as JSON in `materials/`. Do not use real student data: there is no authentication or access control. SQLite data on ephemeral cloud hosting may disappear on restart. A hosted persistent database and real login are needed for deployment with students. GPT may make mistakes; teachers should review generated answer keys.
