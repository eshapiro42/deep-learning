import numpy as np
from neuron2 import TwoParameterNeuron

np.random.seed(1)

x = (np.random.rand(1000) - .5) * 10
y = -2 * x + np.random.normal(0, 2, x.shape) + 5

neuron = TwoParameterNeuron()
neuron.train(x, y, epochs=1000)

print(f"\nw after training = {neuron.parameters['w']}")
print(f"b after training = {neuron.parameters['b']}")