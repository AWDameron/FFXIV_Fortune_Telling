import tkinter as tk
from tkinter import *
from Fortune_Teller_Method import fortune_telling_random  # Importing the updated function

def dialog_box(file_path):
    master = Tk()
    master.title("Fortune Teller")
    
    # User name entry
    label_name = Label(master, text='Please Enter Your Name: ')
    label_name.grid(row=0, column=0)
    user_name = Entry(master)
    user_name.grid(row=0, column=1)

    # Card choice entry 
    label_choice = Label(master, text="Please pick a card between 1 and 6")
    label_choice.grid(row=1, column=0)
    user_choice = Entry(master)
    user_choice.grid(row=1, column=1)

    # Result label 
    label_result = Label(master, text="")
    label_result.grid(row=3, column=0, columnspan=3)

    def submit_button():
        name = user_name.get()
        choice = user_choice.get()

        if not name:
            label_result.config(text="Please enter your name.")
            return
        
        try:
            choice_int = int(choice)
            if choice_int < 1 or choice_int > 6:
                label_result.config(text="Please choose a card number between 1 and 6.")
                return
        except ValueError:
            label_result.config(text="Please enter a valid card number (1-6).")
            return 
        
        # Call fortune_telling_random and get the result
        result = fortune_telling_random(name, choice, file_path)
        label_result.config(text=result)  # Display the result in label_result

    sub_button = Button(master, text='Submit', command=submit_button)
    sub_button.grid(row=5, column=0)
    
    exit_button = Button(master, text='Exit', command=master.quit)
    exit_button.grid(row=5, column=2)

    master.mainloop()
