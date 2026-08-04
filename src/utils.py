import pickle

PICKLE_PATH = r"C:\Users\vkcho\OneDrive\Desktop\nlp pickle\words.pkl"

def load_words():
    with open(PICKLE_PATH, "rb") as file:
        words = pickle.load(file)
    return words




