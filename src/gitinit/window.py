
from tkinter import *


window = Tk()

def main_window():

   
    window.title("Welcome to GitInit")
    window.geometry('350x200')
    welcome_text_screen()
    window.mainloop()

def welcome_text_screen():
   
    welcome_text = Label(window, text="Press start to initialize a new repo", font=("Arial Bold", 10, "bold"))
    welcome_text.grid(column=0, row=0)
    welcome_text.place(x=175, y=50, anchor="center")
    start_button()
   
def start_button():
    btn = Button(window, text="Start")
    btn.grid(column=1, row=0)
    btn.place(x = 175, y = 100, anchor="center")

def start_button_clicked():
    # Go to the next page
