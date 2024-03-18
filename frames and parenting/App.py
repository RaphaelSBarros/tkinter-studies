import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('800x600')
window.title('Frames and parenting')

# frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

# master setting
label = ttk.Label(frame, text='Label in frame')
label.pack()

button = ttk.Button(frame, text='Button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text='Label outside frame')
label2.pack(side='left')

# exercise
frame2 = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side='right')

label3 = ttk.Label(frame2, text='Label in frame2')
label3.pack()

button2 = ttk.Button(frame2, text='Button in a frame')
button2.pack()

entry = ttk.Entry(frame2)
entry.pack()


window.mainloop()