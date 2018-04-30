# from JSONParser import JSONParser
import matplotlib.pyplot as plt
from Shape import Circle
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import interactive
from JSONParser import JSONParser

class Draw:

    @staticmethod
    def draw_to_screen(json_parser):
        palette = json_parser.get_palette()
        screen = json_parser.get_screen()
        shapes = json_parser.get_shapes()

        fig = plt.figure(1)
        ax = fig.add_subplot(1, 1, 1,aspect='equal')
        ax.autoscale(False)
        plt.axis([0,screen["width"],0,screen["height"]])

        # BG AND FG
        JSONParser.return_color(palette,screen["bg_color"])
        ax.add_patch(plt.Rectangle((0, 0), screen["width"],screen["height"],facecolor=JSONParser.return_color(palette,screen["bg_color"]),zorder=-1))
        ax.add_patch(plt.Rectangle((0, 0), screen["width"],screen["height"],facecolor=JSONParser.return_color(palette,screen["fg_color"]),zorder=0))

        for i in shapes:
            print(i.__class__.__name__ )
            i.get_shape(ax)
        plt.axis('off')

        # //////to save to file
        # fig.savefig('to.png')
        # plt.close(fig)
        # ///////

        plt.show()


        pass