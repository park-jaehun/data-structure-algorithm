def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                x[i], x[j] = x[j], x[i]
    return x

print(bubbleSort([1,3,4,668,999]))