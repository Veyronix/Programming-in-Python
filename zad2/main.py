from json import loads
import matplotlib.pyplot as plt
from JSONParser import JSONParser
from sys import argv, exc_info
from os.path import exists


def draw(json_parser, if_print):
    palette = json_parser.get_palette()
    screen = json_parser.get_screen()
    shapes = json_parser.get_shapes()

    fig = plt.figure(figsize=(screen["width"], screen["height"]), dpi=1)

    fig.artists.append(plt.Rectangle((0, 0), screen["width"], screen["height"],
                                     facecolor=JSONParser.return_color(palette, screen["bg_color"]), zorder=0))
    for i in shapes:
        i.add_shape(fig)

    if if_print == 1:
        fig.savefig(argv[3])
        plt.close(fig)
    else:
        plt.show()


def main():
    if_to_print = 0
    if not exists(str(argv[1])):
        print("Given file doesnt exist.")
        return 1
    if len(argv) == 4 and argv[2] == "-o":
        if_to_print = 1
    elif len(argv) != 2:
        print("Bad amount of arguments.")
        return 1
    file = open(str(argv[1]), "r")
    all_lines = ""
    for i in file:
        all_lines += i
    try:
        json_my = JSONParser(loads(all_lines))

    except ValueError:
        print("Bad JSON", exc_info())
        return 1

    draw(json_my, if_to_print)


if __name__ == "__main__":
    main()
