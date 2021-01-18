import random
import os

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    "gollum",
    "aragorn",
    "gandalf",
    "frodo",
    "legolas",
    "sauron",
    "arwen",
    "galadriel",
    "samsagaz",
    "eowyn",
    "saruman",
    "elrond",
    "boromir",
    "pippin",
    "bombadil",
    "meriadoc",
    "glorfindel",
    "denethor",
    "barbol",
]


def random_word():
    idx = random.randint(0, len(WORDS) )
    return WORDS[idx]


def display_board(hidden_word, tries):
    os.system('cls')
    print(IMAGES[tries])
    print ("")
    print (hidden_word)
    print ("")
    print ("")
    print ("--- * --- * --- * --- * --- * --- * --- ")


def run():
    
    word = random_word()
    hidden_word = ["-"] * len(word)
    tries = 0

    while True:    
        display_board(hidden_word, tries)
        print ()
        print ("B I E N V E N I D O S   A   A H O R C A D O S   D E L   S E Ñ O R   D E   L O S   A N I L L O S")
        print ()
        print()
        current_letter = str(input("Escoge una letra: "))

        letter_indexes = []
        for idx in range (len(word)):
            if word [idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries +=1

            if tries == 7:
                display_board(hidden_word, tries-1)
                print ("")
                print ("HAS PERDIDO!!! LA PALABRA CORRECTA ERA: {}".format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index("-")
        except ValueError:
            print("")
            print("FELICIDADES!!! HAS GANADO")
            break

if __name__ == "__main__":
    
    run ()