"""Console RPSLS game."""
import random
import sys

import i18n
import rpsls
import score as score_mod
import settings as settings_mod
from sound import Sound


class QuitGame(Exception):
    pass


def _print(out, text=""):
    print(text, file=out)


def show_header(settings, out):
    _print(out, "=" * 36)
    _print(out, i18n.t(settings["lang"], "title"))
    _print(out, "=" * 36)


def show_help(settings, input_func=input, out=sys.stdout):
    lang = settings["lang"]
    show_header(settings, out)
    _print(out, i18n.t(lang, "help_title"))
    _print(out, i18n.t(lang, "help_text"))
    input_func(i18n.t(lang, "press_enter"))


def show_scores(settings, input_func=input, out=sys.stdout):
    lang = settings["lang"]
    show_header(settings, out)
    _print(out, i18n.t(lang, "scores"))
    scores = score_mod.load()
    if not scores:
        _print(out, i18n.t(lang, "no_scores"))
    for idx, item in enumerate(scores, 1):
        _print(out, f"{idx}. {item['name']} - {item['score']} ({item['difficulty']})")
    input_func(i18n.t(lang, "press_enter"))


def settings_menu(settings, input_func=input, out=sys.stdout):
    while True:
        lang = settings["lang"]
        show_header(settings, out)
        _print(out, i18n.t(lang, "settings"))
        _print(out, f"{i18n.t(lang, 'lang')}: {settings['lang']}")
        _print(out, f"{i18n.t(lang, 'sound')}: {i18n.t(lang, 'on' if settings['sound'] else 'off')}")
        _print(out, f"{i18n.t(lang, 'volume')}: {settings['volume']}")
        _print(out, f"{i18n.t(lang, 'difficulty')}: {settings['difficulty']}")
        _print(out, i18n.t(lang, "settings_menu"))
        choice = input_func(i18n.t(lang, "choice")).strip().lower()
        if choice == "1":
            settings_mod.cycle_lang(settings)
        elif choice == "2":
            settings_mod.toggle_sound(settings)
        elif choice == "3":
            settings_mod.cycle_volume(settings)
        elif choice == "4":
            settings_mod.cycle_difficulty(settings)
        elif choice in ("b", "q"):
            settings_mod.save(settings)
            return
        else:
            _print(out, i18n.t(lang, "unknown"))


def _move(lang, move):
    return i18n.move_name(lang, move)


def play_round(settings, sound, input_func=input, out=sys.stdout, rng=None):
    rng = rng or random.Random()
    lang = settings["lang"]
    difficulty = settings["difficulty"]
    total = rpsls.ROUNDS_BY_DIFFICULTY[difficulty]
    wins = losses = draws = score = streak = best_streak = 0
    for round_no in range(1, total + 1):
        _print(out, i18n.t(lang, "round_status", round=round_no,
                           total=total, wins=wins, losses=losses,
                           draws=draws, score=score))
        try:
            raw = input_func(i18n.t(lang, "move_prompt"))
        except EOFError as exc:
            raise QuitGame() from exc
        if raw.strip().lower() == "q":
            return None
        player = rpsls.normalize_move(raw)
        if not player:
            _print(out, i18n.t(lang, "invalid_move"))
            sound.incorrect()
            continue
        computer = rpsls.random_move(rng)
        outcome = rpsls.winner(player, computer)
        if outcome == "draw":
            draws += 1
            streak = 0
            score += 2
            _print(out, i18n.t(lang, "round_draw", move=_move(lang, player)))
        elif outcome == "player":
            wins += 1
            streak += 1
            best_streak = max(best_streak, streak)
            points = rpsls.round_points(difficulty, streak)
            score += points
            sound.correct()
            _print(out, i18n.t(lang, "round_win", player=_move(lang, player),
                               verb=i18n.verb(lang, rpsls.verb_for(player, computer)),
                               computer=_move(lang, computer), points=points))
        else:
            losses += 1
            streak = 0
            sound.incorrect()
            _print(out, i18n.t(lang, "round_loss", computer=_move(lang, computer),
                               verb=i18n.verb(lang, rpsls.verb_for(computer, player)),
                               player=_move(lang, player)))
    if wins > losses:
        result = "win"
        sound.win()
        _print(out, i18n.t(lang, "result_win", score=score))
    elif losses > wins:
        result = "loss"
        sound.lose()
        _print(out, i18n.t(lang, "result_loss", score=score))
    else:
        result = "draw"
        _print(out, i18n.t(lang, "result_draw", score=score))
    return {"result": result, "score": score, "wins": wins,
            "losses": losses, "draws": draws, "best_streak": best_streak,
            "difficulty": difficulty}


def main_menu(input_func=input, out=sys.stdout):
    settings = settings_mod.load()
    while True:
        lang = settings["lang"]
        sound = Sound(settings["sound"], settings["volume"], out)
        show_header(settings, out)
        _print(out, i18n.t(lang, "main_menu"))
        try:
            choice = input_func(i18n.t(lang, "choice")).strip().lower()
        except EOFError:
            choice = "q"
        if choice == "p":
            try:
                result = play_round(settings, sound, input_func, out)
            except QuitGame:
                _print(out, i18n.t(lang, "bye"))
                return
            if result and result["score"] > 0:
                name = input_func(i18n.t(lang, "name_prompt")).strip()
                if name:
                    score_mod.add(name, result["score"], result["difficulty"])
                    _print(out, i18n.t(lang, "saved"))
                else:
                    _print(out, i18n.t(lang, "not_saved"))
        elif choice == "h":
            show_help(settings, input_func, out)
        elif choice == "s":
            settings_menu(settings, input_func, out)
        elif choice == "c":
            show_scores(settings, input_func, out)
        elif choice == "q":
            _print(out, i18n.t(lang, "bye"))
            return
        else:
            _print(out, i18n.t(lang, "unknown"))


if __name__ == "__main__":
    main_menu()
