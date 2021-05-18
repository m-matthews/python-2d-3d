import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
from matplotlib.animation import FuncAnimation, PillowWriter


frames = 80

fig, ax = plt.subplots(1, figsize=(12, 3))


def circle(pct):
    ax.clear()
    ax.set_axisbelow(True)
    ax.xaxis.grid(color='gray', linestyle='dashed')
    ax.yaxis.grid(color='gray', linestyle='dashed')
    p = Circle((math.pi*pct, 0.5), 0.5, color='lightblue', linewidth=1.0, fill=True)
    ax.add_patch(p)
    p = Arc((math.pi*pct, 0.5), 1.0, 1.0, 0.0, -90.0, 360.0*(1-pct)-90.0, color='b', linewidth=5.0)
    ax.add_patch(p)
    ax.plot([0.0, math.pi*pct], [0.0, 0.0], color='b', linewidth=5.0)
    ax.axis((-0.6, 4.2, 0.0, 1.2))
    plt.yticks([0.0, 1.0], [0, 1])
    if pct == 1.0:
        plt.xticks([0.0, 1.0, 2.0, 3.0, math.pi, 4.0], [0, 1, 2, 3, r'$\pi$', 4])


def init():
    circle(0.0)


def update(i):
    pct = i/(frames-1)
    pct = max(0.0, min(pct, 0.75)-0.25) * 2.0
    circle(pct)


ani = FuncAnimation(fig, update, range(frames), init_func=init)

writer = PillowWriter(fps=25)
ani.save("07_pi.gif", writer=writer)
plt.show()
