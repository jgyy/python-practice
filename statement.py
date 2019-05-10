
from random import shuffle
from random import randint
hungry = False
loc = 'Auto Shop'
if loc == 'Auto Shop' or hungry:
    print ( "Cars are cool!, FEED ME!" )
elif loc == 'Bank' or not hungry:
    print ( "Money is cool!, I'm not hungry" )
elif loc == 'Store':
    print ( "Welcome to the store!" )
else:
    print ( "I dop not know much." )
my_list = [(11, 12), (21, 22),
           (31, 32), (41, 42)]
list_sum = 0
print(len( my_list ))
for num in my_list:
    if num[0] % 2 == 0:
        print ( f'Even Number: {num[0]}' )
    else:
        print ( f'Odd Number: {num[1] + 1}' )
    list_sum += num[0] + num[1]
print ( list_sum )
for _ in 'Hell':
    print ( 'Hello World!' )
for a, b in my_list:
    print ( a, b )
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items ():
    print ( key, value )
y = 0
while y < 5:
    if y == 2:
        break
    print ( f'The current value of y is {y}' )
    y += 1
else:
    print ( "Y IS NOT LESS THAN 5" )
x = [1, 2, 3]
for item in x:
    pass
print ( 'end of my script' )
my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue
    elif letter == 'y':
        break
    print ( letter )
for num in range ( 0, 10, 2 ):
    print ( f'the current number is {num}' )
print ( list ( range ( 0, 11, 2 ) ) )
word = 'Hey'
for index, letter in enumerate ( word ):
    print ( f'the index is {index}, the letter is {letter}' )
my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = ['a', 'b', 'c']
my_list_3 = [100, 200, 300]
for a, b, c in zip ( my_list_1, my_list_2, my_list_3 ):
    print ( a, b, c )
print ( list ( zip ( my_list_1, my_list_2 ) ) )
print ( 'x' in [1, 2, 3] )
print ( 'x' in ['a', 'x', 'n'] )
print ( 'a' in 'a world ' )
d = {'my key': 345}
print ( 'my key' in d )
print ( 345 in d.keys () )
print ( min ( my_list ), max ( my_list ) )
random_list = shuffle ( my_list )
print ( type ( random_list ) )
print ( my_list )
my_number = randint(0, 100)
print(my_number)
for letter in my_string:
    my_list.append(letter)
print(my_list)
my_list_4 = [x * y for x in range(0, 12) if x % 2 == 0 for y in [1, 10, 1000]]
print("my_list_4 =", my_list_4)
celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit)
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        my_list.append(x * y)
print(my_list)
