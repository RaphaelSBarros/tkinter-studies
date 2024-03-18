import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('300x150')
window.title('Tkinter Variables')

def button_func():
    print(string_var.get())
    string_var.set('Button pressed')

# tkinter  variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

window.mainloop()