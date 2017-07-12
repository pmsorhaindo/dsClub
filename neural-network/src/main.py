import math
import numpy as np

def transfer_function():
    print 'empty'

def activation_function():
   print 'empty'


def cost_function():

    return 1/(2 * total_training_examples)


class Neural_network():
    def __init__(self):
        self.input_layer_size = 2
        self.output_layer_size = 1
        self.hidden_layer_size = 3

        self.weights1 = np.random.rand(self.input_layer_size, self.hidden_layer_size)
        self.weights2 = npm.random.rand(self.hidden_layer_size, self.output_layer_size)


    def sigmoid_function(x):
        return 1 / (1 + math.e**x)

    def forward(self, X):

        self.z2 = np.dot(X, self.weights1)
        self.a2 = np.vectorize(self.sigmoid_function)(z1)
        self.z3 = np.dot(self.a2, self.weights2)
        output = np.vectorize(self.sigmoid_function)(z3)
        return output


test = Neural_network()
result = test.forward()
print 'Result: ' + result
