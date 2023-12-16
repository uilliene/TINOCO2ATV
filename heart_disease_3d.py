from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd

heart_disease = fetch_ucirepo(id=45)
features = heart_disease.data.features
df = pd.DataFrame(features)

sex_colors = ["violet", "blue"]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_xlabel('thalach')
ax.set_ylabel('trestbps')
ax.set_zlabel('chol')
ax.scatter(df["thalach"], df["trestbps"], df["chol"], s=10, c=[sex_colors[i] for i in df["sex"]])

legend_elements = [
    Patch(facecolor='pink', edgecolor='black', label='Woman'),
    Patch(facecolor='blue', edgecolor='black', label='Man'),
]
plt.legend(handles=legend_elements, loc='best')

plt.show()
