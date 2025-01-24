import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
print(chosen_word)
lines = "_"* len(chosen_word)
lives = 6
print(lines)
game_over = False

correct_words = []

while not game_over :
    print(f"YOU HAVE {lives} / 6 LIVES")
    guess = input("What will be your guess: ").lower()
    if guess in correct_words:
        print(f"YOU HAVE ALREADY PREDICTED {guess} NO LIVES DEDUCTED")
    display = ""
    for i in chosen_word :
        if guess == i :
            display += i
            correct_words.append(i)
        elif i in correct_words :
            display += i
        else :
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print("YOU MADE A WRONG CHOICE -1 LIFE")
        if lives == 0:
            print("*****YOU***LOST*****")
            break
    if "_" not in display :
        game_over = True
        print("*****YOU***WIN*****")
        break

    print(hangman_art.stages[lives])



