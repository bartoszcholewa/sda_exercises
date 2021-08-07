# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# Best Solution:
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# My solution
def max_sequence(arr):
    if not arr or all(n < 0 for n in arr):
        return 0
    else:
        sum_list = []
        positive_indexes = [i for i, x in enumerate(arr) if x > 0]
        for i in positive_indexes:
            for y in positive_indexes[::-1]:
                s = sum(arr[i:y+1])
                sum_list.append(s)
        return max(sum_list)


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
