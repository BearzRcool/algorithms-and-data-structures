
a = [3,2,1]
b = []
c = []
total = 0
def toh(n,start,temp,dest): 
    global total
    total+=1
    if n == 1:
        #print(f"move {n} from {start} to {dest}")
        return
    toh(n-1,start,dest,temp)
    #print(f"move {n} from {start} to {dest}")
    toh(n-1,temp,start,dest)


    
n = 25
toh(n,"a",'b','c')
print(f"total moves = {total}")
print(2**n - 1)
        