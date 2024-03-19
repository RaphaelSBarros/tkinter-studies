import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Hide widgets')
window.geometry('600x400')

def toggle_label_pack():
    global label_visible
    if label_visible:
        label.pack_forget()
        label_visible = False
        frame.pack(expand=True, before=button)
    else:
        frame.pack_forget()
        label.pack(expand=True, before=button)
        label_visible = True
    
label_visible = True
label = ttk.Label(window, text='A label')
label.pack(expand=True)

button = ttk.Button(window, text='toggle Label', command=toggle_label_pack)
button.pack()

frame = ttk.Frame(window)

# run
window.mainloop()