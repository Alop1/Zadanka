# -*- coding: utf-8 -*-

def reversing(senance):
    reversed_tab_sentence = senance.split()[::-1]
    reversed_string_sentence = " ".join(reversed_tab_sentence)
    return reversed_string_sentence


def main():
    string = "She sells sea shells"
    print reversing(string)


if __name__ == "__main__":
    main()
