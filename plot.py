import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# 1. Data Processing
data = [11508721, 11436047, 11425229, 12202640, 11441374, 11984172, 11670751, 11571645, 11526916, 11451308, 
        11518323, 11576914, 11560003, 11454561, 11464793, 11622547, 11620241, 11668605, 11647261, 11646366, 
        11648694, 11641187, 11457428, 11578650, 11728100, 11652318, 11699846, 11443833, 11735799, 11870721, 
        11618702, 11673435, 11625352, 11679605, 11675263, 11632739, 11652826, 11676306, 11570736, 11762888, 
        11547989, 11568199, 11564618, 11625661, 11623094, 11561067, 11659513, 11582627, 11627106, 11547897, 
        11584511, 11623425, 11627496, 11675639, 11678885, 11711413, 11638846, 11551774, 11647131, 11744146, 
        11564255, 11707450, 11545896, 11713262, 11543508, 11524981, 11723960, 11560320, 11621398, 11681299, 
        11661487, 11698690, 11716948, 11624993, 11659632, 11697802, 11615027, 11603229, 11536061, 11587415, 
        11574810, 11544326, 11712390, 11578361, 11624994, 11760681, 11772036, 11715953, 11616959, 11550172, 
        11671991, 11560757, 11653872, 11517787, 11585654, 11598434, 11595596, 11561600, 11527313, 11580741]

# 2. Statistics
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
bin_width = 100000
bins = np.arange(11100000, 12500000, bin_width)

# Shared Axis Limits for "Easy Comparison"
x_limits = (11100000, 12500000)
y_limits = (0, 45)

# --- GRAPH 1: Relative Frequency Histogram ---
plt.figure(figsize=(10, 5))
plt.hist(data, bins=bins, weights=np.ones(len(data)) / len(data) * 100, 
         color='#345e77', edgecolor='black', alpha=0.8)
plt.title('Relative Frequency Histogram', fontsize=14)
plt.xlabel('Execution Time (ns)', fontsize=12)
plt.ylabel('Relative Frequency (%)', fontsize=12)
plt.xlim(x_limits)
plt.ylim(y_limits)
plt.xticks(bins, [f'{int(val):,}' for val in bins], rotation=-30, ha='left')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# --- GRAPH 2: Normal Distribution Curve ---
plt.figure(figsize=(10, 5))
x = np.linspace(x_limits[0], x_limits[1], 1000) # Large number of x values for smooth curve
# Scaling the PDF by bin_width * 100 to match the % scale of the histogram
p = norm.pdf(x, mean, std_dev) * bin_width * 100
plt.plot(x, p, 'r', linewidth=2.5)
plt.axvline(mean, color='blue', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
plt.title('Normal Distribution Curve', fontsize=14)
plt.xlabel('Execution Time (ns)', fontsize=12)
plt.ylabel('Probability Density (Scaled to %)', fontsize=12)
plt.xlim(x_limits)
plt.ylim(y_limits)
plt.xticks(bins, [f'{int(val):,}' for val in bins], rotation=-30, ha='left')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.legend()
plt.show()




