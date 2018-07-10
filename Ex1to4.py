# -*- coding: utf-8 -*-
import string


def reverse_sentence(sentence):
    """Exercise 1"""
    reversed_tab_sentence = sentence.split()[::-1]
    reversed_string_sentence = " ".join(reversed_tab_sentence)
    return reversed_string_sentence


def convert_to_phone_keyboard_style(sentence):
    """Exercise 2"""
    letter_to_number_map = create_letters_number_mapping()
    sentence= sentence.lower()
    phone_style_sentence = ""
    for char in sentence:
        selected_pair_number_letters = [(key, letter_to_number_map[key]) for key in letter_to_number_map.keys() if char in key]         # select desire pair number amd letter set eg. 'abc' => 2
        letter_in_phone_style = [(index,letter) for index, letter in enumerate(selected_pair_number_letters[0][0]) if letter == char]      # get correct index in letters set eg. b = 2, s = 4
        phone_style_sentence += (letter_in_phone_style[0][0] + 1) * str(selected_pair_number_letters[0][1])                                   # update update sentence for new letter in phone keyboard style
    return phone_style_sentence


def create_letters_number_mapping():
    alphabet = string.ascii_lowercase
    letter_to_number_map = {}
    for number in xrange(2, 10):
        if number == 7 or number == 9:
            letter_to_number_map[alphabet[:4]] = number
            alphabet = alphabet[4:]
        else:
            letter_to_number_map[alphabet[:3]] = number
            alphabet = alphabet[3:]
    letter_to_number_map[" "] = "#"
    return letter_to_number_map

def count_digits(origin_number):
    """Exercise 3"""
    return len(set(str(origin_number)))



def isPalindrome(sentence):
    """Exercise 4"""
    sentence = sentence.replace(' ', '')
    clear_sentence = sentence.lower()
    for i in xrange(len(clear_sentence)/2):
        lower_index = i
        upper_index = -i - 1
        if clear_sentence[lower_index] != clear_sentence[upper_index]:
            return False
    return True




def main():
    string1 = "she sells sea shells"
    string2 = "two tea to room two two"
    string3 = "three witches watch three Swatch watches. Which witch watch which Swatch watch?"
    string4 = "Eve has a cat"
    convert_to_phone_keyboard_style(string4)
    print count_digits(12345555)
    string4 = "Anna"
    print isPalindrome(string4)
#

#
if __name__ == "__main__":
    main()
