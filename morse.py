import unicodedata #handling accents

def cleanText(text: str) -> str:
    """
    I could use unidecode, but it would be another dependence, since unicodedata comes on the Python standard library. By default, strings in Python are Unicode.
    Unicode has multiple ways to normalize a unicode string.
    """
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

def morseIt() -> str:
    """ I made the morse code allphabet + numbers a dictionary for optimization purposes (better than an array, I guess). """
    morse_dict = {'a':'.- ', 'b':'-... ', 'c':'-.-. ', 'd':'-.. ', 'e':'. ', 'f':'..-. ',
                  'g':'--. ', 'h':'.... ', 'i':'.. ', 'j':'.--- ', 'k':'-.- ', 'l':'.-.. ',
                  'm':'-- ', 'n':'-. ', 'o':'--- ', 'p':'.--. ', 'q':'--.- ', 'r':'.-. ',
                  's':'... ', 't':'- ', 'u':'..- ', 'v':'...- ', 'w':'.-- ', 'x':'-..- ',
                  'y':'-.-- ', 'z':'--.. ', '1':'.---- ','2':'..--- ', '3':'...-- ', '4':'....- ',
                  '5':'..... ', '6':'-.... ', '7':'--... ', '8':'---.. ', '9':'----. ', '0':'----- '
                  }

    text = input("Type the text that'll be encoded: ")
    fmt_text = cleanText(text)
    morsed_text = ''

    for letter in fmt_text:
        if(letter == ' '):
            morsed_text += ' / '
        else:
            morsed_text += morse_dict[letter]

    return morsed_text

