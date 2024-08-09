import numpy as np
import matplotlib.pyplot as plt


N = 100
R_wire = 10
G_wire = 1 / R_wire


def calculate_Iout_b(V_in, G, R_wire):
    Iout_b = np.sum(V_in * G / (1 + G * R_wire))
    return Iout_b


V_in = np.random.uniform(0, 1, N)
G = np.random.uniform(10e-6, 100e-6, N)


Iout_b = calculate_Iout_b(V_in, G, R_wire)


I_ideal = np.sum(V_in * G)


Iout_results = []
Iideal_results = []

print("Total output current Iout_b:", Iout_b)

for _ in range(100):
    V_in_test = np.random.uniform(0, 1, N)
    G_test = np.random.uniform(10e-6, 100e-6, N)
    I_out_test = calculate_Iout_b(V_in_test, G_test, R_wire)
    I_ideal_test = np.sum(V_in_test * G_test)
    Iout_results.append(I_out_test)
    Iideal_results.append(I_ideal_test)


plt.scatter(Iideal_results, Iout_results, color='blue')
plt.xlabel('I_ideal')
plt.ylabel('I_out_b')
plt.title('Scatter plot of I_out_b vs I_ideal')
plt.grid(True)
plt.show()