import random
from tkinter import *

random_number = random.randint(0, 999)

root = Tk()
root.geometry('500x500')
root.title("Number guessing game")
label_0 = Label(root, text="Number guessing game", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Enter number", width=20, font=("bold", 10))
label_1.place(x=80, y=150)
entry_1 = Entry(root)
entry_1.place(x=240, y=150)


def printAttempts(_attempts):
    attempt_string = "Attempt left: " + str(_attempts)
    label_attempt = Label(root,
                          text=attempt_string,
                          width=20,
                          font=("bold", 20))
    label_attempt.place(x=90, y=100)


def printSuccess():
    success_message = Label(root,
                            text="Horray you guessed it right",
                            width=20,
                            font=("bold", 10))
    success_message.place(x=80, y=200)


def printFailure():
    failure_message = Label(root,
                            text="You gussed wrong number :(",
                            width=20,
                            font=("bold", 10))
    failure_message.place(x=80, y=200)


printAttempts(3)


def onSubmit():
    attempts = 3

    guessed_number = entry_1.get()
    guessed_number = int(guessed_number)

    while attempts != 0:
        if (guessed_number == random_number):
            printSuccess()
        else:
            printFailure()
            attempts -= 1
            printAttempts(attempts)
            if (attempts == 0):
                print("No attempts left, try again later")


Button(root, text='Submit', width=20, bg='brown', fg='white',
       command=onSubmit).place(x=180, y=380)

root.mainloop()
