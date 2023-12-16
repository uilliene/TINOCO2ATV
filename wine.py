from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt

wine = fetch_ucirepo(id=109)

x = wine.data.features["Ash"]
y = wine.data.features["Alcohol"]

plt.scatter(x, y)
plt.xlabel("Ash")
plt.ylabel("Alcohol")
plt.title("Ash x Alcohol scatter")
plt.show()
