import ba
import numpy as np
import time

power = 7

# Number of trials to repeat over
repeat = 100

# Number of vertices - for each time t -> t + 1, add new vertex
N_vertex = 10**power

# Probability mode for adding edges
prob = 2

# Number of edges added per vertex
m = 16

all_k = []

start_time = time.clock()

for i in range(repeat):
    BA = ba.bamodel(prob, m, N_vertex, 0.5)
    while BA.current < N_vertex:
        BA.add_vertex()
    all_k.extend(BA.k)

run_time = time.clock() - start_time

# Store degree distribution k
np.savetxt('k_10^%s_%s_sum%s_prob%s.csv' %(power, m, repeat, prob), all_k, delimiter = ',')
