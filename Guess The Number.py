import random
import logo_art


EASY_LEVEL_ATTEMPTS=5
HARD_LEVEL_ATTEMPTS=5


def set_difficulty(levelChoosed):
    if levelChoosed == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def check_answer(guessed_number,answer,attempts):
        if guessed_number>answer:
            print("Your guess is too high")
            return attempts-1
        elif guessed_number == answer-1:
            print("Your Guess is near to answer")
            return attempts-1
        elif guessed_number<answer:
            print("Your Guess is too low")
            return attempts-1
        elif guessed_number == answer-1:
            print("Your Guess is near to answer")
            return attempts-1
        else:
            print(f"Your guess is right ... The answer was {answer}")

def game():
    print(logo_art.logo)
    print("Let me think of number between 1 to 50")
    answer = random.randint(1,50)
    print(answer)
    level = input("Chooselevel of Difficulty...Type 'easy' or 'hard' :")
    attempts=set_difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} remaining to guess the number")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts ==0:
            print("You are out of Guess..You LOSE!!!")
            return
        elif guessed_number != answer:
            print("Guess again")

game()

