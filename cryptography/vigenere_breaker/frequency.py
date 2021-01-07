import re
import math

test = "The house introduced in the introduction is owned by Arthur Dent, who is a totally normal human being. That is, just like the rest of us, his house is in the way of a planned road that the local government wants to build. In fact, Arthur starts off the day with a hang over, just like the rest of u…wait, what?, because he was down at the pub last night, drinking and complaining about how the local gov ernment wants to bulldoze his house.Which explains why there are bulldozers outside his house right now. So, Arthur goes out and lies down in front of a bulldozer. Pretty much your average Thursday. The man in charge of the bulldozers is Mr. L. Prosser, who is a dista nt descendant of Genghis Khan. Like Genghis Khan, Prosser has a bit of a belly and likes fur hats. Unlike Genghis Khan, Prosser is ner vous and not so good at conquering"

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
    return letters

def calculate_frequency(letters):
    frequency_map = {}
    for letter in letters:
        frequency_map[letter] = sigmoid(letters[letter] / 26)
    return sort_dict(frequency_map)

def sort_dict(target):
    return sorted(target.items(), key=lambda item: item[1], reverse=True)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def get_frequency(text):
    return calculate_frequency(get_letter_map(text))
