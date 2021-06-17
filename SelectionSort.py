def swap(x, i, j):
    x[i], x[j] = x[j], x[i]
    return x
def selectionSort(x):
    for size  in reversed(range(len(x))):
        max_i = 0
        for i in range(1, size + 1):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)
    return x

print(selectionSort([56,5,78,57,34]))
