import statsmodels
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from statsmodels.stats.meta_analysis import (
    effectsize_smd,
    combine_effects,
)

# data = [
#     ["Graves 2018", 2.49, 0.60, 1152, 2.81, 0.78, 1949, ],
#     ["Walker 2016", 1.02, 1.63, 1595, 1.13, 1.32, 921, ],
#     ["Walker 2019", 1.13, 2.36, 23838, 1.31, 2.37, 5098, ],
#     ["Walker 2014", 1.32, 1.28, 2065, 1.64, 2.21, 448, ],
#     ["Shuaib 2019", 2.30, 0.30, 12271, 3.20, 0.60, 13598, ],
#     ["Zallman 2019", 1.82, 0.76, 980, 1.98, 0.78, 718, ],
#     ["Bank 2015", 2.28, 0.15, 8468, 2.50, 0.27, 5785, ],
#     ["Piersa 2021", 1.65, 0.69, 605, 1.85, 0.49, 579, ],
#     ["Noaimi 2022", 0.61, 0.13, 362, 0.83, 0.23, 463, ]]

data = [
    ["Walker 2014", 1.32, 1.28, 2065, 1.64, 2.21, 448],
    ["Shuaib 2019", 2.3, 0.3, 12271, 3.2, 0.6, 13598],
    ["Zallman 2019", 1.82, 0.76, 980, 1.98, 0.78, 718],
    ["Noaimi 2022", 0.61, 0.13, 362, 0.83, 0.23, 463],
]

colnames = ["study", "mean_c", "sd_c", "n_c", "mean_t", "sd_t", "n_t"]
rownames = [i[0] for i in data]
dframe1 = pd.DataFrame(data, columns=colnames)

mean2, sd2, nobs2, mean1, sd1, nobs1 = np.asarray(
    dframe1[["mean_t", "sd_t", "n_t", "mean_c", "sd_c", "n_c"]]
).T

np.array(nobs1 + nobs2)

eff, var_eff = effectsize_smd(mean2, sd2, nobs2, mean1, sd1, nobs1)

res3 = combine_effects(eff, var_eff, method_re="chi2", use_t=False, row_names=rownames)

res3.conf_int(alpha=0.05)
print(res3.summary_frame())

# fig = res3.plot_forest()
# fig.set_figheight(6)
# fig.set_figwidth(10)

# plt.show()
