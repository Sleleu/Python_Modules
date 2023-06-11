import string
import sys

def text_analyzer(text = None): 
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if (text is None):
        text = input('What is the text to analyze?\n >> ')
    try:
        assert isinstance(text, str), "AssertionError: argument is not a string"
    except AssertionError as Error:
        print(Error)
        return

    upper, lower, punctuation, space = 0, 0, 0, 0

    for letter in text:
        if letter in string.ascii_uppercase:
           upper += 1
        elif letter in string.ascii_lowercase:
             lower += 1
        elif letter in string.punctuation:
            punctuation += 1
        elif letter in string.whitespace:
            space += 1

    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} space(s)")

def main():
    try:
        assert len(sys.argv) == 2, "Error: 1 argument required"
    except AssertionError as Error:
        print(Error)
        return
    text_analyzer(sys.argv[1])

if __name__ == "__main__":
    main()