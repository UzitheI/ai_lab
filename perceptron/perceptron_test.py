import numpy as np
from sklearn.model_selection import train_test_split
from perceptron import Perceptron

def accuracy(y_true, y_predicted):
    return np.sum(y_true == y_predicted) / len(y_true)

# Define dataset
X = [0.21, 0.52, 0.92, 0.36, 0.55, 0.45, 0.34, 0.67, 0.04, 0.77]
y = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
X = np.array([[x] for x in X])
y = np.array(y)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

print("*" * 100)
print("X_test:")
print(X_test)
print("y_test:")
print(y_test)
print("X_train:")
print(X_train)
print("*" * 100)

# Initialize and train Perceptron
p = Perceptron(lr=0.01, itrn=1000)
p.fit(X_train, y_train)

# Make predictions
prediction = p.predict(X_test)
print("Predictions:")
print(prediction)
print("Accuracy:", accuracy(y_test, prediction))

# Predict on new data
new_data = np.array([[0.31], [0.88]])
new_prediction = p.predict(new_data)
print("New Predictions:")
print(new_prediction)
