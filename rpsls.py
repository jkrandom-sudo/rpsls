"""Core logic for Rock Paper Scissors Lizard Spock."""
import random

MOVES = ("rock", "paper", "scissors", "lizard", "spock")
ALIASES = {
    "r": "rock", "rock": "rock", "石头": "rock",
    "p": "paper", "paper": "paper", "布": "paper",
    "s": "scissors", "scissors": "scissors", "剪刀": "scissors",
    "l": "lizard", "lizard": "lizard", "蜥蜴": "lizard",
    "k": "spock", "spock": "spock", "斯波克": "spock",
}
WIN_RULES = {
    "rock": {"scissors": "crushes", "lizard": "crushes"},
    "paper": {"rock": "covers", "spock": "disproves"},
    "scissors": {"paper": "cuts", "lizard": "decapitates"},
    "lizard": {"spock": "poisons", "paper": "eats"},
    "spock": {"scissors": "smashes", "rock": "vaporizes"},
}
ROUNDS_BY_DIFFICULTY = {"easy": 3, "normal": 5, "hard": 7}
POINTS_BY_DIFFICULTY = {"easy": 10, "normal": 15, "hard": 20}


def normalize_move(text):
    return ALIASES.get(text.strip().lower())


def random_move(rng=None):
    rng = rng or random
    return rng.choice(MOVES)


def winner(player, computer):
    if player == computer:
        return "draw"
    if computer in WIN_RULES[player]:
        return "player"
    return "computer"


def verb_for(winning_move, losing_move):
    return WIN_RULES[winning_move][losing_move]


def round_points(difficulty, streak):
    base = POINTS_BY_DIFFICULTY.get(difficulty, POINTS_BY_DIFFICULTY["normal"])
    return base + max(0, streak - 1) * 5


def final_score(difficulty, wins, draws, best_streak):
    base = POINTS_BY_DIFFICULTY.get(difficulty, POINTS_BY_DIFFICULTY["normal"])
    return wins * base + draws * 2 + best_streak * 5
