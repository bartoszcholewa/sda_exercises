import re
def order(sentence):
    sentence_dict = dict()
    for r in re.finditer(r'(?P<word>[a-zA-Z]*(?P<index>\d)[a-zA-Z]*)', sentence):
        sentence_dict[int(r.group('index')) - 1] = r.group('word')
    return ' '.join([sentence_dict[i] for i in range(0, len(sentence_dict))])

def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

print(order2('4of Fo1r pe6ople g3ood th5e the2'))