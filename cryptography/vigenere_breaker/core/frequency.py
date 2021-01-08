import re
import math

TOP_ENGLISH_LETTERS = ["E","T","A","O","I","N"]
LEAST_ENGLISH_LETTERS = ["V","K","J","X","Q","Z"]

def clean_text(text):
    return re.sub(r'\W', '', text)

def get_letter_map(text):
    letters = {}
    text = clean_text(text)
    for c in text:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] = letters[c] + 1
    return sort_dict(letters)

def sort_dict(target):
    return sorted(target.items(), key=lambda item: item[1], reverse=True)

def get_score(letter_dict):
    head = letter_dict[0:5]

    score = 0

    for el in head:
        for ch in TOP_ENGLISH_LETTERS:
            if str(el[0]).upper() == ch:
                score += 1
    return score
