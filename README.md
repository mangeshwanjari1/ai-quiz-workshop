# AI Quiz Workshop — Module 4

## Features
Student registration/login, GPT-generated quizzes based on teacher material, automatic MCQ marking, SQLite attempt history, student progress chart, teacher login, upload, attempt filtering and detailed review.

## Start
1. Python 3.10+ recommended.
2. `python -m venv .venv`
3. Activate: Windows PowerShell `.venv\Scripts\Activate.ps1` / macOS `source .venv/bin/activate`
4. `python -m pip install -r requirements.txt`
5. Set `OPENAI_API_KEY` and `TEACHER_PASSWORD` environment variables (see below).
6. `streamlit run app.py`

Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="YOUR_KEY"
$env:TEACHER_PASSWORD="CHOOSE_A_LONG_RANDOM_PASSWORD"
streamlit run app.py
```

macOS Terminal:
```bash
export OPENAI_API_KEY="YOUR_KEY"
export TEACHER_PASSWORD="CHOOSE_A_LONG_RANDOM_PASSWORD"
streamlit run app.py
```

## Test
- Register ST001 with a password of at least 8 characters; log in.
- Choose LO1 / Introduction / Basics (sample included), generate and submit a quiz.
- Take a second quiz and see progress.
- Log out; log in as Teacher using TEACHER_PASSWORD; filter attempts and open question feedback.
- Upload a UTF-8 `.txt` file with a new LO, chapter, topic; log in as student and select it from the dropdown.
- Try incorrect passwords; they should fail.

## GitHub
```bash
git status
git add .
git commit -m "Module 4: teacher dashboard and basic login"
git push origin main
```

## Limitations
This is a teaching demo, not a production student information system. Teacher uses a shared password; no email verification, rate limiting, password reset, role administration, audit log or HTTPS enforcement by the application. The local SQLite DB and uploaded files are not reliable persistent storage on ephemeral cloud hosts. Never commit API keys, teacher passwords, or actual student data. GPT-generated keys and explanations can be inaccurate; teachers should review quizzes before high-stakes use. Existing Module 3 attempts remain in the database, but older demo student IDs must register before logging in.
