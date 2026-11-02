# AI Quiz Workshop — Module 5

Extends Module 4 with **Agent 2: email feedback**. Previous accounts and attempts remain intact.

## Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Set `OPENAI_API_KEY` and `TEACHER_PASSWORD` as in Module 4. To send email, set these environment variables (or Streamlit secrets):

- `SMTP_HOST` — your email provider SMTP server
- `SMTP_PORT` — usually 465 (SSL) or 587 (STARTTLS)
- `SMTP_USER` — SMTP username
- `SMTP_PASSWORD` — SMTP password or provider-specific app password
- `SMTP_FROM` — verified sender address

**Never commit passwords or API keys.** SMTP sending may have provider limits and may require account configuration. Email is sent only when the student has opted in and supplied an email address.

## Demo steps

1. Log in as a student, enter an email address, check opt-in and save.
2. Generate and submit a quiz. The attempt saves even if email fails.
3. Check the email status displayed with the score.
4. Log in as teacher, select the attempt, preview the exact email and optionally send again.
5. Inspect the `email_log` table with SQLite Browser.

## Limitations

This is a **workshop prototype**. It uses a single shared teacher password, local SQLite and local uploaded materials; free ephemeral hosting does not reliably persist either. There is no queue, retry scheduler, verified email ownership, or production email deliverability guarantee. The email agent is a deterministic automation using GPT-produced explanations from Agent 1, not a separate GPT model call. Use synthetic student data for demos.
