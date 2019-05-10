
my_taxes = 555 * 0.09
my_string = "Hello World Everyone"
last_letters = "JEff"[1:]
result = 100.000/777.000
my_dict = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
d = {'k1': ['a', 'b', 'c'], 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
my_list = d['k1']
letter = my_list[2].upper()
d['k4'] = 400
t = ('zero', 1, 1, 2, 3)
my_set = {1, 2}
my_set.add(3)
b = None
# Default is to read
with open('my_new_file.txt') as f:
    print(f.read())
with open('my_new_file.txt', mode='a') as f:
    f.write('\nNEXT UPON NEXT')
    f.close()
print(b, 1 > 2, 1 == 1, my_set)
print(type(t), type(False))
print(t.count(1), t.index(1))
print(my_dict['apple'])
print(my_list)
print(d['k2'][2])
print(d.keys(), d.values(), d.items())
print("A" + last_letters * 2)
print(my_taxes, result)
print("The result was {r:1.9f}".format(r=result))
print('Hello, his name is {name} and he is {age} years old'.format(name="Jeff", age=3))
print(my_string + ", how do you do?")
print('This is a string {2} {0} {0}'.format('INSERTED', 'fox', 'brown'))
print('This {f} {b} {i}'.format(i='INSERTED', f='fox', b='brown'))
print(my_string.upper().split('l'))
print(my_string[:-2], my_string[2:8], my_string[::-2])
print( "hello \nworld \t2'2" )
my_list = [1, 2, 3, 'STRING', 23.2]
another_list = ['four', 'five']
print(len(my_list))
print(my_list[1:] + another_list)
another_list.append('six')
another_list[0] = 'zero'
new_list = [1, 22, 3, 4, 5, 6, 7, 8, 'nine']
popped_item = new_list.pop()
print(another_list, popped_item)
print(type(new_list.sort()))
new_list.reverse()
print(new_list)
print('2' + '5')
print(7 % 4)
print(0.1 + 0.2 - 0.3)
print(2 == 2, 2 == 1, 'hello' == 'bye', 'Bye' == 'bye')
print('2' == 2, 2.0 == 2, 3 != 3, 4 != 5, 2 > 1, 1 > 2, 2 < 5)
print(1 < 2 < 3, 1 < 2 > 3, 'h' == 'h' and 2 == 2, 100 == 1 or 2 == 20)
print(1 == 1, not 1 == 1, not 400 > 5000)
