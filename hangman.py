import random

word_list = ["python", "java", "kotlin", "javascript"]

chosen_word = random.choice(word_list)

#For testing
#print(f"Guess the word: {chosen_word}")

wl = len(chosen_word)

lives = 6

display = []
for i in range(wl):
    display.append("_")

print(display)

eog = False

while not eog:
    guess = input("Guess a letter: ").lower()

    for position in range(wl):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
            lives -= 1
            print(f"Wrong! You have {lives} lives left.")
            if lives == 0:
                print("You lost!")
                eog = True
                break

    if "_" not in display:
        print("You guessed the word!")
        eof = True