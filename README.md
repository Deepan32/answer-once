# Answer Once

**Small kitchens answer each question once. AI answers everyone.**

Built during the Meta Global AI Developer Hackathon (Oct 27 – Nov 4, 2026). All code in this repo was written during the hackathon.

## MVP
1. Customers send questions (chat or simulator)
2. Similar pending questions are grouped ("8 waiting")
3. Owner answers each group once
4. Every waiting customer gets a personalized reply
5. Answers are remembered, so repeats are answered instantly

## Layout
- `app/llm.py`      – thin wrapper around model calls (stand-ins now, Meta models later)
- `app/store.py`    – SQLite: messages, pending groups, approved facts
- `app/grouping.py` – embedding similarity + threshold
- `app/memory.py`   – match new questions to approved facts
- `app/main.py`     – FastAPI app (API + WebSockets later)
- `scripts/simulate_rush.py` – fires overlapping fake customer questions
- `tests/grouping_pairs.csv` – labeled same/different pairs to tune the threshold

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
