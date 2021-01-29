import unicodedata #handling accents
import time 
from playsound import playsound 

#I made the morse code alphabet + numbers a dictionary for optimization purposes (better than an array, I guess).
MORSE_DICT = {'a':'.- ', 'b':'-... ', 'c':'-.-. ', 'd':'-.. ', 'e':'. ', 'f':'..-. ',
              'g':'--. ', 'h':'.... ', 'i':'.. ', 'j':'.--- ', 'k':'-.- ', 'l':'.-.. ',
              'm':'-- ', 'n':'-. ', 'o':'--- ', 'p':'.--. ', 'q':'--.- ', 'r':'.-. ',
              's':'... ', 't':'- ', 'u':'..- ', 'v':'...- ', 'w':'.-- ', 'x':'-..- ',
              'y':'-.-- ', 'z':'--.. ', '1':'.---- ','2':'..--- ', '3':'...-- ', '4':'....- ',
              '5':'..... ', '6':'-.... ', '7':'--... ', '8':'---.. ', '9':'----. ', '0':'----- '
              }

def cleanText(text: str) -> str:
    """
    I could use unidecode, but it would be another dependence, since unicodedata comes on the Python standard library. By default, strings in Python are Unicode.
    Unicode has multiple ways to normalize a unicode string.
    """
    
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

def morseIt(text: str) -> str:
    """
    Translates from plain text to morse code.
    
    :param str text: The text to be translated
    """

    fmt_text = cleanText(text)
    morsed_text = ''

    for letter in fmt_text:
        if(letter == ' '):
            morsed_text += ' / '
        else:
            morsed_text += MORSE_DICT[letter]

    return morsed_text

def unmorseIt(text: str) -> str:
    """
    Translates from morse code to plain text with some minor alterations.
    
    :param str text: The morse code to be translated
    """

    morse_dict_inverted = {v: k for k, v in MORSE_DICT.items()}

    full_text = "" #the plain text that'll be returned
    stack = "" #helper variable that stacks the dots and hyphens (a letter can correspond to more than 1 dot or dash)

    for letter in text:
        if(letter == ' '): #when we reach a space, we got all the morse that corresponds to a single letter
            stack += letter #adds a space in the end, since the keys are like that (¯\_(ツ)_/¯)
            full_text += morse_dict_inverted[stack]
            stack = ""
        else:
            stack += letter

    if(stack != ""): #usually the last part of the code goes without spaces, so i made this
        stack += ' '
        full_text += morse_dict_inverted[stack]

    return full_text

def playMorse(code: str):
    """
    Plays the morse code. Cross-platform compatibility, thanks to TaylorSMarks! His module is at https://github.com/TaylorSMarks/playsound

    :param str code: The code to be played on the system.
    """
    for i in code:
        if(i == '.'):
            playsound('dot.wav')
        elif(i == '-'):
            playsound('dash.wav')
        else:
            time.sleep(0.3)
