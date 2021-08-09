""" Policz wystąpienia liter w stringu """
from collections import Counter, defaultdict


def symbol_counter(*strings):
    for word in strings:
        # Using collections.Counter
        counter = dict(Counter(word))
        print(f'A: {word}: {counter}')

        # Using collections.defaultdict
        d = defaultdict(int)
        for letter in word:
            d[letter] += 1
        print(f'B: {word}: {dict(d)}')

        # Using standard python
        dd = dict()
        for letter in word:
            a = dd.get(letter, 0)
            dd[letter] = a + 1
        print(f'C: {word}: {dict(dd)}')
        print('\n')


symbol_counter('barbara', 'rabarbar', 'ananas', 'koloratka', 'abecadło', 'abcabcabc')
