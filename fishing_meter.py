import curses
from random import randint, choice

class meter():
  move_counter = 0
  meter_active_str   = "#"
  meter_inactive_str = "-"
  meter_left_edge    = "["
  meter_right_edge   = "]"

  def __init__(self, full_length, active_length):
    self.inactive_length = full_length - active_length
    self.initial_position = randint(0, self.inactive_length)
    self.move_direction = choice([-1,1])
    
    self.meter_active = self.meter_active_str * active_length
    self.meter_head   = self.meter_inactive_str * (self.inactive_length - self.initial_position)
    self.meter_tail   = self.meter_inactive_str * (self.inactive_length - len(self.meter_head))

    self.update_visual_meter()

  def update_visual_meter(self):
    self.visual_meter = self.meter_left_edge + self.meter_head + self.meter_active + self.meter_tail + self.meter_right_edge

  def go_right(self):
    self.meter_head += self.meter_inactive_str
    self.meter_tail = self.meter_tail[1::]

  def go_left(self):
    self.meter_tail += self.meter_inactive_str
    self.meter_head = self.meter_head[1::]

  def move(self):
    # detect edge and change direction
    if len(self.meter_head) == 0: self.move_direction = 1
    if len(self.meter_tail) == 0: self.move_direction = -1

    # move in direction
    if self.move_direction > 0: self.go_right()
    if self.move_direction < 0: self.go_left()

    self.update_visual_meter()


def display_meter(full_length, active_length):

  def _display_meter(stdscr):
    stdscr.clear()
    quit_char = ""
    n_meters = 30
    my_meters = [meter(full_length, active_length) for i in range(n_meters)]

    while quit_char != "q":

      for index, my_meter in enumerate(my_meters):
        stdscr.addstr(index, 0, f'Meter{index}: {my_meter.visual_meter}')
        my_meter.move()

      stdscr.refresh()
      stdscr.addstr(30, 0, f'Press q to quit')
      stdscr.timeout(45)
      code = stdscr.getch()
      stdscr.refresh()

      if code == ord("q"):
        quit_char += chr(code)
        continue

      if quit_char == "q" and code == 10:
        return "quitting"

  return curses.wrapper(_display_meter) 

   
print(display_meter(80, 20))

 
