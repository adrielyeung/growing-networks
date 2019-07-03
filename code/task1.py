import matplotlib.pyplot as pl
import numpy as np
import logbin6_2_2018 as lb

m = 32
power = 6

# Scale factor for logbin
a = 1.25

pl.figure()
for i in [32]:#range(6):
    
    # Load data
    k = np.loadtxt('k_10^%s_%s_sum100_p.csv' %(power, i)).astype('int64')
    
    # Plot p(k) vs k diagram
    bins = np.arange(min(k) - 1.5, max(k) + 2.5, 1)
    bincentre = bins[:-1] + 0.5
    hist, bin_edges = np.histogram(k, bins = bins, density = True) # density = True returns probability density
    
    # Log-bin the data
    bincentre_bin, hist_bin = lb.logbin(k, scale = a, zeros = False)
    
    pl.loglog(bincentre, hist, 'o', label = r"Unbinned, $N = 10^%d$ and $m = %d$" %(power, i))
    pl.loglog(bincentre_bin, hist_bin, '-', label = r"Binned, $N = 10^%d$ and $m = %d$" %(power, i))

pl.grid()
pl.legend()
