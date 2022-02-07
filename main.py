import random
import hangman_art
import hangman_words


word = random.choice(hangman_words.word_list)
word_length = len(word)

x = int(word_length)
lives = 6
blank = [None] * x

for i in range(x):
  blank[i] = "_"

flag = True

print(hangman_art.logo)

while flag is True:
  y = input(f"Guess a letter for the {x} character long word? \n").lower()
  

  count = 0
  for i in range(x):
    if y == word[i]:
       blank[i] = y
       count += 1
    

  if count == 0:
    lives -= 1



  print(f"{hangman_art.stages[lives]}")
  print(blank)
  if lives == 0:
    print("You lose")
    flag = False

  if "_" not in blank:
    print("You win.")
    flag = False


