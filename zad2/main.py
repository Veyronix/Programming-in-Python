from termcolor import colored
import json
import matplotlib.pyplot as plt
from Draw import Draw
import tkinter
from Shape import Shape,Square
from JSONParser import JSONParser
import sys
# from square import Square


if __name__ == "__main__":
    pass
    file = open("to_print.txt","r")
    all_lines = ""
    for i in file:
        all_lines += i
    try:
        json_my = JSONParser(json.loads(all_lines))
        Draw.draw_to_screen(json_my)
    except ValueError:
        print("Bad JSON",sys.exc_info())
        exit(1)


