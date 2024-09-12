import numpy as np

def unit_step(x):
    return np.where(x > 0, 1, 0)

class Perceptron:
    def __init__(self, lr, itrn=100):
        self.lr = lr
        self.itrn = itrn
        self.activation = unit_step
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        
        # Learning weights
        for _ in range(self.itrn):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation(linear_output)

                # Weight update
                error = self.lr * (y[idx] - y_predicted)
                self.weights += error * x_i
                self.bias += error

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation(linear_output)
        return y_predicted
