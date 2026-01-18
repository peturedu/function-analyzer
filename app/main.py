from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    html = Path("templates/analyzer.html").read_text(encoding="utf-8")
    return html


@app.get("/health")
def health():
    return {"status": "ok"}
