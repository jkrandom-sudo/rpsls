"""Tests for RPSLS core."""
import os
import random
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import rpsls


class TestMoves(unittest.TestCase):
    def test_moves_count(self):
        self.assertEqual(len(rpsls.MOVES), 5)

    def test_normalize_shortcuts(self):
        self.assertEqual(rpsls.normalize_move("r"), "rock")
        self.assertEqual(rpsls.normalize_move("K"), "spock")

    def test_normalize_chinese(self):
        self.assertEqual(rpsls.normalize_move("石头"), "rock")
        self.assertEqual(rpsls.normalize_move("蜥蜴"), "lizard")

    def test_normalize_invalid(self):
        self.assertIsNone(rpsls.normalize_move("bad"))

    def test_random_move(self):
        self.assertIn(rpsls.random_move(random.Random(0)), rpsls.MOVES)


class TestWinner(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(rpsls.winner("rock", "rock"), "draw")

    def test_rock_beats_scissors_lizard(self):
        self.assertEqual(rpsls.winner("rock", "scissors"), "player")
        self.assertEqual(rpsls.winner("rock", "lizard"), "player")

    def test_paper_beats_rock_spock(self):
        self.assertEqual(rpsls.winner("paper", "rock"), "player")
        self.assertEqual(rpsls.winner("paper", "spock"), "player")

    def test_scissors_beats_paper_lizard(self):
        self.assertEqual(rpsls.winner("scissors", "paper"), "player")
        self.assertEqual(rpsls.winner("scissors", "lizard"), "player")

    def test_lizard_beats_spock_paper(self):
        self.assertEqual(rpsls.winner("lizard", "spock"), "player")
        self.assertEqual(rpsls.winner("lizard", "paper"), "player")

    def test_spock_beats_scissors_rock(self):
        self.assertEqual(rpsls.winner("spock", "scissors"), "player")
        self.assertEqual(rpsls.winner("spock", "rock"), "player")

    def test_loss(self):
        self.assertEqual(rpsls.winner("rock", "paper"), "computer")

    def test_verb(self):
        self.assertEqual(rpsls.verb_for("paper", "rock"), "covers")


class TestScoring(unittest.TestCase):
    def test_round_points(self):
        self.assertEqual(rpsls.round_points("easy", 1), 10)
        self.assertEqual(rpsls.round_points("easy", 3), 20)

    def test_round_points_unknown(self):
        self.assertEqual(rpsls.round_points("bad", 1), 15)

    def test_final_score(self):
        self.assertEqual(rpsls.final_score("easy", 2, 1, 2), 32)


if __name__ == "__main__":
    unittest.main()
