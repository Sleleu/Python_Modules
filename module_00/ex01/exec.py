import sys

def main():
    if len(sys.argv) > 1:
        str = " ".join(sys.argv[1:])
        rev_str = str[::-1].swapcase()
        print(rev_str)

if __name__ == "__main__":
    main()