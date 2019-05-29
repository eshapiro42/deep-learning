import time
from abc import abstractmethod


class Neuron:
    def __init__(self):
        self.total_epochs = 0
        self.parameters = {}
        
    @abstractmethod
    def predict(self, input):
        pass
    
    @abstractmethod
    def compute_gradient(self, inputs, true_outputs):
        pass
            
    @abstractmethod
    def gradient_descent(self, inputs, true_outputs, learning_rate):
        pass
    
    def loss(self, actual, prediction):
        return (actual - prediction)**2
        
    def cost(self, inputs, true_outputs):
        sum_of_losses = 0
        for idx, input in enumerate(inputs):
            prediction = self.predict(input)
            actual = true_outputs[idx]
            sum_of_losses += self.loss(actual, prediction)
        return sum_of_losses / len(inputs)
    
    def train(self, inputs, true_outputs, epochs=100, learning_rate=0.01):
        start = time.time()
        for epoch in range(epochs):
            self.gradient_descent(inputs, true_outputs, learning_rate)
            if epoch == 0 or (epoch + 1) % 10 == 0 or epoch == epochs - 1:
                end = time.time()
                cost = self.cost(inputs, true_outputs)
                print(f'Epoch: {self.total_epochs + 1:<10} Cost = {cost:<20.9E} Time = {1000 * (end - start):.9f}ms')
                start = time.time()
            self.total_epochs += 1
            
            
class OneParameterNeuron(Neuron):
    def __init__(self):
        super().__init__()
        self.parameters = {'w': 0}
        
    def predict(self, input):
        return self.parameters['w'] * input
    
    def compute_gradient(self, inputs, true_outputs):
        D_w = 0
        for idx, input in enumerate(inputs):
            actual = true_outputs[idx]
            prediction = self.predict(input)
            D_w += -2 * (actual - prediction) * input
        D_w /= len(inputs)
        return D_w
            
    def gradient_descent(self, inputs, true_outputs, learning_rate):
        gradient = self.compute_gradient(inputs, true_outputs)
        self.parameters['w'] -= learning_rate * gradient