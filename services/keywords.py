# services/keywords.py
from config import config


def match_keywords(text: str) -> list[str]:
    """Возвращает список найденных ключевых слов"""
    found = []
    txt = text.lower()
    for kw in config.keywords:
        if kw.lower() in txt:
            found.append(kw)
    return found