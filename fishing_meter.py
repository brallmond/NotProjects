import curses
from random import randint, choice

class meter():
  move_counter = 0
  meter_active_str   = "#"
  meter_inactive_str = "-"
  spot_str = "@"
  meter_left_edge    = "["
  meter_right_edge   = "]"

  def __init__(self, full_length, active_length):
    self.full_length = full_length
    self.active_length = active_length
    self.inactive_length = full_length - active_length
    self.initial_position = randint(0, self.inactive_length)
    self.move_direction = choice([-1,1])
    
    self.spot = randint(1, self.full_length)
    self.meter_active = self.meter_active_str * active_length
    self.meter_head   = self.meter_inactive_str * (self.inactive_length - self.initial_position)
    self.meter_tail   = self.meter_inactive_str * (self.inactive_length - len(self.meter_head))

    self.spot_status = "DEFAULT"

    self.update_visual_meter()

  def update_visual_meter(self):
    self.visual_meter = self.meter_left_edge + self.meter_head + self.meter_active + self.meter_tail + self.meter_right_edge
    self.move_counter += 1
   
    if self.move_counter % 100 == 0:
       self.spot = randint(1, self.full_length)
    self.stationary_spot(self.spot)
    self.check_spot()
    self.all_meter_info = self.visual_meter + " : Spot : " + f"{str(self.spot):2}" + " : Status : " + self.spot_status

  def move_meter_right(self):
    self.meter_head += self.meter_inactive_str
    self.meter_tail = self.meter_tail[1::]

  def move_meter_left(self):
    self.meter_tail += self.meter_inactive_str
    self.meter_head = self.meter_head[1::]

  def move_meter(self):
    # detect edge and change direction
    if len(self.meter_head) == 0: self.move_direction = 1
    if len(self.meter_tail) == 0: self.move_direction = -1

    # move in direction
    if self.move_direction > 0: self.move_meter_right()
    if self.move_direction < 0: self.move_meter_left()

    self.update_visual_meter()

  def stationary_spot(self, index):
    self.visual_meter = self.visual_meter[:index] + self.spot_str + self.visual_meter[index + 1:]

  def check_spot(self):
    self.spot_location = self.visual_meter.index(self.spot_str)

    self.start_active = self.visual_meter.find(self.meter_inactive_str + self.meter_active_str) + 1
    if (self.start_active == -1): 
      self.start_active = self.visual_meter.find(self.meter_left_edge + self.meter_active_str) + 1

    self.end_active = self.visual_meter.find(self.meter_active_str + self.meter_inactive_str) 
    if (self.end_active == -1): 
      self.end_active = self.visual_meter.find(self.meter_active_str + self.meter_right_edge)

    self.spot_status = "OUTSIDE"
    if (self.start_active < self.spot_location < self.end_active): self.spot_status = "BETWEEN"

  def move_spot_left(self):
    if self.spot > 1:
      self.spot -= 1

  def move_spot_right(self):
    if self.spot < self.full_length:
      self.spot += 1



def display_meter(full_length, active_length):

  def _display_meter(stdscr):
    stdscr.clear()
    quit_char = ""
    n_meters = 30
    my_meters = [meter(full_length, active_length) for i in range(n_meters)]

    user_cursor = 0
    while True:

      stdscr.addstr(user_cursor, 0, ">", curses.A_BLINK)
      stdscr.addstr((user_cursor+1), 0, " ")
      if user_cursor > 0:
        stdscr.addstr((user_cursor-1), 0, " ")

      update_lines = 0
      for index, my_meter in enumerate(my_meters):
        stdscr.addstr(index, 6, my_meter.all_meter_info)
        my_meter.move_meter()
        update_lines += 1
      if update_lines < n_meters:
        for line in range(update_lines, n_meters):
          stdscr.addstr(line, 6,
"                                                                                               ")

      stdscr.refresh()
      stdscr.addstr(30, 0, f'Press [Q] and [ENTER] to quit')
      stdscr.timeout(40)
      code = stdscr.getch()
      stdscr.refresh()

      # [SPACE] is 32 to confirm placement/input
      # ARROW KEY TO CODE MAPPING
      # [up, down, left, right]
      # 259,  258,  260, 261
      
      if code == 259 and user_cursor != 0:
        user_cursor -= 1
      if code == 258:
        user_cursor += 1

      if code == 260:
        my_meters[user_cursor].move_spot_left()
      if code == 261:
        my_meters[user_cursor].move_spot_right()

      if code == 32 and my_meters[user_cursor].spot_status == "BETWEEN":
        my_meters.pop(user_cursor)


      stdscr.addstr(31, 0, f'Code: {code}')

      if code == ord("q"):
        quit_char += chr(code)
        continue

      if "q" in quit_char and code == 10:
        return "quitting"

  return curses.wrapper(_display_meter) 

   
print(display_meter(80, 20))

 
