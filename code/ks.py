import numpy as np
import matplotlib.pyplot as pl
import logbin6_2_2018 as lb
import scipy.stats as st

power = 6

a = 1.25

# Define theoretical function
def theo1(m, k):
    return 2*m*(m+1)/(k*(k+1)*(k+2))

def theo2(m, k):
    return (m/(m+1))**(k-m)/(m+1)

def theo3(m, k):
    return 12*(3*m+3)*(3*m+2)*(3*m+1)*m/((k+2*m+4)*(k+2*m+3)*(k+2*m+2)*(k+2*m+1)*(k+2*m))

#req_index = [411, 504, 743, 958, 1316, 1906]

fig, ax = pl.subplots(nrows = 3, ncols = 2, sharex = True, sharey = True)
fig.text(0.5, 0.04, r"Degree $k$", fontsize = "x-large", ha='center')
fig.text(0.04, 0.5, r"Probability of degree $p(k)$", fontsize = "x-large", va='center', rotation='vertical')

for i, row in enumerate(ax):
    for j, cell in enumerate(row):
        #cell.set_xlim([1, 1.1*1e4])
        #cell.set_ylim([1e-9, 1])
        
        power_current = 2*i + j
        # Load data
        k = np.loadtxt('k_10^%s_%s_sum100_prob3.csv' %(power, 2**power_current)).astype('int64')
        
        # Plot p(k) vs k diagram
        bins = np.arange(min(k) - 1.5, max(k) + 2.5, 1)
        bincentre = bins[:-1] + 0.5
        hist, bin_edges = np.histogram(k, bins = bins, density = True) # density = True returns probability density
        
        # Log-bin the data
        bincentre_bin, hist_bin = lb.logbin(k, scale = a, zeros = False)
        
        
        cell.loglog(bincentre, hist, 'bo', label = r"Unbinned, $m = %d$" %(2**power_current), markersize = 1)
        cell.loglog(bincentre_bin, hist_bin, 'r-', label = r"Binned, $m = %d$" %(2**power_current))
        
        y = theo3(2**power_current, bincentre)
        
        # Reset points of zero probability
        y[0] = 0
    
        # Set initial points p and D as there is no comparison
        pval = [1.]
        Dval = [0.]
        # p-value of each k - taken as the p-value of the line from 1 to k
        for k in range(1, len(hist)):
            D, p = st.ks_2samp(hist[:k], y[:k])
            Dval.append(D)
            pval.append(p)
        
        cell.loglog(bincentre, y, 'k-', label = "Theoretical value")# \n"+r"$D$ = %.3f and" %(Dval[req_index[power_current] - 2**power_current])+"\n"+r"$p$-value = %.5f" %(pval[req_index[power_current] - 2**power_current]))
        
        cell.legend()
        
        pl.figure(2)
        pl.plot(bincentre, pval, '-', label = r"$m$ = %d" %(2**power_current))

#pl.figure(1)
#pl.xlabel(r"Degree $k$", fontsize = "x-large")
#pl.ylabel(r"Probability of degree $p(k)$", fontsize = "x-large")
#pl.figure(2)
#pl.legend()
#pl.xlabel(r"Degree $k$", fontsize = "x-large")
#pl.ylabel(r"$p$-value", fontsize = "x-large")
#pl.xlim(0, 3500)
pl.figure(2)
#pl.grid()
pl.legend()
