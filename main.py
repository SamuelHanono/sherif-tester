# The goal of this function is to return the numbers 1-10, order does not matter, in an array.

def printer():
    arr = []
    for i in range(11):
        arr.append(i)
    return arr
    
def printerNeg():
    arr = []
    for i in range(11):
        arr.append(-i)
    return arr

print(printer())
print(printerNeg())
