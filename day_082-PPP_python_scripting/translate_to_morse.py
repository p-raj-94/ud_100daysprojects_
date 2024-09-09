from tkinter import *
import pyperclip

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

window = Tk()
window.title("Text to Morse Converter")
window.config(pady= 20, padx= 100)

def text_to_morse():
    global MORSE_CODE_DICT
    text = text_value.get('1.0', 'end')
    text = text.split(" ")
    morse_encode = ""
    for word in text:
        word = word.strip("\n")
        for x in word:
            y = x.upper()
            if not MORSE_CODE_DICT.get(y):
                return change_text(f"Only character accepted are A-Z, 0-9 or \",.?/-()\" ")
            morse_encode += MORSE_CODE_DICT.get(y)+ " "
        if word != text[-1].strip("\n"):
            morse_encode += "/ "
    change_text(morse_encode)
    

def change_text(morse_text):
    morse_value['state'] = 'normal'
    morse_value.delete('1.0', 'end')
    morse_value.insert("1.0", f"{morse_text}")
    morse_value['state'] = 'disabled'

def copy_code():
    pyperclip.copy(morse_value.get('1.0', 'end'))


text_label = Label(text="Text to convert:")
text_label.grid(column=0, row= 0)

text_value = Text(width=50, height=5)
text_value.grid(column=0, row= 1)

translate_button = Button(text="Translate", command=text_to_morse)
translate_button.grid(column=0, row=2, pady=10)



morse_label = Label(text="Output in Morse:")
morse_label.grid(column=0, row= 3)

morse_value = Text(width=50, height=5)
morse_value.grid(column=0, row= 4)
morse_value['state'] = 'disabled'

copy_button = Button(text="Copy", command=copy_code)
copy_button.grid(column=0, row=5, pady=10)


window.mainloop()
