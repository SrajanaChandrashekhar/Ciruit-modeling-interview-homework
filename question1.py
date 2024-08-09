import numpy as np
import matplotlib.pyplot as plt

N = 100
V_in = np.random.uniform(0, 1, N)
G = np.random.uniform(10e-6, 100e-6, N)


Iout_a = np.sum(V_in * G)
I_ideal = np.sum(V_in * G)

print("Total output current Iout_a:", Iout_a)

Iout_results = []
Iideal_results = []

for _ in range(100):  # Run 100 different tests
    V_in_test = np.random.uniform(0, 1, N)
    G_test = np.random.uniform(10e-6, 100e-6, N)
    I_out_test = np.sum(V_in_test * G_test)
    I_ideal_test = np.sum(V_in_test * G_test)
    Iout_results.append(I_out_test)
    Iideal_results.append(I_ideal_test)

plt.scatter(Iideal_results, Iout_results, color='blue')
plt.xlabel('I_ideal')
plt.ylabel('Iout_a')
plt.title('Scatter plot of Iout_a vs I_ideal')
plt.grid(True)
plt.show()