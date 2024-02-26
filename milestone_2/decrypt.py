### COPIED FRON encrypt.py
# Dictionaries
number_chars='0123456789'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_chars = uppercase_chars.lower()

def get_chars_config(chars):
    CHARS_NUM=len(chars)
    ORD_FIRST=ord(chars[0])
    return [CHARS_NUM, ORD_FIRST]

def isNumber(s):
    return (s in number_chars)

# c - char
# key - key number
# ord_first - first ord(c) in dictionary
# dl - dictionary lenght
def get_next_char(c, key, ord_first, dl):
    return chr((ord(c) + key - ord_first) % dl + ord_first)

# Init constants
upper_chars_config = get_chars_config(uppercase_chars)
UPPER_CHARS_NUM = upper_chars_config[0]
UPPER_ORD_FIRST = upper_chars_config[1]
lower_chars_config = get_chars_config(lowercase_chars)
LOWER_CHARS_NUM = lower_chars_config[0]
LOWER_ORD_FIRST = lower_chars_config[1]
digits_config = get_chars_config(number_chars)
DIGITS_CHARS_NUM = digits_config[0]
DIGITS_ORD_FIRST = digits_config[1]

# s - string for encryption
# key - is a number for shifting char in dictionaries
def encrypt(s, key): 
    if key % 26 == 0:
        key+=11
    enc = ''
    
    for c in s:
        if c.isalpha():
            if c.isupper():
                enc += get_next_char(c, key, UPPER_ORD_FIRST, UPPER_CHARS_NUM)
            else:
                enc += get_next_char(c, key, LOWER_ORD_FIRST, LOWER_CHARS_NUM)
        elif isNumber(c):
            enc+= get_next_char(c, key, DIGITS_ORD_FIRST, DIGITS_CHARS_NUM)
        else:
            enc+= c
    return enc
### COPY OF CODE END

# s - string for encryption
# key - is a key number
def decrypt(s, key):
    if key % 26 == 0:
        key+=11
    return encrypt(s, -key)

key = int(input('Enter key: '))
message = input('Enter encrypted message: ')
print(decrypt(message, key))
