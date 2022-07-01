import random
import string

def hangman():
    word = random.choice(list(open('words.txt'))).upper().strip()
    hangman_stage = 0
    letters = list(word)
    alphabet = list(string.ascii_uppercase)
    used_letters = []
    guessed_letters = ["_"]*(len(word))
    while guessed_letters != letters and hangman_stage < 6:
        print("word so far: ")
        print(guessed_letters)
        print("letters guessed so far:")
        print(used_letters)
        draw_hangman(hangman_stage)
        guess = input("guess a letter or guess the word.\n").upper()
        if guess == word:
            guessed_letters = word
            print(letters)
        elif len(guess) > 1 and guess != word:
            print("incorrect guess. Try again.\n")
            hangman_stage += 1
        elif guess in alphabet and guess not in used_letters:
            used_letters.append(guess)
            for i in range(len(word)):
                if letters[i] == guess:
                    guessed_letters[i] = guess
            if guess not in guessed_letters:
                print("incorrect guess. Try again.\n")
                hangman_stage += 1
    if hangman_stage >= 6:
        print(f"You lose :(. the word was {word}.")  
    else:
        print(f"You win :) ! the word was {word}.")              

def draw_hangman(stage):
    if stage == 6:
        print("    |\ ")
        print("    | \ ")
        print("    |  O ")
        print("    | /|\ ")
        print("    | / \ ")
        print("____|____ ")
    elif stage == 5:
        print("    |\ ")
        print("    | \ ")
        print("    |  O ")
        print("    | /|\ ")
        print("    | ")
        print("____|____ ")
    elif stage == 4:
        print("    |\ ")
        print("    | \ ")
        print("    |  O ")
        print("    | ")
        print("    | ")
        print("____|____ ")
    elif stage == 3:
        print("    |\ ")
        print("    | \ ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("____|____ ")
    elif stage == 2:
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("____|____ ")
    elif stage == 1:
        print("____|____ ")
    elif stage == 0:
        pass

hangman()
