from neuron import OneParameterNeuron

x = [1, 2, 3]
y = [2, 4, 6]

neuron = OneParameterNeuron()
neuron.train(x, y)

print(f"\nw after training = {neuron.parameters['w']}")