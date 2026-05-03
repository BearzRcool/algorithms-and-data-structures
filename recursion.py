#call stack\
# - data satructure that stores all the commands/instructions that the cpu will do for a program (like a tall tower full of commands)

def recurstion_sum(values):
    if len(values) == 0:
        return 0
    value = values[len(values)-1]
    values.pop()
    return recurstion_sum(values) + value

values = [1,2,3,4,5]
length = len(values)
#print(recurstion_sum(values)//length)

sequence = []

def fib(n): #n = numbers of fib sequence to return
    global sequence
    if n == 0:
        return 0
    if len(sequence) <= 1:
        sequence.append(1)
        return fib(n)
    
    a = sequence[len(sequence)-1]#last
    b = sequence[len(sequence)-2]#1 before last

    c = a+b
    sequence.append(c)
    n-=1
    return fib(n) 

#fib(20)
#print(sequence)


def fact(n):
    if n == 0:
        return 1
    number = n
    n-=1
    return fact(n) * number
        
#print(fact(5))
    

def harmonic(n):
    if n == 0:
        return 0
    number = 1/n
    n-=1
    return harmonic(n) + number

#print(harmonic(6))


tower1 = [3,2,1]
tower2 = []
tower3 = []
towers = [tower1,tower2,tower3]
def TOHanoi(towers):
    if towers[2] == [3,2,1]:
        return towers
    if tower3[len(tower3)-1] < disk:
        return towers
    
