"""Collections Script"""
from collections import Counter, defaultdict, OrderedDict, namedtuple
import random
import datetime
import re
import timeit


def pat(patterns):
    """Check for match"""
    text = 'This is a string with term1, but not the other term'
    for pattern in patterns:
        print('Searching for %s in: \n"%s"' % (pattern, text))

        if re.search(pattern, text):
            print("\nMatch was found. \n")
        else:
            print("\nNo Match was found. \n")
    match = re.search(patterns[0], text)
    print(match, match.start(), match.end())


def multi_re_find(patterns, phrase):
    """
    :param patterns: Takes in a list of regex patterns
    :param phrase: Prints a list of all matches
    """
    for pattern in patterns:
        print('Searching the phrase using the re check: %r ' % pattern)
        print(re.findall(pattern, phrase), '\n')


if __name__ == '__main__':
    L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    print(Counter(L))
    S = "Hello World Strings Letters Ass. How many times does each word show up " \
        "in this sentence. Word word shoe up ups. Good day to all of us word counts."
    print(Counter(S))
    WORDS = S.split()
    C = Counter(WORDS)
    print(C, C.most_common(6))
    print(sum(C.values()))
    D = defaultdict(lambda: random.randint(-9999, 9999))
    print(type(D['one']), type(D['two']))
    print(dict(D))

    E = OrderedDict()
    E['a'], E['b'], E['c'], E['d'], E['e'] = (1, 2, 3, 4, 5)
    print(dict(E))
    D1 = OrderedDict()
    D1['a'], D1['b'] = (1, 2)
    D2 = OrderedDict()
    D2['b'] = 2
    D2['a'] = 1
    print(D1 == D2)
    T = (1, 2, 3)
    print(T[0], T[1], T[2])
    DOG = namedtuple("Dog", "age breed name")
    SAM = DOG(age=2, breed='Lab', name="Sammy")
    print('hello \nnewline')

    print(SAM.age, SAM.breed, SAM.name)
    CAT = namedtuple("Cat", "fur claws name")
    C = CAT(fur="Fuzzy", claws=False, name="Kitty")
    print(C[0], C[1], C[2])
    T = datetime.time(5, 25, 1)
    print(T, datetime.time, datetime.time.min)
    print(datetime.time.max, datetime.time.resolution)
    TODAY = datetime.date.today()
    print(TODAY, TODAY.timetuple(), TODAY.day)
    print(datetime.date.min, datetime.date.max, datetime.date.resolution)
    D1 = datetime.date(2015, 3, 11)
    D2 = D1.replace(year=1990)
    print(D1, D2, D1 - D2)
    LINE = "-".join(str(n) for n in range(99))
    TIME = timeit.timeit(LINE, number=999999)
    print(TIME)
    LINE2 = "-".join([str(n) for n in range(99)])
    TIME2 = timeit.timeit(LINE2, number=999999)
    print(TIME2)
    LINE3 = "-".join(map(str, range(99)))
    TIME3 = timeit.timeit(LINE3, number=999999)
    print(TIME3)

    PATTERNS = ['term1', 'term2']
    pat(PATTERNS)
    print(re.search('h', 'w'))
    SPLIT_TERM = '@'
    PHRASE = 'What is your email, is it hello@gmail.com?'
    print(re.split(SPLIT_TERM, PHRASE), 'HELLO WORLD'.split())
    print(re.findall('match', 'Here is one match, here is another match'))
    # noinspection SpellCheckingInspection
    TEST_PHRASE = 'dddsdsdsdsdsdsddsdsdds...sddd...sdsdssdsssdddssdsdsd.sdsdsdsdddsdsd.sd' \
                  '.....dsdsdddsdsddd.....sdsdsdsdsdddsdsssdsdsd....dsdsdddsdsdsdsd' \
                  '.....dsdsdsdsssddsdd....sdsdsddddsdsdssddssdds...dsdsdsdsddsdddsdssdddd'
    TEST_PATTERNS = ['sd*', 'sd+', 'sd?', 'sd{3}', '[sd]', 's[sd]+']
    multi_re_find(TEST_PATTERNS, TEST_PHRASE)
    TEST_PHRASE2 = "This is a string with some numbers 1233 and a symbol #hashtag"
    TEST_PATTERNS2 = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']
    multi_re_find(TEST_PATTERNS2, TEST_PHRASE2)
