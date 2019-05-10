"""Collections Script"""
from collections import Counter, defaultdict, OrderedDict
import random

L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
print(Counter(L))
S = "Hello World Strings Letters Ass. How many times does each word show up "\
    "in this sentence. Word word shoe up ups. Good day to all of us word counts."
print(Counter(S))
WORDS = S.split()
C = Counter(WORDS)
print(C)
print(C.most_common(6))
print(sum(C.values()))
D = defaultdict(lambda: random.randint(-9999, 9999))
print(type(D['one']), type(D['two']))
print(dict(D))
E = OrderedDict()
E['a'] = 1
E['b'] = 2
E['c'] = 3
E['d'] = 4
E['e'] = 5
print(dict(E))
D1 = OrderedDict()
D1['a'] = 1
D1['b'] = 2
D2 = OrderedDict()
D2['b'] = 2
D2['a'] = 1
print(D1 == D2)
