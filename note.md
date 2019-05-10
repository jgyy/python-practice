#
# Objects and Data Structures Assessment Test

## Test your knowledge. 

** Answer the following questions **

Write a brief description of all the following Object Types and Data Structures we've learned about: 

Numbers: Store numerical information such as integers and floating point.

Strings: Ordered sequence of characters

Lists: Order sequence of objects (mutable)

Tuples: Ordered sequence of objects (immutable)

Dictionaries: Key-Value pairing that is unordered


## Numbers

Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


```python
(60 + (10 ** 2) / 4 * 7) - 134.75
```

Answer these 3 questions without typing code. Then type code to check your answer.

    What is the value of the expression 4 * (6 + 5)
    
    What is the value of the expression 4 * 6 + 5 
    
    What is the value of the expression 4 + 6 * 5 


```python
forty_four = 4 * (6 + 5)
twenty_nine = 4 * 6 + 5
thirty_four = 4 + 6 * 5
```

What is the *type* of the result of the expression 3 + 1.5 + 4?<br>

Answer: Floating Point Number

What would you use to find a number’s square root, as well as its square? 


```python
# Square root:
square_root = 100 ** 0.5
```


```python
# Square:
square = 100 ** 2
```

## Strings

Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:


```python
s = 'hello'
# Print out 'e' using indexing

e = s[1]
```

Reverse the string 'hello' using slicing:


```python
s ='hello'
# Reverse the string using slicing

hello_reversed = s[::-1]
```

Given the string hello, give two methods of producing the letter 'o' using indexing.


```python
s ='hello'
# Print out the 'o'

# Method 1:

o = s[-1]
```


```python
s ='hello'
# Method 2:

o = s[4]
```

## Lists

Build this list [0,0,0] two separate ways.


```python
# Method 1:
ooo = [0]*3
```


```python
# Method 2:
list_2 = [0, 0, 0]
```

Reassign 'hello' in this nested list to say 'goodbye' instead:


```python
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

```

Sort the list below:


```python
list4 = [5,3,4,6,1]
sorted(list4)
list4.sort()
```

## Dictionaries

Using keys and indexing, grab the 'hello' from the following dictionaries:


```python
d = {'simple_key':'hello'}
# Grab 'hello'
hello = d['simple_key']
```


```python
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
hello = d['k1']['k2']
```


```python
# Getting a little tricky
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
hello = d['k1'][0]['nest_key'][1][0]
```


```python
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
hello = d['k1'][2]['k2'][1]['tough'][2][0]
```

Can you sort a dictionary? Why or why not?<br>

Answer: No, because normal dictionaries are mapping and not a sequence.

## Tuples

What is the major difference between tuples and lists?<br>

Tuples are immutable.

How do you create a tuple?<br>

t = (1, 2, 3)

## Sets 

What is unique about a set?<br>

Answer: They don't allow for duplicate items!

Use a set to find the unique values of the list below:


```python
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)


```

## Booleans

For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>==</td>
<td>If the values of two operands are equal, then the condition becomes true.</td>
<td> (a == b) is not true.</td>
</tr>
<tr>
<td>!=</td>
<td>If values of two operands are not equal, then condition becomes true.</td>
<td> (a != b) is true.</td>
</tr>
<tr>
<td>&gt;</td>
<td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
<td> (a &gt; b) is not true.</td>
</tr>
<tr>
<td>&lt;</td>
<td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
<td> (a &lt; b) is true.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>If the value of left operand is greater than or equal to the value of right operand, 
then condition becomes true.</td>
<td> (a &gt;= b) is not true. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &lt;= b) is true. </td>
</tr>
</table>

What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)


```python
# Answer before running cell
false = 2 > 3
```


```python
# Answer before running cell
false = 3 <= 2
```


```python
# Answer before running cell
false = 3 == 2.0
```


```python
# Answer before running cell
true = 3.0 == 3
```


```python
# Answer before running cell
false = 4**0.5 != 2
```

Final Question: What is the boolean output of the cell block below?


```python
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
false = l_one[2][0] >= l_two[2]['k1']
```

## Great Job on your first assessment! 
