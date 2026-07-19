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
y_values = np.array([2,4,6,8])


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

epocs = int(input("how many epocs? "))


slopeLowerRange = -10
slopeUpperRange = 10

bLowerRange = -10
bUpperRange = 10

slope = np.random.uniform(slopeLowerRange,slopeUpperRange)
b = np.random.uniform(bLowerRange,bUpperRange)

slopeOffset = 0.1
bOffset = 0.1
learingRate = 0.01


#x = np.linespace(-5,5,20)
#y = (init_slope)*x+init_b

#plt.plot(x,y, color = "green") #x,y,legend
plt.legend("p")
plt.grid(True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Predicted Pattern")

#plt.show()



for _ in range(epocs):
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
    
    

    # y = init_slope*x + init_b

    # time.sleep(5)
