from random import randint

def guess():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

    secret_number = randint(1, 99)
    attempts = 1
    while True:
        try:
            response = input("What's your guess between 1 and 99?\n>> ")
            number = int(response)
            assert number >= 1 and number <= 99
            if number == secret_number:
                if secret_number == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                else:
                    print("Congratulations, you've got it!")
                if attempts == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print(f"You won in {attempts} attempts!")
                return
            elif number > secret_number:
                print("Too high!")
            elif number < secret_number:
                print("Too low!")
            attempts += 1
        except AssertionError:
            print("Invalid scope number.")
            attempts += 1
        except ValueError:
            if response == "exit":
                print("Goodbye!")
                return
            print("That's not a number.")
            attempts += 1


if __name__ == "__main__":
    guess()