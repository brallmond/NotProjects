from tkinter import *
import time as time

window = Tk()

# name size and color
window.title("Moving Rectangle")
window.configure(width=500, height=300)

canvas_width = 450
canvas_height = 290
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

canvas_center = canvas_width/2
canvas_pad = 10

sweet_spot_start = 15
sweet_spot_location = sweet_spot_start

big_rectangle = canvas.create_rectangle(canvas_center - 25, canvas_pad, canvas_center + 25, canvas_height - canvas_pad, fill='white')

middle_rectangle = canvas.create_rectangle(canvas_center - 24, canvas_pad, canvas_center + 24, 30, fill='blue')

small_rectangle = canvas.create_rectangle(canvas_center - 24, sweet_spot_start, canvas_center + 24, sweet_spot_start+10, fill='green')


def move_meter(start_location, sign):
  xinc = 0
  yinc = 1*sign
  canvas.move(small_rectangle, xinc, yinc)
  canvas.move(middle_rectangle, xinc, yinc)
  window.update()
  time.sleep(0.009)
  new_location = start_location + yinc
  return new_location


def check_direction(box_location, sign):
  if box_location < canvas_pad: sign = 1
  elif box_location > (canvas_height - canvas_pad): sign = -1
  return sign


def start_game():
  sign = 1
  current_location = move_meter(sweet_spot_location, sign)
  while True:
    sign = check_direction(current_location, sign)
    current_location = move_meter(current_location, sign)


# button to quit
button_quit = Button(window, text='quit', command=window.destroy)
button_quit.place(x=0, y=0) 
# button to start
button_start = Button(window, text='start', command=start_game)
button_start.place(x=0, y=30)


window.mainloop()
