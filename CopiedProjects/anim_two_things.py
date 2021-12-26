import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

#copied/adapted from https://matplotlib.org/gallery/animation/subplots.html

class SubplotAnimation(animation.TimedAnimation):
  def __init__(self):
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 2)
    ax2 = fig.add_subplot(2, 1, 1)
   
    el = 2.5
 
    self.t = np.linspace(0, 40, 200)
    self.s = np.linspace(-5,5, 200)
    self.x = el*np.cos(2 * np.pi * self.t / 10.)
    self.y = el*np.sin(2 * np.pi * self.t / 10.) 
    self.E = np.linspace(el, el+0.001, 200)
    ax2.plot(self.s, self.s*self.s)

    ax1.set_xlabel('')
    ax1.set_ylabel('')
    self.line1 = Line2D([], [], color='black')
    self.line1a = Line2D([], [], color='red', linewidth=2)
    self.line1e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
    ax1.add_line(self.line1)
    ax1.add_line(self.line1a)
    ax1.add_line(self.line1e)
    ax1.set_xlim(-2*5,2*5)
    ax1.set_ylim(-5,5) #overridden by set_aspect on next line 
    #ax1.set_aspect('equal', 'datalim')
    
    ax2.set_xlabel('')
    ax2.set_ylabel('')
    self.line2 = Line2D([], [], color='black')
    self.line2a = Line2D([], [], color='red', linewidth=2)
    self.line2e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
    ax2.add_line(self.line2)
    ax2.add_line(self.line2a)
    ax2.add_line(self.line2e)
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(0, 10)

    animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

  def _draw_frame(self, framedata):
    i = framedata
    head = i - 1
    head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])
  
    self.line1.set_data(self.x[:i], self.y[:i])
    self.line1a.set_data(self.x[head_slice], self.y[head_slice])
    self.line1e.set_data(self.x[head], self.y[head])

    self.line2.set_data(self.x[:i]/2.0, self.E[:i])
    self.line2a.set_data(self.x[head_slice]/2.0, self.E[head_slice])
    self.line2e.set_data(self.x[head]/2.0, self.E[head])

    self._drawn_artists = [self.line1, self.line1a, self.line1e,
                         self.line2, self.line2a, self.line2e]

  def new_frame_seq(self):
    return iter(range(self.t.size))

  def _init_draw(self):
    lines = [self.line1, self.line1a, self.line1e,
          self.line2, self.line2a, self.line2e]
    for l in lines:
      l.set_data([], [])

ani = SubplotAnimation()
plt.show()
