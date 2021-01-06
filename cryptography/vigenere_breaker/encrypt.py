import sys
import argparse
import string
import re

UPPER_DICT = list(string.ascii_uppercase)

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


def encrypt(message, key_length, key):

    v_square = build_vigenere_square()
    enc_message = ""

    for i in range(0, len(message), key_length):
        fragment = message[i:i+key_length]
        for a in range(0, len(fragment)):
            try:
                enc_char = v_square[UPPER_DICT.index(key[a].upper())][UPPER_DICT.index(fragment[a])]
                enc_message += enc_char
            except:
                enc_message += fragment[a]

    return enc_message

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--secret", dest="secret", required=True, help="your secret word to encrypt")
        parser.add_argument("-m", "--message", dest="message", required=True, help="the message you want to encrypt")
        
        args = parser.parse_args()

        print(encrypt(parse_message(args.message), len(args.secret), args.secret))

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
