from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt

heart_disease = fetch_ucirepo(id=45)
features = heart_disease.data.features
targets = heart_disease.data.targets["num"]
df = pd.DataFrame(features)

fig, axes = plt.subplots(2, 2)

sex_colors = ["violet", "blue"]
targets_colors = ["r", "g", "b", "m", "c"]

axes[0, 0].scatter(df["age"], df["trestbps"], c=[sex_colors[i] for i in df["sex"]], s=5)
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Trestbps")
axes[0, 0].set_title("Age x Trestbps scatter")

axes[0, 1].scatter(df["age"], df["thalach"], c=[targets_colors[i] for i in targets], s=5)
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_ylabel("thalach")
axes[0, 1].set_title("Age x thalach scatter")

axes[1, 0].scatter(df["thalach"], df["chol"], c=df["cp"], s=5)
axes[1, 0].set_xlabel("thalach")
axes[1, 0].set_ylabel("chol")
axes[1, 0].set_title("thalach x chol scatter")

axes[1, 1].scatter(df["age"], df["chol"], c=[sex_colors[i] for i in df["sex"]], s=5)
axes[1, 1].set_xlabel("age")
axes[1, 1].set_ylabel("chol")
axes[1, 1].set_title("age x chol scatter")

plt.subplots_adjust(hspace=0.5)
plt.show()
