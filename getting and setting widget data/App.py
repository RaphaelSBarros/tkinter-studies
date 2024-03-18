import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()
    # update the label
    # label.configure(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    
def button_enable():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

window = tk.Tk()
window.title('Getting and setting widgets')

label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The Button', command=button_func)
button.pack()

button2 = ttk.Button(master=window, text='enable', command=button_enable)
button2.pack()

window.mainloop()