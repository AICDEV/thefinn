import sys
import string

LOWER_DICT = list(string.ascii_lowercase)

def rotate(char, key):
    try:
        origin = LOWER_DICT.index(char.lower())
        target = origin + key

        return LOWER_DICT[(target % len(LOWER_DICT))]
    except:
        return char


def main(args):
    secret_message = sys.argv[1]

    print("attack: '{}'".format(secret_message))

    for i in range(0,26):
        decrypted_message = ""
        print("\n rotate with key: {} \n".format(i))
        for char in secret_message:
            decrypted_message += rotate(char, i -(i*2))
        print(decrypted_message)

if __name__ == "__main__":
    main(sys.argv)
