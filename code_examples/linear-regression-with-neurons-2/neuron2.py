import neuron.py


class TwoParameterNeuron(Neuron):
    def __init__(self):
        super().__init__()
        self.parameters = {
            'w': 0,
            'b': 0,
        }
        
    def predict(self, input):
        return self.parameters['w'] * input + self.parameters['b']
    
    def compute_gradient(self, inputs, true_outputs):
        D_w = 0
        D_b = 0
        for idx, input in enumerate(inputs):
            actual = true_outputs[idx]
            prediction = self.predict(input)
            D_w += -2 * (actual - prediction) * input
            D_b += -2 * (actual - prediction)
        D_w /= len(inputs)
        D_b /= len(inputs)
        return D_w, D_b
            
    def gradient_descent(self, inputs, true_outputs, learning_rate):
        D_w, D_b = self.compute_gradient(inputs, true_outputs)
        self.parameters['w'] -= learning_rate * D_w
        self.parameters['b'] -= learning_rate * D_b