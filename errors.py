#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines() 
    # FileNotFoundError
    print(names.append)
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre")

try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)
