import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'eff': [0.445308, 0.072162, 0.076212, 0.214890, 1.868769, 0.208101, 1.061426, 0.332800, 1.141004, 0.894289, 0.602399, 0.894289, 0.602399],
    'sd_eff': [0.037592, 0.041398, 0.015434, 0.052207, 0.014918, 0.049254, 0.018179, 0.058540, 0.075598, 0.008376, 0.289120, 0.267571, 0.206453],
    'ci_low': [0.371629, -0.008976, 0.045962, 0.112566, 1.839530, 0.111565, 1.025795, 0.218064, 0.992834, 0.877873, 0.035733, 0.369860, 0.197759],
    'ci_upp': [0.518987, 0.153300, 0.106462, 0.317215, 1.898007, 0.304637, 1.097056, 0.447537, 1.289173, 0.910706, 1.169065, 1.418719, 1.007039],
    'w_fe': [0.049643, 0.040935, 0.294509, 0.025739, 0.315236, 0.028918, 0.212274, 0.020471, 0.012275, 1.000000, pd.NA, 1.000000, pd.NA],
    'w_re': [0.111201, 0.111156, 0.111375, 0.111007, 0.111377, 0.111051, 0.111361, 0.110904, 0.110568, pd.NA, 1.000000, pd.NA, 1.000000]
}

index = [
    'Graves 2018',
    'Walker 2016',
    'Walker 2019',
    'Walker 2014',
    'Shuaib 2019',
    'Zallman 2019',
    'Bank 2015',
    'Piersa 2021',
    'Noaimi 2022',
    'Fixed Effect',
    'Random Effect',
    'Fixed Effect WLS',
    'Random Effect WLS',
]

# df = pd.DataFrame(data, index=index)

x = np.array(data['eff'][::-1])
y = np.arange(0, 13)
x2 = np.zeros(13)

fig, ax1 = plt.subplots(nrows=1, figsize=(9, 6))

error_vals = [(round(1.96 * data['sd_eff'][i], 6), round(1.96 * data['sd_eff'][i], 6)) for i in range(0, 13)]
err_val_reorder = error_vals[::-1]

x2_labels = [f"{data['eff'][i]} ({data['ci_low'][i]}, {data['ci_upp'][i]})" for i in range(0, 13)]

xerr = np.array(err_val_reorder).T

ax1.errorbar(x, y, xerr=xerr, fmt='o', capsize=5,
             markersize=5,
             markerfacecolor='black',
             markeredgecolor='black',
             ecolor='red')
ax1.set_title('Patients per Hour')

plt.xticks(range(-1, 4))

plt.yticks(range(0, 13), index[::-1])

ax1.grid(False)
ax1.set_xlabel("Cohen's d")

ax2 = ax1.twinx()  # Sets up second y labels on right side
ax2.plot(x2, y, ls='--')
ax2.grid(False)
ax2.set_yticks(y)
ax2.set_yticklabels(x2_labels[::-1])

plt.tight_layout()

fig.savefig('fig3.png')
# plt.show()
