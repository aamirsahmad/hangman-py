# HANGMAN

import random

mistake = ['''
    +-----+
    |     |
          |
          |
          |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
          |
          |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
    |     |
          |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
   /|     |
          |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
   /|\\    |
          |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
   /|\\    |
   /      |
          |
          |
==============
''', '''
    +-----+
    |     |
    O     |
   /|\\    |
   / \\    |
          |
          |
==============
''']

listOfWords = ["fast", "programming", "student", "are", "lazy", "hangmen"]

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def hangman():

  guessWord = random.choice(listOfWords)
  blanks = "-" * len(guessWord)
  alreadyGuessed = set()
  wrongs = 7

  newBlanks = " ".join(blanks)
  print '''
  \t-------------\t
  \tH A N G M A N\t
          by aamir
  \t-------------\t
  '''
  print mistake[0]
  print newBlanks

  guessed = False
  while not guessed and wrongs > 0:
    guess = getGuess(alreadyGuessed)
    if guess in guessWord:
      alreadyGuessed.add(guess)
      #alreadyGuessed += guess
      blanks = "".join([char if char in alreadyGuessed else "-" for char in guessWord])
      if blanks == guessWord:
        guessed = True
        print '''
        ----------------------
            Y O U   W I N  !
        ----------------------
        '''
    else:
      wrongs -= 1
      print "Wrong Guess ... Mistakes Left: %r " % wrongs
      
      pic = 6 - wrongs
      print mistake[pic]

      if wrongs == 0:
        print '''
        ----------------------
           Y O U   L O S T  !
        ----------------------
        '''
        print "The Correct Word was >", guessWord
        
    
    print(" ".join(blanks))
    
hangman()