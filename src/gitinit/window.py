
import skeleton

def main_window():

    skeleton.window_screen.title("Welcome to GitInit")
    skeleton.window_screen.geometry('400x320')
    tabs()
    skeleton.window_screen.mainloop()

def tabs():

    skeleton.tab_control.add(skeleton.tab1, text='Choose directory')
    skeleton.tab_control.add(skeleton.tab2, text='Initialize the repo')
    skeleton.tab_control.add(skeleton.tab3, text='Tutorial')

    skeleton.tab1_skeleton()
    skeleton.tab2_skeleton()
    skeleton.tab3_skeleton()

    skeleton.tab_control.pack(expand=1, fill='both')


