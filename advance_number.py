"""Advanced Numbers"""
import math

if __name__ == '__main__':
    print(hex(12), hex(512))
    print(bin(1234), bin(128), bin(512))
    print(2**4, pow(2, 4, 3))
    print(abs(-3), abs(2))
    print(round(3.9), round(math.pi, 2))

    S = 'hello world'
    S2 = 'hello'
    S3 = 'hhiihhihihihihihihhihihihihihihihihhihihihiihi'
    print(S.capitalize(), S.upper(), S.lower())
    print(S.count('o'), S.find('o'), S.center(20, 'z'))
    print('hello\thi'.expandtabs())
    print(S2.isalnum(), S2.isalpha(), S2.islower(), S2.isspace(), S2.istitle())
    print('HELLO'.isupper(), S2.endswith('o'), S2[-1] == 'o')
    print(S3.split('i'))
    print(S3.partition('i'))

    SE = set()
    SE.add(1)
    SE.add(2)
    SC = SE.copy()
    SE.add(3)
    SE.add(4)
    print(SE, SC, SE.difference(SC))
    S1 = {1, 2, 3}
    S2 = {1, 4, 5}
    S1.difference_update(S2)
    SE.discard(2)
    print(S1, SE)
    S1.add(1)
    S2.add(2)
    S1.intersection_update(S2)
    print(S1.intersection(S2), S1)
    S3 = {5}
    print(S1.isdisjoint(S2), S1.isdisjoint(S3), S1.issubset(S2), S2.issuperset(S1))
    print(S1.symmetric_difference(S2), S1.union(S2))
    S1.update(S2)
    print(S1)

    D = {'k1': 1, 'k2': 2}
    print({k: v**2 for k, v in zip(['a', 'b'], range(2))})
    L = [1, 2, 3, 4]
    X = [1, 2, 3]
    X.extend([4, 5])
    print(L.count(1), L.index(2), X)
    L.insert(2, 'inserted')
    ELE = L.pop()
    print(L, ELE)
    L.remove('inserted')
    L.reverse()
    L.sort()

    print(bin(1024), hex(1024), round(5.23222, 2))
    ST = 'hello how are you Mary, are you feeling okay?'
    ST2 = 'qwertyuiopoiuytrewqwertyuiuytrewqwertyuiopoiuytrewqwertyuioiuytrewq'
    print(ST.islower(), ST2.count('w'))
    SET1 = {2, 3, 1, 5, 6, 8}
    SET2 = {3, 1, 7, 5, 6, 8}
    print(SET1.difference(SET2), SET1.union(SET2))
    print({x: x**3 for x in range(5)})
    L = [1, 2, 3, 4, 2, 5, 1]
    print(L.reverse(), L.sort())
