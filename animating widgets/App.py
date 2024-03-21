import customtkinter as ctk
from random import choice

# exercise
# animate the button and move it right side of the window

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)
        
        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)
        
        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True
        
        # layout
        self.place(relx = self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)
        
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False
    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

        
def exercise_animation():
    global button_x
    # colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
    if button_x < 0.9:
        button_x += 0.001
        # color = choice(colors)
        # button.configure(fg_color = color)
        button.place(relx=button_x, rely=0.5, anchor='center')
        window.after(10, exercise_animation)

def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, anchor='center')
    
    # configure
    colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
    color = choice(colors)
    button.configure(fg_color = color)

def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print('infinite')
        print(button_x)
        window.after(100, infinite_print)

# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

# animated widget
animated_panel = SlidePanel(window, 1, 0.7)
ctk.CTkLabel(animated_panel, text='Label 1').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkLabel(animated_panel, text='Label 2').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(animated_panel, text='Button 1', corner_radius=0).pack(expand=True, fill='both', pady=10)
ctk.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', pady=10)




#button
button_x = 0.5
button = ctk.CTkButton(window, text='toggle sidebar', command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor='center')

window.mainloop()