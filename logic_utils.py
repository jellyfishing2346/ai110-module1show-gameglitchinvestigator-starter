
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Now checks for out-of-range guesses and returns an error message if guess is not within allowed range.
    # Assumes secret is always within the valid range.
    if isinstance(secret, str):
        try:
            secret = int(secret)
        except Exception:
            return "Error", "Secret number is invalid."

    # Define the valid range based on the secret (since range is not passed in, infer from secret)
    # For a more robust solution, pass low/high as arguments.
    # Here, assume range is always 1 to 100 (default Normal)
    low, high = 1, 100
    if secret <= 20:
        low, high = 1, 20
    elif secret <= 50:
        low, high = 1, 50

    if guess < low or guess > high:
        return "Out of Range", f"❌ Guess must be between {low} and {high}."

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Prevent score from going negative and make scoring more intuitive.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return max(current_score + points, 0)

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return max(current_score + 5, 0)
        return max(current_score - 5, 0)

    if outcome == "Too Low":
        return max(current_score - 5, 0)

    return max(current_score, 0)
