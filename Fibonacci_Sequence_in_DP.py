# Implemetation Example
def FibonacciDP(n):
    # Setting up a memoization table
    dictFiboncci = {}
    dictFiboncci[0] = 0
    dictFiboncci[1] = 1
    #building up a bigger solutions
    for itr in range(2, n + 1):
        dictFiboncci[itr] = dictFiboncci[itr - 1] + dictFiboncci[itr - 2]
    return dictFiboncci[n]

for i in range(0, 3):
    print("FibonacciDP print: ",FibonacciDP(i))