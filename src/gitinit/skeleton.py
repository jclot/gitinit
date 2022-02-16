from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import git

window_screen = Tk()
tab_control = ttk.Notebook(window_screen)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)


def choose_dir():
    global dir_file
    dir_file = filedialog.askdirectory(initialdir='.')
    choosed_dir = Label(tab1, text=dir_file, font=("Arial Bold", 8, "bold"))
    choosed_dir.grid(column=0, row=0)
    choosed_dir.place(x=200, y=200, anchor="center")
    print(dir_file)

def initialize_repository():

    try:
         new_user_repo = git.Repo.init(dir_file)
         new_user_repo.git.add(all=True)
         messagebox.showinfo('Great!', 'Dir: ' + dir_file + ' is initialized')
    except NameError:
        messagebox.showerror('Dir not defined', 'Please first choose a directory before initializing it.')
    except:
        print("Somthing else wen't wrong")


def tab1_skeleton():

    choose_dir_text_title = Label(tab1, text="Choose a Directory", font=("Arial Bold", 15, "bold"))
    choose_dir_text_title.grid(column=0, row=0)
    choose_dir_text_title.place(x=200, y=80, anchor="center")

    choose_text_info = Label(tab1, text="Choose an directory then initialize the repository in the next tab")
    choose_text_info.grid(column=0, row=0)
    choose_text_info.place(x=200, y=120, anchor="center")


    choose_button_dir = Button(tab1, text="Choose a Directory", command=choose_dir)
    choose_button_dir.grid(column=1, row=0)
    choose_button_dir.place(x=200, y=160, anchor="center")

def tab2_skeleton():

    initialize_repo_title = Label(tab2, text="Initialize the repo", font=("Arial Bold", 15, "bold"))
    initialize_repo_title.grid(column=0, row=0)
    initialize_repo_title.place(x=200, y=80, anchor="center")

    initialize_repo_info = Label(tab2, text="Press the button to initialize the repo  in the assign directory")
    initialize_repo_info.grid(column=0, row=0)
    initialize_repo_info.place(x=200, y=120, anchor="center")

    initialize_repo = Button(tab2, text="Initialize Repository", command=initialize_repository)
    initialize_repo.grid(column=1, row=0)
    initialize_repo.place(x=200, y=160, anchor="center")


def tab3_skeleton():

    welcome_screen_text_title = Label(tab3, text= " Tutorial: ", font    =("Arial Bold", 15, "bold"))
    welcome_screen_text_1 = Label(tab3, text= " - Choose the directoy you wan't to initialize as a repository on github. ")
    welcome_screen_text_2 = Label(tab3, text= " - Initialize the dirctory as a repo by pressing the button (start). ")

    welcome_screen_text_title.grid(column=0, row=0)
    welcome_screen_text_1.grid(column=0, row=0)
    welcome_screen_text_2.grid(column=0, row=0)

    welcome_screen_text_title.place(x=200, y=100, anchor="center")
    welcome_screen_text_1.place(x=200, y=160, anchor="center")
    welcome_screen_text_2.place(x=200, y=130, anchor="center")




