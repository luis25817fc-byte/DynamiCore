from fastapi import APIRouter
from pydantic import BaseModel
from collections import Counter
import re

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str

positive = {
    "increíble","bueno","excelente","genial","correcto",
    "bien","perfecto","rápido","éxito","funciona"
}

negative = {
    "malo","horrible","error","fallo","problema",
    "lento","terrible","incorrecto","bug","falla"
}

def sentiment(text):
    words = re.findall(r"\w+", text.lower(), re.UNICODE)

    score = (
        sum(w in positive for w in words)
        - sum(w in negative for w in words)
    )

    if score > 0:
        return "positivo", score
    elif score < 0:
        return "negativo", score
    return "neutral", 0


@router.post("/analyze")
def analyze(req: AnalyzeRequest):

    text = req.text

    words = re.findall(r"\w+", text.lower(), re.UNICODE)

    word_count = len(words)

    characters = len(text)

    avg_word_length = round(
        sum(len(w) for w in words) / word_count,
        2
    ) if word_count else 0

    top_words = [
        {"word": w, "count": c}
        for w, c in Counter(words).most_common(5)
    ]

    sentiment_label, sentiment_score = sentiment(text)

    sentences = max(
        1,
        len([s for s in re.split(r"[.!?]+", text) if s.strip()])
    )

    if avg_word_length < 5:
        complexity = "baja"
    elif avg_word_length < 7:
        complexity = "media"
    else:
        complexity = "alta"

    return {
        "status": "ok",
        "analysis": {
            "words": word_count,
            "characters": characters,
            "sentences": sentences,
            "avg_word_length": avg_word_length,
            "sentiment": sentiment_label,
            "sentiment_score": sentiment_score,
            "complexity": complexity,
            "top_words": top_words
        }
    }
