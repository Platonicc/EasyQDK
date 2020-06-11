from openQDK import qubit
from openQDK import gates
import numpy as np

print(qubit.state0)
print(qubit.state1)
print(gates.X)
print(gates.H)

print(np.dot(gates.H,qubit.state1))