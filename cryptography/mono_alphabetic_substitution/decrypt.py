mono_alphabet_dict = {
    'X':'A',
    'E':'B',
    'U':'C',
    'A':'D',
    'D':'E',
    'N':'F',
    'B':'G',
    'K':'H',
    'V':'I',
    'M':'J',
    'R':'K',
    'O':'L',
    'C':'M',
    'Q':'N',
    'F':'O',
    'S':'P',
    'Y':'Q',
    'H':'R',
    'W':'S',
    'G':'T',
    'L':'U',
    'Z':'V',
    'I':'W',
    'J':'X',
    'P':'Y',
    'T':'Z',
}

original_message = "RDVGK HDUDQGOP UXCD EXUR NHFC X GHVS GF UKVUXBF VOOVQFVW GKVW CVAIDWGDHQ CDGHFSFOVW VW NFLQA XOFQB GKD WKFHD FN OXRD CVUKVBXQ ALHVQB KVW ZVWVG RDVGK WSDQG X OFG FN GVCD DJSOFHVQB GKD UVGP GF ZVWVG VCSFHGXQG OXQACXHRW XQA CFQLCDQGW"
decrypted_message = ""

for char in original_message:
    if ord(char) == 32:
        decrypted_message += " "
    # check for all letters in the alphabet. special letters like '|&%§!§' are not being decrypted
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        decrypted_message += mono_alphabet_dict[char.upper()]

print(decrypted_message)