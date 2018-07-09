# -*- coding: utf-8 -*-
import string

def reverse_sentence(senance):
    reversed_tab_sentence = senance.split()[::-1]
    reversed_string_sentence = " ".join(reversed_tab_sentence)
    return reversed_string_sentence


def convert_to_phone_keyboard_style():
    alphabet  = string.ascii_lowercase
    mapa = {}
    for number in xrange(2, 10):
        if number == 7 or number == 9 :
            mapa[number] = alphabet[:4]
            alphabet = alphabet[4:]
        else:
            mapa[number] = alphabet[:3]
            alphabet = alphabet[3:]
    mapa["#"] = " "
    print mapa
    pass



def main():
    # string = "She sells sea shells"
    # print reverse_sentence(string)
    convert_to_phone_keyboard_style()


if __name__ == "__main__":
    main()
