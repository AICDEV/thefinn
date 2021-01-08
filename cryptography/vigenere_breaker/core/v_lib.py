import re
import math
import string
from core import frequency

UPPER_DICT = list(string.ascii_uppercase)

"""
CLEAN MESSAGE
"""
def parse_message(message):
    message = message.replace("\n", "")
    message = message.upper()
    return re.sub(r'\W', '', message)

"""
SEARCH FOR MULTIPLE OCCURRENCES IN CIPHER TEXT
"""
def _analyse_text(message, length):
    hits = {}
    for i in range(0, len(message)):
        if (i + length) < len(message):
            fragment = message[i:i+length]
            if fragment not in hits:
                hits[fragment] = 1
            else:
                hits[fragment] = hits[fragment] + 1
    return _strip_single_hits(hits)


def _strip_single_hits(hits):
    for hit in list(hits):
        if hits[hit] == 1:
            hits.pop(hit)
    return hits


def search_occurences(message):
    counter = 3
    occurrences = []
    while counter >= 2:
        occurrences.append((counter, _analyse_text(message, counter)))
        counter -= 1
    return occurrences

"""
SEARCH FOR POSITIONS OF MULTIPLE OCCURRENCES IN CIPHER TEXT
"""
def search_positions(message, word):
    positions = []
    for i in range(0, len(message)):
        if (i + len(word)) < len(message):
            if message[i:i+len(word)] == word:
                positions.append((i+1, (i+len(word))))
    return positions

""" 
CALCULATE DISTANCE BETWEEN OCCURRENCES
"""
def calculate_distances(positions):
    distance_set = set()
    for pos in positions:
        for i in range(0, len(pos)):
            if i + 1 < len(pos):
                distance_set.add((pos[i+1][0])-pos[i][0])
                
    return distance_set

"""
GET PRIME FACTORS
"""
def factorise(n):
    fac = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            if n // i != i:
                fac.add(n // i)
    return fac

"""
GET MOST FREQUENT NUMBER
"""
def get_most_frequent_number(distances):
    dict_n = {}
    for dis in distances:
        for d in dis:
            if d not in dict_n:
                dict_n[d] = 1
            else:
                dict_n[d] = dict_n[d] + 1

    return dict_n

"""
GET KEY MAP
"""
def get_sorted_key_map(frequent_numbers):
    return sorted(frequent_numbers.items(), key=lambda item: item[1], reverse=True)

"""
GET MESSAGE PARTS
"""
def get_message_parts(message, length):
    parts = []
    for a in range(0, length):
        counter = a
        part = ""
        while counter < len(message):
            part += message[counter]
            counter += length
        parts.append(part)
    return parts

"""
GET MAX
"""
def get_max(t):
    max_t = 0
    for a in t:
        if a[0] > max_t:
            max_t = a[0]
    return max_t


"""
ROTATE
"""
def rotate(text, key):
    try:
        rotated = ""
        for c in text:
            origin = UPPER_DICT.index(c.upper())
            target = origin - key

            rotated += UPPER_DICT[(target % len(UPPER_DICT))]
        return rotated
    except:
        return text

"""
CALCULATE ROTATION SCORE
"""
def calculate_rotation_score(parts):
    rotation_scores = []

    for part in parts:
        score_metric = []

        for a in range(0,26):
            rotated_text = rotate(part,a)
            letter_map = frequency.get_letter_map(rotated_text)
            score = frequency.get_score(letter_map)
            score_metric.append((score, a))

            rotation_scores.append(score_metric)
    return rotation_scores


"""
EXTRACT POSSIBLE KEY ELEMENTS
"""
def get_possible_key_elements(score_metric):
    max_score = get_max(score_metric)
    parts = []
    for s in score_metric:
        if max_score == s[0]:
            parts.append(UPPER_DICT[s[1]])
    return parts
