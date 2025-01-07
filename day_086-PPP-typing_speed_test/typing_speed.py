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

def load_data():
    global GAME_DATA, GAME_STARTED
    if GAME_STARTED :
        GAME_DATA = []
    with open("day_086-PPP-typing_speed_test/words.txt", "r") as f:
        data = [line.strip() for line in f]

        while len(GAME_DATA) < 100:
            new_word = choice(data).lower()
            if new_word not in GAME_DATA:
                GAME_DATA.append(new_word)

# reset the game when button pushed
def reset_game():
    global CORRECT_WORDS, PLAYER_WORDS, COUNTING, GAME_STARTED
    load_data()
    GAME_STARTED = False
    CORRECT_WORDS = []
    PLAYER_WORDS = []
    COUNTING = 0
    modify_text()
    player_input.config(state="normal")
    player_input.delete(0, tk.END)
    player_input.insert(0, "Type here to start!")
    subtitle.configure(text=f"Welcome!")
    window.focus()
    

# Handle countdown + modify subtitle
def count_down():
    global COUNTING
    wpm = len(PLAYER_WORDS)
    cpm = len("".join(PLAYER_WORDS))
    if TIMING > COUNTING and GAME_STARTED:
        COUNTING += 1
        subtitle.configure(text=f"{TIMING - COUNTING} seconds remaining!\n {int(wpm/TIMING*60)} words/min, {int(cpm/TIMING*60)} chars/min")
        window.after(1000, count_down)
    else:
        if GAME_STARTED:
            if PLAYER_WORDS == CORRECT_WORDS:
                subtitle.configure(text=f"Congratulation, no mistake!\n You're typing at {int(wpm/TIMING*60)} words/min, {int(cpm/TIMING*60)} chars/min")
            else :
                wrong_words = 0
                wrong_char = 0
                for i in range(len(CORRECT_WORDS)):
                    if PLAYER_WORDS[i] != CORRECT_WORDS[i]:
                        wrong_words += 1
                        wrong_char += len(PLAYER_WORDS[i])
                subtitle.configure(text=f"You've made some mistakes !\n You're typing at {int((wpm - wrong_words)/TIMING*60) } words/min ({wrong_words} mispelled word{"s" if wrong_words > 1 else ""}), {int((cpm- wrong_char)/TIMING*60) } chars/min")
            player_input.config(state="disabled")
    
# start the game when clicking on entry
def handle_click(event):
    global GAME_STARTED
    player_input.delete(0, tk.END)
    if not GAME_STARTED:
        GAME_STARTED = True
        subtitle.configure(text=f"{TIMING - COUNTING} seconds remaining!")
        window.after(1000, count_down)


def add_wording(event):
    word = player_input.get()
    # verify if entry is empty
    if word.strip() == "":
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
    word_list_box.tag_config("start", font=("Arial", 14, "bold") )



# window
window = tk.Tk()
window.geometry('650x500')
window.title('Fast Typing App')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky= 'nsew')
frame.columnconfigure([0,2], weight=1)
frame.columnconfigure(1, weight=3)
frame.rowconfigure(0, weight=1)

# Title and subtitle
title = tk.Label(frame, text="T Y P I N G   S P E E D   T E S T",  font=("Arial", 20, "bold"))
title.grid(row = 0, column=1)
subtitle = tk.Label(frame, text="Welcome!",  font=("Arial", 14, "bold"))
subtitle.grid(row = 1, column=1)


# Text list
load_data()
word_list = tk.StringVar()
word_list_box = tk.Text(frame, height=15, width=60 )
modify_text()
word_list_box.grid(row = 2, column=0, columnspan=3, pady = 25, padx=10, sticky= 'nsew')


# Player input
player_input = tk.Entry(frame, width=40)
player_input.insert(0, "Type here to start!")
player_input.grid(row = 3, column=1)
player_input.bind('<BackSpace>', going_back_in_list)
player_input.bind('<space>', add_wording)
player_input.bind('<Return>', add_wording)
player_input.bind('<Button-1>', handle_click)

# Button
start_button = tk.Button(frame, text='Restart', command=lambda: reset_game())
start_button.grid(row = 4, column=1, pady=10)


# run 
window.mainloop()