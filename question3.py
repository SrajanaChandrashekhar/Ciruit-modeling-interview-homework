import numpy as np
import matplotlib.pyplot as plt

N = 100
R_wire = 10
G_wire = 1 / R_wire
V_offset = 0.05


def calculate_Iout_c(V_in, G, R_wire, V_offset):
    Iout_c = np.sum((V_in[:, 1] - V_offset) * G[:, 1] / (1 + G[:, 1] * R_wire))
    return Iout_c


V_in = np.random.uniform(0, 1, (N, 2))
G = np.random.uniform(10e-6, 100e-6, (N, 2))


Iout_c = calculate_Iout_c(V_in, G, R_wire, V_offset)


I_ideal = np.sum(V_in[:, 1] * G[:, 1])

print("Total output current Iout_c:", Iout_c)

Iout_results = []
Iideal_results = []

for _ in range(100):
    V_in_test = np.random.uniform(0, 1, (N, 2))
    G_test = np.random.uniform(10e-6, 100e-6, (N, 2))
    I_out_test = calculate_Iout_c(V_in_test, G_test, R_wire, V_offset)
    I_ideal_test = np.sum(V_in_test[:, 1] * G_test[:, 1])
    Iout_results.append(I_out_test)
    Iideal_results.append(I_ideal_test)


plt.scatter(Iideal_results, Iout_results, color='blue')
plt.xlabel('I_ideal')
plt.ylabel('Iout_c')
plt.title('Scatter plot of I_out_c vs I_ideal')
plt.grid(True)
plt.show()