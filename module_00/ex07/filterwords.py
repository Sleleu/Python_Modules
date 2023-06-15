import sys
import string

def main():
    try:
        assert len(sys.argv) == 3, "ERROR"
        value = int(sys.argv[2])
    except AssertionError as Error:
        print(Error)
        return
    except ValueError:
        print('ERROR')
        return
    text = sys.argv[1].split(" ")
    checked_text = []
    for word in text:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if len(word) > value:
            checked_text.append(word)
    print(checked_text)

if __name__ == "__main__":
    main()