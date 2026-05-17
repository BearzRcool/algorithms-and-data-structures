# is Empty() - checks if it is Empty
# ---pop() - removes the last thing you put in (lifo)
# ---push() - adds thing to the top
# ---peek() - checks what is at the top
# ---size() - checks how many things are in the stack
class Stack(list):
    def __init__(self,list):
        self.list = list
    
    def empty(self):
        if len(self.list) == 0:
            return True
        
        return False
    def pop(self):
        if len(self.list) != 0:
            a = self.list[len(self.list)-1]
            self.list.pop()
            return "Removed " + str(a) + ". "
        else:
            return "The list is empty. "
    def push(self, item):
        self.list.append(item)
        return "Added " + str(item) + ". "
    def peek(self):
        if len(self.list) != 0:
            return self.list[len(self.list)-1]
        else:
            return "The list is empty. "
    def size(self):
        return len(self.list)
stack = Stack([1,2,3,4,5])
# while True:
#     question = input("size, empty, pop, push, or peek. ")
#     if "size" in question:    
#         print(stack.size())
#     elif "empty" in question:
#         print(stack.empty())
#     elif "pop" in question:
#         print(stack.pop())
#     elif "push" in question:
#         item = input("what are you adding (number) ")
#         print(stack.push(item))
        
#     elif "peek" in question:
#         print(stack.peek())
#     else: 
#         print("try agian")
        
class Node:
    def __init__(self, n=[], p=None, data=None):
        self.data = data
        self.n = n
        self.p = p

    def __repr__(self):
        print(f"This Node {self.data} has {self.n} forward and {self.p} backwards")

class Tree:
    def __init__(self, root, nodes):
        self.root = root
        self.nodes = nodes



NodeB = Node(data="B")
NodeC = Node(data="C")
rootNode = Node([NodeB,NodeC], data = "A")