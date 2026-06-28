import numpy as np
import matplotlib.pyplot as plt
print(np.__version__)
# print(plt.__version__)

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



plt.show()

