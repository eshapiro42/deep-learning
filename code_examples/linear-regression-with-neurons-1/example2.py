import numpy as np
from neuron import OneParameterNeuron

np.random.seed(0)

x = (np.random.rand(1000) - .5) * 10
y = 2 * x + np.random.normal(0, 5, x.shape)

neuron = OneParameterNeuron()
neuron.train(x, y)

print(f"\nw after training = {neuron.parameters['w']}")