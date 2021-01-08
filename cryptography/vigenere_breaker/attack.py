import sys
import argparse
from core import v_lib
import itertools

MIN_KEY_SIZE = 3
MAX_KEY_SIZE = 7


def main():
    try:
        ########################################################################################
        ### PREPARE CIPHER TEXT
        ########################################################################################
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--message", dest="message",
                            required=True, help="the message you want to decrypt")

        args = parser.parse_args()
        parsed_message = v_lib.parse_message(args.message)


        # search for multiple fragments in cipher text
        multiples = v_lib.search_occurences(parsed_message)

        # get positions from found multiples in cipher text
        positions = []
        for m in multiples:
            for word in m[1]:
                positions.append(v_lib.search_positions(parsed_message, word))

        # calculate each text distance between each position from a text multiple
        distances = v_lib.calculate_distances(positions)


        # factorise all distances
        fact_arr = []
        for dis in distances:
            fact_arr.append(v_lib.factorise(dis))


        # clean factorise numbers
        frequent_numbers = v_lib.get_most_frequent_number(fact_arr)


        ########################################################################################
        ### INVESTIGATE POSSIBLE KEYS
        ########################################################################################

        key_map = v_lib.get_sorted_key_map(frequent_numbers)

        for key in key_map:
            if key[0] > MIN_KEY_SIZE and key[0] < MAX_KEY_SIZE:
                rotation_score = v_lib.calculate_rotation_score(v_lib.get_message_parts(parsed_message, key[0]))

                key_char_map = set()
                for rs in rotation_score:
                    possible_keys_fragments = v_lib.get_possible_key_elements(rs)
                    for char in possible_keys_fragments:
                        key_char_map.add(char)

                print("possible chars for key with length: {}".format(key[0]))
                print(key_char_map)

                print("possible keys are:")
                a = itertools.permutations(list(key_char_map), key[0])  
                y = [''.join(i) for i in a]
                for possible_key in y:
                    print(possible_key)
  

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
