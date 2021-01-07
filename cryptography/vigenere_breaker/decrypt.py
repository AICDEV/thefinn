import sys
import argparse
import string
import re

UPPER_DICT = list(string.ascii_uppercase)

def get_char_frequencies(encrypted_text):
    frequency_char_object = {}
    for char in encrypted_text:
        if ord(char) != 32:
            if char in frequency_char_object:
                frequency_char_object[char] += 1
            else:
                frequency_char_object[char] = 1

    return sorted(frequency_char_object.items(), key=lambda item: item[1], reverse=True)

def rotate(char, key):
    try:
        origin = UPPER_DICT.index(char.lower())
        target = origin + key

        return UPPER_DICT[(target % len(UPPER_DICT))]
    except:
        return char

def get_rotated_alphabet(r):
    return UPPER_DICT[r:] + UPPER_DICT[:r]

def build_vigenere_square():
    v_square = []

    counter = 0
    for _ in string.ascii_uppercase:
        v_square.append(get_rotated_alphabet(counter))
        counter += 1

    return v_square

def parse_message(message):
    message = message.replace("\n", "")
    
    message = message.upper()
    return re.sub(r'\W', '', message)


def decrypt(message, key_length, key):

    v_square = build_vigenere_square()
    dec_message = ""

    for i in range(0, len(message), key_length):
        fragment = message[i:i+key_length]
        for a in range(0, len(fragment)):
            try:
                dec_char_key_row = v_square[UPPER_DICT.index(key[a].upper())]
                dec_char_index = dec_char_key_row.index(fragment[a])
                dec_char = UPPER_DICT[dec_char_index]

                dec_message += dec_char
            except:
                dec_message += fragment[a]

    return dec_message

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--secret", dest="secret", required=True, help="your secret word to decrypt")
        parser.add_argument("-m", "--message", dest="message", required=True, help="the message you want to decrypt")
        
        args = parser.parse_args()

        print(decrypt(parse_message(args.message), len(args.secret), args.secret))

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
