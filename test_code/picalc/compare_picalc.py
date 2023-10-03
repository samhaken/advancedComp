import sys
from picalc_pyx1 import main
import matplotlib.pyplot as plt
import numpy as np

times = []

for i in range(1,9):
    avg = []
    for j in range(10):
        time = main(1000000000, i)
        avg.append(time)
    times.append(sum(avg)/len(avg))
    
    

plt.bar(np.linspace(1, 8, 8), times, color='green')
plt.xlabel("# of cores")
plt.ylabel("Time (s)")
plt.title("Time taken to run picalc for 1E9 iterations (averaged over 10 runs)")

for i, v in enumerate(times):
    plt.text(i+0.4, v+0.05, "{:8.3f}".format(v))

plt.savefig("picalc")
