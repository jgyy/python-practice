
# Statements Assessment Test
Let's test your knowledge!

_____
**Use <code>for</code>, .split(), and <code>if</code> 
to create a Statement that will print out words that start with 's':**


```python
st = 'Print only the words that start with s in this sentence'
```


```python
#Code here
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
```

______
**Use range() to print all the even numbers from 0 to 10.**


```python
#Code Here
list(range(0, 11, 2))
for num in range(0, 11, 2):
    print(num)
```

___
**Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**


```python
#Code in this cell
list_comprehension = [x for x in range(1, 51) if x % 3 == 0]
```

_____
**Go through the string below and if the length of a word is even print "even!"**


```python
st = 'Print every word in this sentence that has an even number of letters'
```


```python
#Code in this cell
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' is even!')
```

____
**Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**


```python
#Code in this cell
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
```

____
**Use List Comprehension to create a list of the first letters of every word in the string below:**


```python
st = 'Create a list of the first letters of every word in this string'
```


```python
#Code in this cell
st = 'Create a list of the first letters of every word in this string'
split_word = [word for word in st.split()]
```

### Great Job!
