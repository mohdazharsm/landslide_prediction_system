import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("seaborn")

fig, ax = plt.subplots(2, 2, sharex=True)

for first in ax:
    for second in first:
        second.set_ylim(0, 255)
        second.grid()


def animate(i):
    try:
        data = pd.read_csv("processedData.csv")
        x = data.index.values
        RainFall_1 = data["Rain1"]
        Soil_1 = data["Moisture1"]
        X_1 = data["X1"]
        Y_1 = data["Y1"]
        Z_1 = data["Z1"]
        RainFall_2 = data["Rain2"]
        Soil_2 = data["Moisture2"]
        X_2 = data["X2"]
        Y_2 = data["Y2"]
        Z_2 = data["Z2"]

        ax[0][0].cla()
        ax[0][0].plot(x, RainFall_1, label="RainFall 1")  # , linestyle="--")
        ax[0][0].plot(
            x,
            RainFall_2,
            label="RainFall 2",
        )
        ax[0][0].set_title("Live Rainfall Data From 2 Nodes")
        ax[0][0].set_ylabel("Rainfall Intensity")
        ax[0][0].legend(loc="upper left")

        ax[1][0].cla()
        ax[1][0].plot(x, Soil_1, label="Moisture 1")  # , linestyle="--")
        ax[1][0].plot(x, Soil_2, label="Moisture 2")
        ax[1][0].set_ylabel("Moisture Content")
        ax[1][0].legend(loc="upper left")
        ax[1][0].set_xlabel("Time")

        ax[0][1].cla()
        ax[0][1].plot(x, X_1, label="X axis")  # , linestyle="--", color="r")
        ax[0][1].plot(x, Y_1, label="Y axis")  # , linestyle="-", color="y")
        ax[0][1].plot(x, Z_1, label="Z axis")  # , linestyle="-.", color="k")
        ax[0][1].set_title("Gyroscope Values From 2 Nodes")
        ax[0][1].set_ylabel("Gyroscope Values")
        ax[0][1].legend(loc="upper left")

        ax[1][1].cla()
        ax[1][1].plot(x, X_2, label="X axis")  # , linestyle="--", color="r")
        ax[1][1].plot(x, Y_2, label="Y axis")  # , linestyle="-", color="y")
        ax[1][1].plot(x, Z_2, label="Z axis")  # , linestyle="-.", color="k")
        ax[1][1].set_ylabel("Gyroscope Values")
        ax[1][1].legend(loc="upper left")
        ax[1][1].set_xlabel("Time")

        plt.tight_layout()
    except:
        pass


ani = FuncAnimation(fig, animate, interval=10)

plt.tight_layout()
plt.show()
