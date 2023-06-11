import sys

def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif len(sys.argv) > 1:
        try:
            value = int(sys.argv[1])
            if (value == 0):
                print("I'm Zero.")
            elif (value % 2 == 0):
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except:
            print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()