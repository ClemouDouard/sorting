import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from utils import quicksort

N = 1000
data = [rd.randint(1, 1000) for _ in range(N)]

if __name__ == "__main__":
    
    states = [data[:]]
    quicksort(data, 0, len(data) - 1, states)

    fig, ax = plt.subplots()
    bar_plot = ax.bar(range(len(data)), states[0], align="edge")

    def update(frame):
        for bar, h in zip(bar_plot, states[frame]):
            bar.set_height(h)
        return bar

    anim = animation.FuncAnimation(fig, update, frames=len(states), interval=1, repeat=False)
    plt.show()
    anim.save("quicksort.gif", writer="pillow")