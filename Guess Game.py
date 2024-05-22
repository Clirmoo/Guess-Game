from tkinter import *
from tkinter import messagebox
import random


def check_answer():
    global attempts
    global text


    attempts -= 1


    guess = int(entry_window.get())


    if answer == guess:
        text.set("You win!")
        btn_check.place_forget()
    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.place_forget()
    elif guess < answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Higher!")
    elif guess > answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Lower!")


def play_again():
    global answer
    global attempts


    answer = random.randint(1, 10)
    attempts = 3
    text.set("You have only 3 attempts remaining")
    btn_check.place(x=490, y=180)


def login():
    username = entry1.get()
    password = entry2.get()


    if username == '' and password == '':
        messagebox.showerror('login', 'Blanks are not allowed')
    elif username == 'player' and password == 'escananmaganda':
        messagebox.showinfo('login', 'Login Successful')


        global answer
        global attempts
        global entry_window
        global text
        global btn_check


        answer = random.randint(1, 10)
        attempts = 3


        top = Toplevel()
        top.title("Guess the number Game")
        top.geometry("1000x500")


        label4 = Label(top, text='Welcome to the game!', font=('Arial', 20))
        label4.place(x=380, y=20)


        label5 = Label(top, text="Guess the number between 1 to 10", font=('Arial', 20))
        label5.place(x=300, y=80)


        entry_window = Entry(top, width=40, borderwidth=4)
        entry_window.place(x=390, y=150)


        btn_check = Button(top, text='Check', command=check_answer)
        btn_check.place(x=490, y=190)


        btn_quit = Button(top, text='Quit', command=top.destroy)
        btn_quit.place(x=495, y=220)


        btn_play_again = Button(top, text='Play Again', command=play_again)
        btn_play_again.place(x=480, y=300)


        text = StringVar()
        text.set("You have only 3 attempts remaining")


        guess_attempts = Label(top, textvariable=text)
        guess_attempts.place(x=415, y=260)


    else:
        messagebox.showerror('login', 'Incorrect Username and Password')


def show_password():
    if entry2.cget('show') == '*':
        entry2.config(show='')
    else:
        entry2.config(show='*')


root = Tk()
root.title("Guess the number Game")
root.geometry("500x500")
root.configure(bg='cyan4')


label1 = Label(root, text='Login Page', bg='cyan4', fg='cyan', font=('Arial', 20))
label1.place(x=185, y=50)


label2 = Label(root, text='Username :', font=('Arial', 20), bg='cyan4', fg='white')
label2.place(x=70, y=100)


label3 = Label(root, text='Password  :', font=('Arial', 20), bg='cyan4', fg='white')
label3.place(x=70, y=150)


entry1 = Entry(root, font=('Arial', 15))
entry1.place(x=225, y=110)


entry2 = Entry(root, font=('Arial', 15), show='*')
entry2.place(x=225, y=155)


button = Button(root, text='Login', bg='cyan3', font=('Arial', 15), bd=5, command=login)
button.place(x=290, y=220)


check_button = Checkbutton(root, text="show password", command=show_password)
check_button.place(x=225, y=190)


root.mainloop()
