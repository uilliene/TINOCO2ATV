from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

breast_cancer = fetch_ucirepo(id=17)
features = breast_cancer.data.features
targets = breast_cancer.data.targets["Diagnosis"]

boolean_targets = [int(val == "B") for val in targets]
colors = ['r', 'g']

texture = features["texture1"]
smoothness = features["smoothness1"]
fractal_dimension = features["fractal_dimension1"]
area = features["area1"]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_title("Breast Cancer 3d plot (Texture vs Smoothness vs Area)")
ax.set_xlabel('Texture')
ax.set_ylabel('Smoothness')
ax.set_zlabel('Area')
ax.scatter(texture, smoothness, area, s=10, c=[colors[i] for i in boolean_targets])

legend_elements = [
    Patch(facecolor='green', edgecolor='black', label='benign'),
    Patch(facecolor='red', edgecolor='black', label='malignant'),
]

plt.legend(handles=legend_elements, loc='best')

plt.show()
