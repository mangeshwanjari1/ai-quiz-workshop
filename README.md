# AI Quiz Workshop — Module 2

Simple Streamlit + GPT + teacher-content retrieval demo. **Not production-ready.**

## Setup

```bash
python -m venv .venv
# Mac/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set your OpenAI API key in an environment variable (do not commit it):

- Mac/Linux: `export OPENAI_API_KEY="your-key"`
- Windows PowerShell: `$env:OPENAI_API_KEY="your-key"`

Run `streamlit run app.py`.

Choose Student, keep LO1 / Introduction / Basics, and generate three questions using the included sample material. Or choose Teacher and upload a UTF-8 `.txt` file with your own LO, chapter and topic.

## Limitations

- No real login, scoring, database or email yet.
- Local files on free cloud hosting may be lost after restarts; use persistent storage later.
- This module uses exact metadata matching, not semantic vector search.
- API usage may incur charges; never publish API keys.
- Uploaded teacher material should not contain personal or confidential data.
