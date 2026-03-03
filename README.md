# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Game Purpose:**
  The game is a number guessing challenge built with Streamlit. Players try to guess a secret number within a set range and receive hints after each guess. The goal is to guess the number in as few attempts as possible, earning a higher score for quicker success.

- **Bugs Found:**
  1. The game gave misleading hints, telling players to "Go LOWER!" even for guesses below the minimum allowed value.
  2. Negative guesses were accepted, and the game did not warn about out-of-range inputs.
  3. The score could become negative after repeated incorrect guesses, which is not typical for such games.

- **Fixes Applied:**
  1. Added logic to check if a guess is within the valid range before providing hints. Out-of-range guesses now show an error message.
  2. Updated the scoring logic to prevent the score from dropping below zero.
  3. Refactored all core logic functions (range, guess parsing, hint generation, scoring) into logic_utils.py for better organization and testability.

## 📸 Demo

- [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
