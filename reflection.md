# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
- The score can become negative and does not seem to reflect performance accurately. For example, after several incorrect guesses, the score dropped below zero, which is not typical for a guessing game. I expected the score to either stay at zero or decrease in a way that still makes sense for the game's rules, but instead, it kept decreasing with each wrong guess, leading to confusing results.

---

## 2. How did you use AI as a teammate?

- I used GitHub Copilot in VS Code to help refactor code, generate test cases, and explain buggy logic. Copilot Agent mode was especially useful for moving functions between files and suggesting fixes.
- A correct AI suggestion was to refactor the check_guess and update_score functions into logic_utils.py and to add range checks for guesses. I verified this by running the game and seeing that out-of-range guesses now show an error message.
- An incorrect suggestion was when Copilot initially suggested a fix for the hint logic that did not account for the valid range, so the bug persisted. I caught this by running the game and seeing the same issue, then prompted Copilot for a more specific solution.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed when both manual gameplay and automated pytest cases confirmed the correct behavior. For example, after fixing the range check, entering a negative guess produced an error instead of a misleading hint.
- I ran pytest to verify that all logic functions worked as intended, including new tests for out-of-range guesses and score not going negative. The passing tests showed the code was robust.
- Copilot helped design the new tests by suggesting edge cases and providing example assertions for the updated logic.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because it was re-generated on every rerun, rather than being stored in session_state. This made the game unwinnable.
- Streamlit reruns the script from top to bottom every time a widget changes, so variables reset unless stored in session_state. Session state allows values to persist across reruns, making interactive apps possible.
- By storing the secret number in st.session_state, I ensured it stayed the same throughout a game, making the gameplay fair and predictable.

---

## 5. Looking ahead: your developer habits

- I want to reuse the habit of marking bug locations with # FIXME comments and using automated tests to verify fixes. Prompting Copilot for targeted changes and reviewing its suggestions critically was also valuable.
- Next time, I would be more specific in my prompts to AI tools and always verify their suggestions with tests and manual checks.
- This project taught me that AI-generated code can be helpful but must be reviewed and tested carefully. Human judgment is essential for debugging and validating code quality.
