import tkinter as tk
from tkinter import ttk
from time import time

from random import choice

GAME_STARTED = False
GAME_DATA = []
CORRECT_WORDS = []
PLAYER_WORDS = []
TIMING = 60
COUNTING = 0

with open("day_086-PPP-typing_speed_test/words.txt", "r") as f:
    data = [line.strip() for line in f]

    while len(GAME_DATA) < 100:
        GAME_DATA.append(choice(data).lower())


def count_down():
    global COUNTING
    wpm = len(PLAYER_WORDS)
    cpm = len("".join(PLAYER_WORDS))
    COUNTING += 1
    subtitle.configure(text=f"{TIMING - COUNTING} seconds remaining! {int(wpm/TIMING*60)} words/min, {int(cpm/TIMING*60)} chars/min")
    
    if TIMING > COUNTING:
        window.after(1000, count_down)
    

def handle_click(event):
    player_input.delete(0, tk.END)
    GAME_STARTED = True
    window.after(1000, count_down)


def add_wording(event):
    word = player_input.get()
    # verify if entry is empty
    if word.strip() == "":
        print("no word")
        return
    # add entry value in player words
    PLAYER_WORDS.append(word)
    player_input.delete(0, tk.END)

    # add first word of game data in  correct words 
    CORRECT_WORDS.append(GAME_DATA.pop(0))
    modify_text()
    

def going_back_in_list(event):
    global GAME_DATA
    entry = player_input.get()
    # verify if entry or correct words list is empty
    if len(entry) != 0 or len(CORRECT_WORDS) == 0:
        return

    # suppressing last word in correct words list and add back
    # to game data
    last_word = CORRECT_WORDS.pop(-1)
    GAME_DATA = [last_word] + GAME_DATA
    modify_text()
    # suppressing last word in player words list and add back
    # to entry
    last_player_word = PLAYER_WORDS.pop(-1)
    player_input.insert(0, last_player_word)
    
    

def modify_text():
    word_list.set(" ".join(GAME_DATA))
    word_list_box.configure(state="normal")
    word_list_box.delete(('1.0'), tk.END)
    word_list_box.insert(tk.END, word_list.get())
    change_part_of_text()
    word_list_box.configure(state="disabled")

def change_part_of_text():
    start_index = "1.0"
    end_index = f"1.{len(GAME_DATA[0])}" 
    word_list_box.tag_add("start", start_index, end_index)
    word_list_box.tag_config("start", font=("Arial", 16, "bold") )

# window
window = tk.Tk()
window.geometry('640x960')
window.title('Fast Typing App')

# Title and subtitle
title = tk.Label(window, text="T Y P I N G   S P E E D   T E S T")
title.grid()
subtitle = tk.Label(window, text="Welcome!")
subtitle.grid()

# Text list
word_list = tk.StringVar()
word_list.set(" ".join(GAME_DATA))
word_list_box = tk.Text(window, height=15, width=60 )
word_list_box.insert(tk.END, word_list.get())
change_part_of_text()
word_list_box.configure(state="disabled")
word_list_box.grid(pady = 25)


# Player input
player_input = tk.Entry(window, width=40)
player_input.insert(0, "Type here to start!")
player_input.grid()
player_input.bind('<BackSpace>', going_back_in_list)
player_input.bind('<space>', add_wording)
player_input.bind('<Return>', add_wording)
player_input.bind('<Button-1>', handle_click)

# Button
start_button = tk.Button(window, text='Restart')
start_button.grid(pady=10)


# run 
window.mainloop()