import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat
import random as rd


# biases = np.array([2])
# l1inputs = np.array([2,5,7,8])
# l1weights = np.array([0.1,0.2,0.3,0.4]) 
# l2inputs = np.array([np.dot(l1inputs,l1weights), np.dot(l1inputs,l1weights)])
# l2weights = np.array([0.2,0.4])

# l3inputs = np.dot(l2inputs,l2weights) + biases[0]

# print(l2inputs)
# print(l3inputs)

matrix1 = np.array([4,6,8])
matrix2 = np.array([1,2,3])
plt.plot(matrix1, matrix2, "green") #x,y,legend
plt.legend("p")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Predicted Pattern")

#plt.show()

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

    return (2/len(x_values)) * (sum)

def predict_b(m,b):
    sum = 0
    for i in range(0,len(x_values)-1):
        sum += y_values[i] - (m*x_values[i] + b)

    return (-2/len(x_values)) * (sum)


def neural_network(weight,bias):
    weights = np.array([weight,weight,weight,weight])
    
    predicted_y_value_sum = predicted_y_value = np.dot(x_values,weights)+bias
    return 
actual_y_value_sum = 10

epocs = int(input("how many epocs? "))
init_slope = rd.randint(0,10)
init_b = rd.randint(0,10)
b = 100
slope = 100
for _ in range(epocs):
    
    pred_y_sum = neural_network(init_slope,init_b)

    cost = cost_function(init_slope,init_b)
    
    
    print(f"epoc {_+1}, cost = {cost}, slope = {slope}, b = {b}, init_slope = {init_slope}, init_b = {init_b}")
    if b != 0:
        b = predict_b(init_slope,init_b)
    if slope != 1:
        slope = predict_slope(init_slope,init_b)
    if slope == 1 and b == 0:
        break
        print("found it!")
    init_slope = rd.randint(0,10)
    init_b = rd.randint(0,10)
