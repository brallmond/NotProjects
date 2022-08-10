#!/bin/bash

LINES=$(wc -l <~/Desktop/anims/HANDLES.txt)

LINE=$((1 + RANDOM%${LINES}))

sed "${LINE}q;d" ~/Desktop/anims/HANDLES.txt
