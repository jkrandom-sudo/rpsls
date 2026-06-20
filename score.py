"""Score persistence."""
import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".rpsls_scores.json"
MAX_SCORES = 10
MAX_NAME_LENGTH = 20
MIN_NAME_LENGTH = 1


def validate_name(name):
    """Validate and sanitize player name for scoreboard.

    Returns (is_valid, cleaned_name).
    """
    if not name:
        return False, ""
    cleaned = name.strip()[:MAX_NAME_LENGTH]
    if len(cleaned) < MIN_NAME_LENGTH:
        return False, ""
    return True, cleaned


def load(path=None):
    if path is None:
        path = DEFAULT_PATH
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []


def save(scores, path=None):
    if path is None:
        path = DEFAULT_PATH
    with open(path, "w", encoding="utf-8") as f:
        json.dump(scores[:MAX_SCORES], f, ensure_ascii=False, indent=2)


def add(name, score, difficulty, path=None):
    scores = load(path)
    scores.append({"name": name, "score": score, "difficulty": difficulty})
    scores.sort(key=lambda item: item.get("score", 0), reverse=True)
    save(scores, path)
