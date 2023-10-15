# Hangman by Oliver Bennett and Rhys Jordan


# Importing (Oliver)
import random
from tkinter import *

x = Tk()

# create Canvas (Oliver)
canvas = Canvas(x, width=300, height=300)
canvas.grid(row=0, column=0)

# Create Hangman noose (Oliver)
canvas.create_line(40, 300, 140, 300)
canvas.create_line(90, 100, 90, 300)
canvas.create_line(90, 100, 200, 100)
canvas.create_line(200, 100, 200, 140)

# Read file of words (Rhys)
words = []
file = open('Wordlist.txt')
for line in file:
    line = line.rstrip("\n")
    words.append(line)
file.close()


# Randomize word (Oliver)
word = random.choice(words)
a = len(word)

# Put letter from the word into a list (Rhys)
wordLetter = []
for lett in word:
    wordLetter.append(lett)

# create blanks based on random word(Rhys)
c = Canvas(x, width=450, height=50)
c.grid(row=0, column=1)


x1 = 0
x2 = 30
for i in range(a):
    c.create_line(x1, 25, x2, 25)
    x1 += 40
    x2 += 40

# Put letter in the correct blanks(Rhys)


def letter(g):
    numletter = wordLetter.count(g)
    for w in range(numletter):
        index = wordLetter.index(g)
        wordLetter.remove(wordLetter[index])
        wordLetter.insert(index, ' ')
        lx = 15 + (40 * index)
        c.create_text(lx, 15, text=g, fill='black', font=('Times', 20))
    # If all letter are guessed you win (Oliver)
    ifwin = wordLetter.count(' ')
    if ifwin == a:
        Label(x, text='YOU WIN', font=('calibri', 50)).grid(row=1, column=1)


# Create hanging man as guessed wrong(Rhys)
tries = 0


def nLetter():
    global tries
    if tries == 0:
        canvas.create_oval(180, 140, 220, 180)
        tries += 1
    elif tries == 1:
        canvas.create_line(200, 180, 200, 230)
        tries += 1
    elif tries == 2:
        canvas.create_line(200, 205, 175, 180)
        tries += 1
    elif tries == 3:
        canvas.create_line(200, 205, 225, 180)
        tries += 1
    elif tries == 4:
        canvas.create_line(200, 230, 175, 270)
        tries += 1
    elif tries == 5:
        canvas.create_line(200, 230, 225, 270)
        # Print you lose/dead man if run out of guesses(Oliver)
        Label(x, text='YOU LOSE', font=('calibri', 50)).grid(row=1, column=1)
        canvas.create_line(190, 150, 195, 160)
        canvas.create_line(205, 150, 210, 160)
        canvas.create_line(195, 150, 190, 160)
        canvas.create_line(210, 150, 205, 160)
        canvas.create_line(190, 170, 215, 170)
        # Print what word it was(Rhys)
        w = 15
        for letters in word:
            c.create_text(w, 15, text=letters, fill='black', font=('Times', 20))
            w += 40


# User guesses input (Oliver)
label1 = Label(x, text='Enter Letter:', font=('times', 20)).grid(row=1, column=1)
entry1 = Entry(x, width=10)
entry1.grid(row=1, column=2)
canvas2 = Canvas(x, width=100, height=30)
canvas2.grid(row=0, column=2)


# Calling guess(Rhys)
n = 10


def guess1():
    global canvas2, n
    g = str(entry1.get())
    if g in word:
        letter(g)
    elif g not in word:
        nLetter()
        # Print letter guessed not in word(Oliver)
        canvas2.create_text(n, 11, text=g, font=('calibri', 20), fill='black')
        n = n + 15
    entry1.delete(0, END)


# Try Button(Oliver)
b1 = Button(x, text='Try', font=('Times', 20), command=guess1).grid(row=1, column=3)

x.mainloop()
