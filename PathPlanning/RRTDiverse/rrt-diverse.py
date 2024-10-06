import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from RRT.rrt import RRT
from RRTStar.rrt_star import RRTStar

show_animation = True

print("Start " + __file__)

# ====Search Path with RRT====
obstacle_list = [
    (5, 5, 0.1),
    (3, 6, 0.2),
    (3, 8, 0.2),
    (3, 10, 0.2),
    (7, 5, 0.2),
    (9, 5, 0.2),
    (8, 10, 1),
    (6, 12, 1),
]  # [x,y,size(radius)]

# Set Initial parameters
rrt_star = RRTStar(
    start=[0, 0],
    goal=[6, 10],
    rand_area=[-2, 15],
    obstacle_list=obstacle_list,
    expand_dis=1, # max length of one RRT branch step
    robot_radius=0.8,
    max_iter=1000)
path = rrt_star.planning(animation=show_animation)

if path is None:
    print("Cannot find path")
else:
    print("found path!!")

    # Draw final path
    if show_animation:
        rrt_star.draw_graph()
        plt.plot([x for (x, y) in path], [y for (x, y) in path], 'r--')
        plt.grid(True)
        plt.show()