There are two programs in this directory. They're more than a few lines,
and I didn't document them very well when I made them. There are also some
options (and some hardcoding) that I should have described better when I wrote
the code initially. Lesson learned I suppose.

Anyways

bbcode.py
execute like this
python bbcard.py

This was my first attempt at classes and writing a turn-based terminal
auto-battler. It's a little jank, and honestly I did not do myself any favors
commenting the code or making it readable. Keeping it so one day I can say 
I learned something, but I don't intend to work on it again.

Liss_SHO.py  
execute like this
python3 Liss_SHO.py

I wrote this code for graduate advanced dynamics. It draws lissajous figures
and randomly selects initial conditions. Many presets are defined, and the animation
is pretty solid. A better man would include a gif in this library.


MC_mass_slow.py
execute like this (not compatible with python2)
python3 MC_mass_slow.py

This is a python implementation of MC Photon Propagation.
But, if you're not totalling the "photon weight" deposition,
it's really just brownian motion (random walk). Anyways, see the 
pseudo-code on the wikipedia page.
It would be better to write this with a grid and binning scheme than
3D lines, but maybe this is a good visual demonstartion anyways.
https://en.wikipedia.org/wiki/Monte_Carlo_method_for_photon_transport
