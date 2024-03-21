import tkinter as tk
from tkinter import ttk, font

# setup
window = tk.Tk()
window.geometry('400x300')
window.title('Styling')

# print(font.families())

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('winnative')

style.configure('new.TButton', foreground='green', font=('Georgia', 20))
style.map('new.TButton',
        foreground=[('pressed', 'red'), ('disabled', 'yellow')],
        background=[('pressed', 'green'), ('disabled', 'blue')])
style.configure('TFrame', background = 'pink')

# widgets
label = ttk.Label(
        window,
        text='A label\nAnd then type on another line',
        background='red',
        foreground='white',
        font=('Georgia', 20),
        justify='right')

label.pack()

button = ttk.Button(window, text='A button', style='new.TButton')
button.pack()

# exercise

frame = ttk.Frame(window, height=200, width=100)
frame.pack()

window.mainloop()