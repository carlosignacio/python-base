#!/usr/bin/env python3

import os
import sys

# LYBL - Look Before You Leap

if os.path.exists("names.txt"):
    input("...") # Race Condiction
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[1])
else: 
    print("[Error]: Missing name in the list")
    sys.exit(1)
