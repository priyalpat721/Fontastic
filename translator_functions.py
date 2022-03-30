"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 6: Translator functions

   A file of helper functions for translator
"""
import os

DIRECTIVE = 'directives.txt'
FONTS = 'fonts.txt'


def open_directives() -> list:
    """
    Opens a file called directives and saves the information from the file
    to a list. Exception handling is used to make sure the file is valid.
    Parameters:

    Return:
        directives_list (list): [english, other language/font, text, output]
    """
    try:
        if os.path.getsize(DIRECTIVE):
            # format of the list: [english, other language/font, text, output]
            directives_list = []

            # opens directives file and reads text into a list
            with open(DIRECTIVE, 'r') as directives:
                for line in directives:
                    directives_list.append(line.strip().split())
            return directives_list
    
    except FileNotFoundError:
        print("Sorry, directives.txt does not exist.")
        quit()

    except IOError:
        print("Sorry, directives.txt is locked")
        quit()


def make_dictionary(directive: list, m_data: list, font: list, font_dict: dict) -> dict:
    """
    Determines the current language/font and the language/font that
    needs to be translated. Once that is established, a dictionary is
    created where the keys are from the current language and the values are
    from the translated language/font
    Parameters:
        directive (list)
        m_data (list): list of the header from the font file
        font (list): list of each line in the font file
        font_dict (dictionary): each iteration populates the dictionary
    Return:
        font_dict (dictionary)
    """
    from_language = -1
    to_language = -1

    # determines the correct columns in the font file
    for i in range(len(m_data)):
        # determines the dictionary key
        if directive[0].upper() == m_data[i]:
            from_language = i - 1
        # determines the dictionary values
        if directive[1].upper() == m_data[i]:
            to_language = i - 1

    if from_language != -1 and to_language != -1:
        # the column numbers are used to populate the dictionary
        font_dict[font[from_language]] = font[to_language]

    return font_dict


def open_fonts(directive: list) -> dict:
    """
    Opens the font fonts using exception handling to determine if the
    fonts is valid. The metadata is determined and passed as a parameter
    in the function: make_dictionary() to create a dictionary
    Parameters:
        directive (list): format -> [english, other language/font, text, output]
    Return:
        dictionary (dictionary): complete dictionary needed for translation
    """
    font_dict = {}
    m_data = []

    try:
        #  opens the fonts fonts.txt
        with open(FONTS) as fonts:
            # creates a list that stores information on metadata from font fonts
            for line in fonts:
                font = line.strip().split()
                if font[0] == 'METADATA':
                    m_data = font

                else:
                    # m_data  is necessary for the dictionary's keys and values
                    dictionary = make_dictionary(directive, m_data, font, font_dict)

        return dictionary

    except FileNotFoundError:
        print("Sorry, fonts.txt does not exist.")

    except AttributeError:
        print("Dictionary was not made.")

    except UnboundLocalError:
        print("Fonts.txt is empty")


def translate(dictionary: dict, directive: list) -> str:
    """
    Takes the sentence/phrase that needs to be translated and translates
    each letter into its respective counterpart in the specified language.
    Parameters:
        dictionary (dict): dictionary with values stored as translated language
        directive (list): format -> [english, other language/font, text, output]
    Return:
        translation (str): the translated sentence/phrase
    """
    try:
        # the text that needs to be translated
        text = open_text(directive)
        translation = ""

        for i in range(len(text)):
            # each character is translated and stored in a string
            if text[i] in dictionary.keys():
                translation += dictionary[text[i]] + " "

            elif text[i] == " ":
                # each space is separated by a forward slash to fit the format
                translation += "/ "

            elif text[i] not in dictionary.keys():
                # passes characters that are not in the dictionary as is
                translation += text[i]

            else:
                # needed for multiple sentences in the text
                translation += "\n"

        return translation

    except AttributeError:
        quit()

    except TypeError:
        quit()


def open_text(directive: list) -> list:
    """
    Opens the text file using exception handling to determine if the
    file is valid. The text is read into a list by character to allow for
    easier translation.
    Parameters:
        directive (list): format -> [english, other language/font, text, output]
    Return:
        text (list): a list of characters that need to be translated
    """
    try:
        text = []
        # directive[2] is the file that has the text that will be translated
        with open(directive[2], 'r') as file:
            # each individual character is accessed through the nested for loop
            for line in file:
                for word in line:
                    # the characters are stored in uppercase to match the font
                    text.append(word.upper())
        return text
    
    except FileNotFoundError:
        print("Sorry, the test font file does not exist.")
        quit()

    except IOError:
        print("Sorry, the test font file is locked")
        quit()


def output_file(directive: list, translation: str):
    """
    The translated sentence/phrase is stored in a new .txt file
    Parameters:
        directive (list): format -> [english, other language/font, text, output]
        translation (str): the translated sentence/phrase
    Return:
        None
    """

    # directive[3] is the output file name from the directives file
    with open(directive[3], 'w') as output:
        # the translated font/language is written into the file, then the text
        output.write(directive[1] + ":\n\n")
        for word in translation:
            output.write(word)


