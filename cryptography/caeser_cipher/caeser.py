import string
import sys
import getopt

LOWER_DICT = list(string.ascii_lowercase)

def usage():
    print("for encryption please run: \n")
    print("caeser --mode=encrypt --mesage=<message> --key=<key>")
    print("\n" + "-"*10 + "\n")
    print("for decryption please run: \n")
    print("caeser --mode=decrypt --mesage=<message> --key=<key>")


def parse_params(optlist):
    mode = ""
    message = ""
    key = 0

    for opt in optlist[0]:
        if "mode" in opt[0]:
            mode = opt[1]

        elif "message" in opt[0]:
            message = opt[1]

        elif "key" in opt[0]:
            key = int(opt[1])

        else:
            pass

    return (mode, message, key)

def rotate(char, key):
    try:
        origin = LOWER_DICT.index(char.lower())
        target = origin + key

        return LOWER_DICT[(target % len(LOWER_DICT))]
    except:
        return char

def main(argv):
    try:
        optlist = getopt.getopt(argv[1:], "",["mode=","key=", "message="])
        mode, message, key = parse_params(optlist)
       
        if mode == "encrypt":
            encrypted_message = ""
            for char in message:
                encrypted_message += rotate(char, key)

            print("encrypted message: \n")
            print(encrypted_message)

        elif mode == "decrypt":
            decrypted_message = ""
            key = key - (2*key)
            for char in message:
                decrypted_message += rotate(char, key)

            print("decrypted message: \n") 
            print(decrypted_message)
        else:
            sys.exit("unrecognised mode: '{}'".format(mode))
    except Exception as e:
        print(e)
        usage()
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)

