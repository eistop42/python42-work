
def filter_words(*words):
    filtered = []
    for word in words:
        if len(word) > 5:
            filtered.append(word)
    return " ".join(filtered)

print(filter_words('кот', 'молоко', 'собака', 'стол'))