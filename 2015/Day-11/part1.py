import numpy as np
import re


def password_to_dec(string):
    pos, total = 0, 0
    string = list(string)
    string.reverse()
    for char in string:
        total += (ord(char) - 97) * 26 ** pos
        pos += 1
    return total

def dec_to_password(number):
    nums, ret = [], []
    while number != 0:
        result = divmod(number, 26)
        number = result[0]
        nums.append(result[1])
    nums.reverse()
    for num in nums:
        ret.append(chr(num + 97))
    return "".join(map(str, ret))

def three_letters(string):
    for i in range(0, len(string) - 2):
        if ord(string[i]) + 1 == ord(string[i + 1]) and ord(string[i]) + 2 == ord(string[i + 2]):
            return True
    return False

def fits_criteria(string: str):
    no_iol = string.find("i") == -1 and string.find("o") == -1 and string.find("l") == -1
    double = re.search("(?P<first>[a-z])(?P=first).*(?P<second>[a-z])(?P=second)", string) is not None
    return three_letters(string) and no_iol and double

password = open("./input.txt").read()
password_num = password_to_dec(password)

while not fits_criteria(password):
    password_num += 1
    password = dec_to_password(password_num)

print(password)

