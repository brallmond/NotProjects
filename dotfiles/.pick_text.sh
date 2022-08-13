#!/bin/bash

LINES=$(wc -l < ~/.HANDLES.txt)

LINE=$((1 + RANDOM%${LINES}))

sed "${LINE}q;d" ~/.HANDLES.txt
