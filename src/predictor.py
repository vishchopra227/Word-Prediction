from src.utils import load_words
words = load_words()

def get_suggestions(prefix, top_k=10):
    prefix = prefix.lower().strip()

    if not prefix:
        return []

    suggestions = []

    for word in words:
        if word.startswith(prefix):
            suggestions.append(word)

            if len(suggestions) == top_k:
                break

    return suggestions