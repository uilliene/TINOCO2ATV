from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt

wine = fetch_ucirepo(id=109)

ash = wine.data.features["Ash"]
alcohol = wine.data.features["Alcohol"]
malic_acid = wine.data.features["Malicacid"]
hue = wine.data.features["Hue"]
color_intensity = wine.data.features["Color_intensity"]
magnesium = wine.data.features["Magnesium"]

fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.5)
axes[0, 0].scatter(ash, alcohol, c=color_intensity, s=10)
axes[0, 0].set_xlabel("Ash")
axes[0, 0].set_ylabel("Alcohol")
axes[0, 0].set_title("Ash x Alcohol scatter")

axes[1, 0].scatter(malic_acid, alcohol, c=color_intensity, s=10)
axes[1, 0].set_xlabel("Malic Acid")
axes[1, 0].set_ylabel("Alcohol")
axes[1, 0].set_title("Malic Acid x Alcohol scatter")

axes[0, 1].scatter(hue, alcohol, c=color_intensity, s=10)
axes[0, 1].set_xlabel("Hue")
axes[0, 1].set_ylabel("Alcohol")
axes[0, 1].set_title("Hue x Alcohol scatter")

axes[1, 1].scatter(magnesium, alcohol, c=color_intensity, s=10)
axes[1, 1].set_xlabel("Magnesium")
axes[1, 1].set_ylabel("Alcohol")
axes[1, 1].set_title("Magnesium x Alcohol scatter")

plt.show()
