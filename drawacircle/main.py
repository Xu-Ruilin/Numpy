import numpy as np
import matplotlib.pyplot as plt

nsteps = 0
while nsteps <= 200:
    draws = np.random.randint(0, 100, size=nsteps)
    print(draws)
    nsteps = nsteps + 1
draws.tofile('draws.txt', str(draws))