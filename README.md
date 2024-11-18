# Hangman Game
## Description
This project was created for a final project of an introduction to Python course. A word is randomaly chosen from a specified text file. The length of the chosen word determines the number of blank spaces.
The user can enter a guess in the text box. If the guess is wrong then more of the man is drawn. If the guess is right the letter is added to the position(s) it belongs in the word.
If the user cannot guess the word and the whole man is drawn they lose. 

## Getting Started

### Dependencies

* Uses python library tkinter and random

### Executing program
```
python Hangman.py
```
## Known Bugs
* Can only play game once then have to exit program and restart to play again
* Can not handle uppercase guesses
