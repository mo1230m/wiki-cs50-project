# Merge sort
def Isort(x):
    for i in range(1, len(x)):
        
        key = i
        j = i-1
        while j >= 0 and x[key] < x[j]:
            temp = x[i] 
            x[i] = x[j]
            x[j] = temp
            j -= 1


  
x = [7, 2, 5, 12, 1, 10, 19, 37, 28]
y = Isort(x)
for i in range(len(y)):
    print(y[i])