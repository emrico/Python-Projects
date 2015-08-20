# NOTE ON USE:To use this class ensure that this file is inside the same directory as your project.
#             Declare an instance of this class first, and then call the play_game method on that
#             instance. Below is an example of how to instantiate this class in your program:
#                 from __init__ import HangManGame
#                 new_game = HangManGame
#                 new_game.play_game(HangManGame)


import time
import sys
from random import randint

class HangManGame:

    easy_word_list = ["apple","like","eye","love","list","blue","read","time","test","reach",
                      "tree","open","know","pop","move","silly","back","dream","lost","make"]

    moderate_word_list = ["enhance","reclaim","result","define","repeat","treaty","perceive","astronomy","medicine",
                          "sanitize","arrange","excite","enlist","moderate","accept","intent","pencil","delete",
                          "manage","release"]

    hard_word_list = ["precocious","propensity","nonsecular","verbose","engagement","redaction","admittance",
                      "entangle","remorse","esoteric","rejected","personification","entertainment","synchronization",
                      "indelible","supererogatory","facetious","incongrous","predilection","entitlement"]

    def __init__(self,difficutly):

        self.__difficulty = difficutly
    def __set_difficulty(self):

        self.__difficulty = input("Enter difficulty level (1-3): ")             # Set difficulty from user prompt
    def __set_welcome(self):

        name = input("Enter your name: ")
        print("\nHi " +  name.upper() + ", lets play some hangman!")            # User inputs name
        print("\nInstructions: When prompted try to guess a letter you \nthink may be in the magic word. If you guess correctly,"
              "                \nthe board will update with your letter. If you guess"
              "                \nincorrectly, you will lose a turn. Be careful not to"
              "                \nlose all of your turns, or you lose the game. If you"
              "                \nguess  the magic word correctly, you win!"
              "                \nThats it, good luck and have fun!")
        input("\nPress enter to start the game")
    def __select_word(self):

        rand_num = randint(0,19)                            # Generate a random number
        word = ""

        if self.__difficulty == "1":
            word = self.easy_word_list[rand_num]            # Use random number to generate random word from easy
        elif self.__difficulty == "2":
            word = self.moderate_word_list[rand_num]        # Use random number to generate random word from moderate
        elif self.__difficulty == "3":
            word = self.hard_word_list[rand_num]            # Use random number to generate random word from hard
        else:
            pass

        return word
    def __loading_ani(self):

        sys.stdout.write("loading ")
        sys.stdout.flush()
        for i in range(3):
             time.sleep(0.5)
             sys.stdout.write(".")
             sys.stdout.flush()
        print("\n"*2)
    def __check_guess(word):

        bkword = ["_"]*len(word)                                            # Initialize broken word list
        players_guess = ""                                                  # Initialize players guess
        num_of_guesses = 10                                                 # Initialize number of guesses to 10
        total_score = 0                                                     # Initialize Counter
        guess_list = []                                                     # Initialize Guess List

        for char in word:
            sys.stdout.write("_ ")                                          # Initialize the game board (Display)
            sys.stdout.flush()


        while num_of_guesses > 0:
            print("\n\nGuesses Left: " + str(num_of_guesses))               # Display number of guesses left
            print("Letters Guessed: "+" ".join(guess_list))                  # Display Guessed Letters

            players_guess = input("\nEnter your guess: ")                   # User prompted for input
            print("\n"*14)                                                  # Spacing for easy reading

            if players_guess in word and players_guess not in bkword:
                for i in range(len(word)):
                    if players_guess == word[i]:                            # If user guesses correctly
                        bkword[i] = players_guess
                        total_score +=1
                        guess_list.append(players_guess)
                    else:
                        pass
            else:
                num_of_guesses -= 1                                         # If user guesses incorrectly
                if players_guess not in guess_list:
                    guess_list.append(players_guess)

            sys.stdout.write(" ".join(bkword))                              # Display output per guess
            sys.stdout.flush()
            if total_score == len(word):
                print("\n\nCongratulations you have won!")                  # Display congrats message if you win
                print("word: "+ word)
                break
        if num_of_guesses == 0:
            print("\n\nYou Lost, better luck next time!")                   # Display lost message if you lose
            print("word: "+ word)
    def play_game(self):

        # Initialize Game
        self.__set_difficulty(self)                        # Set Difficulty Level
        self.__set_welcome(self)                           # Instructions and welcome message
        word = self.__select_word(self)                    # Requests word according to difficulty level and stores
        self.__loading_ani(self)                           # Displays loading animation
        self.__check_guess(word)







