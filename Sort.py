def swap(x, i, j):
    x[i], x[j] = x[j], x[i]
    return x

# BubbleSort implemention
def bubbleSort(x):
    for size in reversed(range(len(x))):
        for idx in range(size):
            if x[idx] > x[idx+1]:
                x[idx], x[idx + 1] = x[idx +1], x[idx]
    return x

# SelectionSort implemention
def selectionSort(x):
    for size  in reversed(range(len(x))):
        max_i = 0
        for i in range(1, size + 1):
            if x[i] > x[max_i]:
                max_i = i
        swap(x, max_i, size)
    return x

# MergeSort implemention
def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid],x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0,0,0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i +=1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    return x

print(mergeSort([12,34,45,11,23,24]))
print(bubbleSort([12,34,45,11,23,24]))
print(selectionSort([12,34,45,11,23,24]))
