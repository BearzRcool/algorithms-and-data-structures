import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat
import random as rd
import time


# biases = np.array([2])
# l1inputs = np.array([2,5,7,8])
# l1weights = np.array([0.1,0.2,0.3,0.4]) 
# l2inputs = np.array([np.dot(l1inputs,l1weights), np.dot(l1inputs,l1weights)])
# l2weights = np.array([0.2,0.4])

# l3inputs = np.dot(l2inputs,l2weights) + biases[0]

# print(l2inputs)
# print(l3inputs)


x_values = np.array([1,2,3,4])
y_values = np.array([1,2,3,4])


def cost_function(m,b):
    sum = 0
    for i in range(len(x_values)):
        sum += (y_values[i] - (m*x_values[i]+b))**2
    
    return (1/len(x_values)) * (sum)

def predict_slope(m,b):
    sum = 0
    for i in range(len(x_values)):
        sum += x_values[i]*(y_values[i] - (m*x_values[i] + b))

    return (-2/len(x_values)) * (sum)

def predict_b(m,b):
    sum = 0
    for i in range(0,len(x_values)-1):
        sum += y_values[i] - (m*x_values[i] + b)

    return (-2/len(x_values)) * (sum)


def neural_network(weight,bias):
    predicted_y_values = []
    for x in x_values:
        predicted_y_values.append((weight*x)+bias)
    return predicted_y_values

epochs = int(input("how many epochs? "))


slopeLowerRange = -10
slopeUpperRange = 10

bLowerRange = -10
bUpperRange = 10

slope = np.random.uniform(slopeLowerRange,slopeUpperRange)
b = np.random.uniform(bLowerRange,bUpperRange)

slopeOffset = 0.1
bOffset = 0.1
learingRate = 0.01



def plot_grid(epoch):
    plt.grid(True)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title(f"Predicted Linear Equation \n Epoch: {epoch}")
    plt.plot(x_values, predicted_y_values)
    plt.plot(x_values, y_values)
    plt.show()
    


for _ in range(epochs):
    slope_gradient = predict_slope(slope,b)
    b_gradient = predict_b(slope,b)

    slope -= learingRate*slope_gradient
    b -= learingRate* b_gradient

    cost = cost_function(slope,b)

    predicted_y_values = neural_network(slope,b)

     
    print(f'''

epoc {_+1}
overall accuracy = {cost}
slope accuracy = {slope}
y intercept accuracy = {b}
slope gradient = {slope_gradient}
b gradient = {b_gradient}
predicted equation = y = {slope}x + {b}
pred y value = {predicted_y_values}
''')
    plot_grid(_+1)
    time.sleep(0.1)