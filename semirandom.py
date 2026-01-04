from random import random

STATE_FILE = ".randstate"


def load_state():
    """Load the counter from file, or initialize if missing."""
    try:
        with open(STATE_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        with open(STATE_FILE, "w") as file:
            file.write("0")
        return 0
    except Exception:
        return 0  # fallback if file is corrupted


def save_state(counter):
    """Save the counter to file."""
    with open(STATE_FILE, "w") as f:
        f.write(str(counter))


def semi_random():
    """
    Returns True or False with these rules:
    - True on average every 4th call (≈25% chance)
    - Forced True if 6 or more calls have passed since last True
    - State persists between runs

    This function is not thread safe.
    """
    counter = load_state()

    if counter >= 6:
        result = True
    else:
        result = random() < 1 / 4

    if result:
        counter = 0
    else:
        counter += 1

    save_state(counter)
    return result
