import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'eff': [0.214890, 1.868769, 0.208101, 1.141004, 1.608346, 0.858528, 1.608346, 0.858528],
    'sd_eff': [0.052207, 0.014918, 0.049254, 0.075598, 0.013549, 0.526916, 0.337685, 0.402076],
    'ci_low': [0.112566, 1.839530, 0.111565, 0.992834, 1.581791, -0.174208, 0.946496, 0.070473],
    'ci_upp': [0.317215, 1.898007, 0.304637, 1.289173, 1.634901, 1.891264, 2.270195, 1.646583],
    'w_fe': [0.067349, 0.824863, 0.075668, 0.032120, 1.000000, pd.NA, 1.000000, pd.NA],
    'w_re': [0.250010, 0.250575, 0.250077, 0.249339, pd.NA, 1.000000, pd.NA, 1.000000]
}

index = [
    'Walker 2014',
    'Shuaib 2019',
    'Zallman 2019',
    'Noaimi 2022',
    'Fixed Effect',
    'Random Effect',
    'Fixed Effect WLS',
    'Random Effect WLS',
]

# df = pd.DataFrame(data, index=index)

x = np.array(data['eff'][::-1])
y = np.arange(0, 8)
x2 = np.zeros(8)

fig, ax1 = plt.subplots(nrows=1, figsize=(9, 6))

error_vals = [(round(1.96 * data['sd_eff'][i], 6), round(1.96 * data['sd_eff'][i], 6)) for i in range(0, 8)]
err_val_reorder = error_vals[::-1]

x2_labels = [f"{data['eff'][i]} ({data['ci_low'][i]}, {data['ci_upp'][i]})" for i in range(0, 8)]

xerr = np.array(err_val_reorder).T

ax1.errorbar(x, y, xerr=xerr, fmt='o', capsize=5,
             markersize=5,
             markerfacecolor='black',
             markeredgecolor='black',
             ecolor='red')
ax1.set_title('Patients per Hour')

plt.xticks(range(-1, 4))
plt.yticks(range(0, 8), index[::-1])

ax1.grid(False)
ax1.set_xlabel("Cohen's d")

ax2 = ax1.twinx()  # Sets up second y labels on right side
ax2.plot(x2, y, ls='--')
ax2.grid(False)
ax2.set_yticks(y)
ax2.set_yticklabels(x2_labels[::-1])

plt.tight_layout()
# fig.savefig("fig2.png")
plt.show()

