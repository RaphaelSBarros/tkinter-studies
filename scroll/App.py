import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# canvas
canvas = tk.Canvas(window, bg='white', scrollregion=(0,0,2000,5000))
canvas.create_line(0,0,2000,5000, fill='green', width=10)
for i in range(100):
    l = randint(0,2000)
    t = randint(0,5000)
    r = l+ randint(10, 500)
    b = t+ randint(10, 500)
    color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(l,t,r,b, fill=color)
canvas.pack(expand=True, fill='both')

# mousewheel scrolling
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

# scrollbar
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

scrollbar_bottom = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))

window.mainloop()