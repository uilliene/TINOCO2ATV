from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt

breast_cancer = fetch_ucirepo(id=17)
features = breast_cancer.data.features
targets = breast_cancer.data.targets["Diagnosis"]

boolean_targets = [int(val == "B") for val in targets]
colors = ['r', 'g']

area = features["area1"]
perimeter = features["perimeter1"]
texture = features["texture1"]
concavity = features["concavity1"]
radius = features["radius1"]
smoothness = features["smoothness1"]
compactness = features["compactness1"]

fig, ax = plt.subplots(2, 3)
plt.subplots_adjust(hspace=0.4, wspace=0.25)

ax[0, 0].scatter(area, perimeter, c=[colors[i] for i in boolean_targets], s=10)
ax[0, 0].set_xlabel("Area")
ax[0, 0].set_ylabel("Perimeter")
ax[0, 0].set_title("Area x Perimeter scatter")

ax[0, 1].scatter(area, texture, c=[colors[i] for i in boolean_targets], s=10)
ax[0, 1].set_xlabel("Area")
ax[0, 1].set_ylabel("Texture")
ax[0, 1].set_title("Area x Texture scatter")

ax[0, 2].scatter(perimeter, texture, c=[colors[i] for i in boolean_targets], s=10)
ax[0, 2].set_xlabel("Perimeter")
ax[0, 2].set_ylabel("Texture")
ax[0, 2].set_title("Perimeter x Texture scatter")

ax[1, 0].scatter(concavity, smoothness, c=[colors[i] for i in boolean_targets], s=10)
ax[1, 0].set_xlabel("Concavity")
ax[1, 0].set_ylabel("Smoothness")
ax[1, 0].set_title("Concavity x Smoothness scatter")

ax[1, 1].scatter(compactness, texture, c=[colors[i] for i in boolean_targets], s=10)
ax[1, 1].set_xlabel("Compactness")
ax[1, 1].set_ylabel("Texture")
ax[1, 1].set_title("Compactness x Texture scatter")

ax[1, 2].scatter(compactness, radius, c=[colors[i] for i in boolean_targets], s=10)
ax[1, 2].set_xlabel("Compactness")
ax[1, 2].set_ylabel("Radius")
ax[1, 2].set_title("Compactness x Radius scatter")

plt.show()
