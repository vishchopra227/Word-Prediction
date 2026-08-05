from pathlib import Path
import pickle

PICKLE_PATH = Path("data") / "words.pkl"

def load_words():
    with open(PICKLE_PATH, "rb") as file:
        return pickle.load(file)

