import sys

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def main():
    try:
        assert len(sys.argv) > 1, "ERROR"
    except AssertionError as Error:
        print(Error)
        return
    morse_code = ''
    for arg in sys.argv[1:]:
            for letter in arg:
                if letter.upper() not in morse_dict:
                    print("ERROR")
                    return
                morse_code += morse_dict[letter.upper()] + ' '
            morse_code += '/ '
    print(morse_code.rstrip('/ '))
    

if __name__ == "__main__":
    main()