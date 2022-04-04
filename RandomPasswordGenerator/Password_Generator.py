import string
import random
pw_size=int(input('Enter the size of the password required\n'))

def sumfind(l):
    if len(l) <= 1:
        return l[0]
    return l[0]+sumfind(l[1:])

def roundingtheChars(s):
    small_chars=round(s*0.7)
    cap_chars=round(s*0.1)
    numbers=round(s*0.1)
    symbols=round(s*0.1)
    return [small_chars,cap_chars,numbers,symbols]

def correctPwSize(pw_to_be_generated,pw_elements):
    pw_to_be_generated = roundingtheChars(pw_size)
    pw_elements = sumfind(pw_to_be_generated)
    if (pw_elements != pw_size):
        if pw_elements < pw_size:
            small_chars = pw_to_be_generated[0] - 1
            pw_to_be_generated[0] = small_chars
        else:
            small_chars = pw_to_be_generated[0] + 1
            pw_to_be_generated[0] = small_chars
    return pw_to_be_generated

def Generate_password():
    pw_to_be_generated = roundingtheChars(pw_size)
    pw_elements = sumfind(pw_to_be_generated)
    contentList = correctPwSize(pw_to_be_generated, pw_elements)
    symbols = '!@#$%&*(),<>;:\".+_-'
    strFormat = [string.ascii_lowercase, string.digits, string.ascii_uppercase, symbols]
    s = ''
    for strings, size in zip(strFormat, contentList):
        ran = ''.join(random.choices(strings, k=size))
        s = s + ran
    return s


