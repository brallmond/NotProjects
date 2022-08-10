This is a small project that randomly chooses your terminal handle
from one of the lines in the file HANDLES.txt included in this library.

instructions:
look for your .bashrc file by doing ls -a in your home directory

put this line at the bottom of your bashrc file 

PS1="\e[0;36m$(~/path/to/file/pick_text.sh) (\w)\e[0m \n"

and change the directory above to wherever you downloaded this library to

pick_text.sh points to a file called HANDLES.txt, 
which currently contains Halo and CowboyBebop title cards (also included as separate files in this directory)

feel free to update for your own customisation 

also, prepend pick_text with a "." to hide the file.
Make sure to propagate that change to HANDLES.txt as well
and update the filename in your bashrc as well.
