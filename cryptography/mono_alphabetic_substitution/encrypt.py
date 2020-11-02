mono_alphabet_dict = {
    'A':'X',
    'B':'E',
    'C':'U',
    'D':'A',
    'E':'D',
    'F':'N',
    'G':'B',
    'H':'K',
    'I':'V',
    'J':'M',
    'K':'R',
    'L':'O',
    'M':'C',
    'N':'Q',
    'O':'F',
    'P':'S',
    'Q':'Y',
    'R':'H',
    'S':'W',
    'T':'G',
    'U':'L',
    'V':'Z',
    'W':'I',
    'X':'J',
    'Y':'P',
    'Z':'T',
}

# https://lingua.com/english/reading/chicago/
original_message = "Keith recently came back from a trip to Chicago, Illinois. This midwestern metropolis is found along the shore of Lake Michigan. During his visit, Keith spent a lot of time exploring the city to visit important landmarks and monuments."
encrypted_message = ""

for char in original_message:
    # check for all letters in the alphabet. special letters like '|&%§!§' are not being encrypted
    if ord(char) == 32:
        encrypted_message += " "
    
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        encrypted_message += mono_alphabet_dict[char.upper()]

print(encrypted_message)