from fastapi import APIRouter
from pydantic import BaseModel
import re
from collections import Counter

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str


@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    text = req.text.strip()

    if not text:
        return {"status": "error", "message": "Texto vacío"}

    words = re.findall(r"\b\w+\b", text.lower())
    chars = len(text)
    sentences = len(re.split(r"[.!?]+", text)) - 1

    freq = Counter(words)
    most_common = freq.most_common(5)

    positive = {"bueno","genial","excelente","amor","feliz","increíble","bien","perfecto"}
    negative = {"malo","horrible","triste","odio","feo","terrible","mal"}

    score = 0
    for w in words:
        if w in positive:
            score += 1
        elif w in negative:
            score -= 1

    sentiment = "neutral"
    if score > 0:
        sentiment = "positivo"
    elif score < 0:
        sentiment = "negativo"

    avg_len = sum(len(w) for w in words) / len(words) if words else 0

    complexity = "baja"
    if avg_len > 4:
        complexity = "media"
    if avg_len > 6:
        complexity = "alta"

    return {
        "status": "ok",
        "analysis": {
            "words": len(words),
            "characters": chars,
            "sentences": sentences,
            "avg_word_length": round(avg_len, 2),
            "sentiment": sentiment,
            "sentiment_score": score,
            "complexity": complexity,
            "top_words": [{"word": w, "count": c} for w, c in most_common]
        }
    }
