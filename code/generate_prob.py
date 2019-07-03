import ba
import numpy as np
import time
import matplotlib.pyplot as pl

#import pandas

power = 7

# Number of vertices - for each time t -> t + 1, add new vertex
N_vertex = 10**power

# Probability mode for adding edges
prob = 1 # Pure preferential attachment

# Number of edges added per vertex
m = 6

# Set up graph G0
BA = ba.bamodel(prob, m, N_vertex)

start_time = time.clock()
while BA.current < N_vertex:
    BA.add_vertex()
run_time = time.clock() - start_time

# Store degree distribution k
np.savetxt('k_10^%s_%s.csv' %(power, m), BA.k, delimiter = ',')
