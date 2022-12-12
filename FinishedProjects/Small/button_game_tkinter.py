from tkinter import *
import random as random

window = Tk()

# name and size
window.title("Button Game")
window_width = 500
window_height = 300
window.configure(width=window_width, height=window_height)

def make_new_button():
  button = Button(window, text="click me!", command=lambda:[button.destroy(), make_new_button()])
  button.place(x=random.randint(0,window_width-50), y=random.randint(0,window_height-10))

make_new_button()

window.mainloop()
