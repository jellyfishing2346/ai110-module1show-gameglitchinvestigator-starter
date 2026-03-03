import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 40 and guess is 49 (within 1-50), outcome should be "Too High"
    outcome, _ = check_guess(49, 40)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_out_of_range_low():
    # Guess below the minimum should return "Out of Range"
    outcome, msg = check_guess(-5, 50)
    assert outcome == "Out of Range"
    assert "between" in msg

def test_guess_out_of_range_high():
    # Guess above the maximum should return "Out of Range"
    outcome, msg = check_guess(101, 50)
    assert outcome == "Out of Range"
    assert "between" in msg

def test_score_never_negative():
    # Score should not go below zero
    score = 0
    for _ in range(10):
        score = update_score(score, "Too Low", 1)
    assert score == 0
