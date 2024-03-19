import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('extra window')
        self.geometry('300x400')
        ttk.Label(self, text='A label').pack()
        ttk.Button(self, text='A Button').pack()
        ttk.Label(self, text='Another label').pack(expand=True)

def ask_yes_no():
    answer = messagebox.askquestion('Title', 'Body')
    print(answer)
    
def create_window():
    global extra_window
    extra_window = Extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('extra window')
    # extra_window.geometry('300x400')
    # ttk.Label(extra_window, text='A label').pack()
    # ttk.Button(extra_window, text='A Button').pack()
    # ttk.Label(extra_window, text='Another label').pack(expand=True)
def close_window():
    extra_window.destroy()

window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text='open main window', command= create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window')
button2.pack(expand=True)

button3 = ttk.Button(window, text='create yes no window', command= ask_yes_no)
button3.pack(expand=True)

window.mainloop()