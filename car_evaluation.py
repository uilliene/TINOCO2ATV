from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt

car_evaluation = fetch_ucirepo(id=19)
features = car_evaluation.data.features
targets = car_evaluation.data.targets

df_targets = pd.DataFrame(targets)
df_targets["class_int"] = pd.factorize(df_targets["class"])[0]

df = pd.DataFrame(features)
df["buying_int"] = pd.factorize(df["buying"])[0]
df["safety_int"] = pd.factorize(df["safety"])[0]
df["lug_boot_int"] = pd.factorize(df["lug_boot"])[0]
df["maint_int"] = pd.factorize(df["maint"])[0]
df["doors_int"] = pd.factorize(df["doors"])[0]
df["persons_int"] = pd.factorize(df["persons"])[0]

fig, ax = plt.subplots(2, 3)

ax[0, 0].scatter(df["buying_int"], df["maint_int"])
ax[0, 0].set_xlabel("Buying")
ax[0, 0].set_ylabel("Maintenance")
point_counts = df.groupby(['buying_int', 'maint_int']).size()
print('buying_int', 'maint_int')
print(point_counts)
print(40 * "----/----")

ax[0, 1].scatter(df["buying_int"], df["safety_int"])
ax[0, 1].set_xlabel("Buying")
ax[0, 1].set_ylabel("Safety")
point_counts = df.groupby(['buying_int', 'safety_int']).size()
print('buying_int', 'safety_int')
print(point_counts)
print(40 * "----/----")

ax[0, 2].scatter(df["buying_int"], df["doors_int"])
ax[0, 2].set_xlabel("Buying")
ax[0, 2].set_ylabel("Doors")
point_counts = df.groupby(['buying_int', 'doors_int']).size()
print('buying_int', 'doors_int')
print(point_counts)
print(40 * "----/----")

ax[1, 0].scatter(df["safety_int"], df["doors_int"])
ax[1, 0].set_xlabel("Safety")
ax[1, 0].set_ylabel("Doors")
point_counts = df.groupby(['safety_int', 'doors_int']).size()
print('safety_int', 'doors_int')
print(point_counts)
print(40 * "----/----")

ax[1, 1].scatter(df["lug_boot_int"], df["doors_int"])
ax[1, 1].set_xlabel("Luggage Boot")
ax[1, 1].set_ylabel("Doors")
point_counts = df.groupby(['lug_boot_int', 'doors_int']).size()
print('lug_boot_int', 'doors_int')
print(point_counts)
print(40 * "----/----")

ax[1, 2].scatter(df["persons_int"], df["safety_int"])
ax[1, 2].set_xlabel("Persons")
ax[1, 2].set_ylabel("Safety")
point_counts = df.groupby(['persons_int', 'safety_int']).size()
print('persons_int', 'safety_int')
print(point_counts)
print(40 * "----/----")

plt.show()
