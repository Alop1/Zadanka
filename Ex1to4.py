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
    phone_style_sentence = ""
    for char in sentence:
        selected_pair_number_letters = [(key, letter_to_number_map[key]) for key in letter_to_number_map.keys() if char in key]         # select desire pair number amd letter set eg. 'abc' => 2
        selected_pair_number_letters = selected_pair_number_letters[0]
        letter_in_phone_style = [(index,letter) for index, letter in enumerate(selected_pair_number_letters[0]) if letter == char]      # get correct index in letters set eg. b = 2, s = 4
        letter_in_phone_style = letter_in_phone_style[0]
        phone_style_sentence += (letter_in_phone_style[0] + 1) * str(selected_pair_number_letters[1])                                   # update update sentence for new letter in phone keyboard style
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
    without_repetition_number = set(str(origin_number))
    digits_number = len(without_repetition_number)
    return digits_number


"""4.	Palindrome. Write a program which tells if a word or a sentence is a palindrome.
I.e. “A toyota”, “11 02 2011”, “Anna”. Ignore spaces or letter case.
"""
def isPalindrome(sentence):
    """Execise 4"""
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

    # print reverse_sentence(string1)
    print string
    convert_to_phone_keyboard_style(string2)
    print count_digits(12345555)
    string4 = "Anna"
    # print isPalindrome(string4)
    # string5 = "A toyota"
    # print isPalindrome(string5)
    # string6 = "11 02 2011"
    # print isPalindrome(string6)
    print isPalindrome(string1)
#

#
if __name__ == "__main__":
    main()
