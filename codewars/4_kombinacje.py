from itertools import permutations as p
def permutations(string):
    return [''.join(x) for x in set(p(string))]



print(sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(sorted(permutations('aabb')))