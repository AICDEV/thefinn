import sys
import argparse
import string
import re
import math
import frequency

UPPER_DICT = list(string.ascii_uppercase)

"""
SEARCH FOR MULTIPLE OCCURRENCES IN CIPHER TEXT
"""
def analyse_text(message, length):
    hits = {}
    for i in range(0, len(message)):
        if (i + length) < len(message):
            fragment = message[i:i+length]
            if fragment not in hits:
                hits[fragment] = 1
            else:
                hits[fragment] = hits[fragment] + 1
    return strip_single_hits(hits)


def strip_single_hits(hits):
    for hit in list(hits):
        if hits[hit] == 1:
            hits.pop(hit)
    return hits


def search_occurences(message):
    counter = 8
    occurrences = []
    while counter >= 3:
        occurrences.append((counter, analyse_text(message, counter)))
        counter -= 1
    return occurrences


"""
SEARCH FOR POSITIONS OF MULTIPLE OCCURRENCES IN CIPHER TEXT
"""
def search_positions(message, word):
    positions = []
    print(word)
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
CLEAN MESSAGE
"""
def parse_message(message):
    message = message.replace("\n", "")
    message = message.upper()
    return re.sub(r'\W', '', message)

"""
BRUTEFORCE
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

def bruteforce(parts):
    print("bruteforcing")
    for part in parts:
        key = part[0]
        print("rotate for key:{}".format(key))
        for text in part[1]:
            print("*"*40)
            for a in range(1,27):
                score = frequency.get_score(frequency.get_letter_map(rotate(text,a)))
                print(score)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--message", dest="message",
                            required=True, help="the message you want to decrypt")

        args = parser.parse_args()
        parsed_message = parse_message(args.message)

        print("-"*40)
        print("analyse text for triagrams etc")
        multiples = search_occurences(parsed_message)


        print("extracting positions")
        positions = []
        for m in multiples:
            for word in m[1]:
                positions.append(search_positions(parsed_message, word))

        distances = calculate_distances(positions)
        fact_arr = []
        for dis in distances:
            fact_arr.append(factorise(dis))


        frequent_numbers = get_most_frequent_number(fact_arr)
        key_map = get_sorted_key_map(frequent_numbers)


        print("found the following possible key lengths")
        part_arr = []
        c = 1
        for key in key_map:
            # print("rank: {} -> key with length: {}".format(c, key[0]))
            # print("extract message parts")
            # part_arr.append((key[0],get_message_parts(parsed_message, key[0])))
            c += 1
        
        print("rank: {} -> key with length: {}".format(4, 4))
        print("extract message parts")
        part_arr.append((4,get_message_parts(parsed_message, 4)))

        bruteforce(part_arr)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
