"""File for the Game Class"""
import math
import random


class Game:
    """Class for the game"""
    def __init__(self, hints: bool = False, auto: bool = False):
        """Initializer for the class"""
        self.hints = hints
        self.auto = auto
        self.pointers = {"low": 0, "mid": 0, "high": 0, "list_size": 0} # Dictionary
        self.max_guesses = 0
        self.guesses = 0
        self.won = False

    # Unlike some languages, Python doesn't have private methods.
    # This is called name mangling and is the closest you can get to a private method.
    def __print_hint(self, hint: str) -> None:
        """Pseudo private method to print data if hints is True"""
        if self.hints:
            print(hint)

    def __print_try_hint(self) -> None:
        """Print out what to try next"""
        self.__print_hint("Try {} since the low is now {} and high is now {}".format(
            str(self.pointers['mid']),
            str(self.pointers['low']),
            str(self.pointers['high'])
        ))

    def check_answer(self, guess: int, answer: int, total_guesses: int) -> None:
        """Lets the user know if guess was correct, high or low"""
        if guess == answer:
            print("\033[32mCongratulations!\033[00m You guessed it in {} of {} guesses!".format(
                str(total_guesses + 1),
                str(self.max_guesses)))
            self.won = True
        elif guess > answer:
            self.pointers['high'] = self.pointers['mid'] - 1
            self.pointers['mid'] = math.ceil(
                (self.pointers['low'] + self.pointers['high']) / 2)
            print("\033[31mHIGH\033[00m")
            self.__print_try_hint()
        else:
            self.pointers['low'] = self.pointers['mid'] + 1
            self.pointers['mid'] = math.floor(
                (self.pointers['low'] + self.pointers['high']) / 2)
            print("\033[36mLOW\033[00m")
            self.__print_try_hint()

    def define_list(self) -> None:
        """Prompt for list"""
        try:
            list_size = int(input("How many items are in this list: "))
            if list_size < 2:
                print("Must be whole number greater than 1")
                return

            self.pointers['list_size'] = list_size

            self.pointers['high'] = self.pointers['list_size']
            self.pointers['mid'] = int((self.pointers['low'] + self.pointers['high']) / 2)
            self.max_guesses = math.ceil(math.log(self.pointers['high'], 2))
        except ValueError:
            print("List size must be an whole number!")

    def start(self) -> None:
        """Start the game"""
        while self.pointers['list_size'] < 2:
            self.define_list()
        random_number = random.randrange(1, self.pointers['list_size'])

        print()
        print(f"Max guesses: {str(self.max_guesses)}")
        self.__print_hint(f"Mid point is {str(self.pointers['mid'])}")

        total_guesses = 0

        while total_guesses <= self.max_guesses or self.won is False:
            try:
                print()
                if self.auto:
                    print("Guessing mid point between {} and {}: {}".format(
                        self.pointers['low'],
                        self.pointers['high'],
                        self.pointers['mid']
                    ))
                    my_guess = self.pointers['mid']
                else:
                    my_guess = int(input(
                        f"Guess the number between 1 and {str(self.pointers['list_size'])}: "))

                self.check_answer(my_guess, random_number, total_guesses)

                if self.won:
                    break

                total_guesses = total_guesses + 1
                if (self.max_guesses - total_guesses) > 0:
                    print(f"You have {str(self.max_guesses - total_guesses)} guesses left.")
                else:
                    print(f"You failed to guess the number! {str(random_number)}")
                    break
            except ValueError:
                print("Guess must be an integer!")
