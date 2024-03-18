import tkinter as tk
from tkinter import ttk

def button_func():
    print('button pressed')
    
def ex_func():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text='This is a test')
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk exercise
label_ex = ttk.Label(master=window, text='exercise label')
label_ex.pack()

#ttk button
button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()

# button_ex = ttk.Button(master=window, text='Button exercise', command=ex_func)
button_ex = ttk.Button(master=window, text='Button exercise', command=lambda: print('hello'))
button_ex.pack()

# run
window.mainloop()