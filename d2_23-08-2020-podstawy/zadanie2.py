data = [5,8,2,4,7,9,3]

def bubbleSort(alist):
    length = len(alist)
    for i in range(length):
        first = alist[i]
        second = alist[i + 1]
        if first > second:
            a, b = alist.index(first), alist.index(second)
            alist[b], alist[a] = alist[a], alist[b]
    return data
print(bubbleSort(data))