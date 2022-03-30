"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 6: Translator

   A program that translates words in english to morse or NATO phonetic
   Functions used for this program can be found in translator_functions.py
"""
from translator_functions import *


def main():
    try:
        directives = open_directives()

        # reads each line in the directives and translates the text file
        for directive in directives:
            dictionary = open_fonts(directive)
            translation = translate(dictionary, directive)
            output_file(directive, translation)
    except TypeError:
        print("File is empty")


if __name__ == "__main__":
    main()
