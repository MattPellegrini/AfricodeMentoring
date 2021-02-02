# Function Challenges
Try to write small python functions to the problems below.

## Challenge 1
```
def dice_rolls(dice_1: int, dice_2:int) -> None:
    # Complete this function that prints the sum of the two dice rolls.
    # Also, if the roll is a double (both dice are the same number), print another line to say "Double!"
    ...


# Example 1
# INPUT: dice_rolls(4, 1)
# OUTPUT: "The total is 5."

# Example 2
# INPUT: dice_rolls(3, 3)
# OUTPUT: "The total is 6."
#         "Double!"
```

## Challenge 2
Write a function that takes a shopping list, and a single item and print either, "Item is on the list" or "Item is not on the list".
The types are as follows: the shopping list should be a list of strings, the item should be a string.
```
# Example 1
# INPUT: check_item_on_list(["Apples", "Oranges", "Bread"], "Cookies")
# OUTPUT: "Item is not on the list."

# Example 2
# INPUT: check_item_on_list(["Carrots", "Pineapple", "Peppers"], "Carrots")
# OUTPUT: "Item is on the list."
```
## Challenge 3 - List comprehensions.
List comprehensions are a really quick and useful tool in python. A list comprehension is a way to define a list from other data. For example:
```python
list_1 = [1,2,3,4,5]
list_2 = [x+1 for x in list_1]
```
`list_2` will be `[2,3,4,5,6]`

List comprehensions can also use `if` conditions. For example:
```python
list_1 = [1,2,3,4,5]
list_2 = [x for x in list_1 if x > 3]
```
This time `list_2` will be `[4,5]`

**Use list comprehensions to write the following functions:**
```python
def odds(list: List[int]) -> List[int]:
  """Returns a list of all the odd numbers in the provided list."""
  ...

def squares(list: List[int]) -> List[int]:
  """Returns a list of all the squares numbers in the provided list."""
  ...
  
def vowels(phrase: str) -> List[str]:
  """Returns a list of all the vowels of the given words."""
  ...
```

#### Example input and output
```
In : odds([1,2,11,12,13,21,89,117,120])
Out: [1,11,13,21,89,117]

In : squares([1,2,3,4,5,6,7,8,9,10)
Out: [1, 4, 9, 16, 25, 36, 49, 64, 89, 100]

In : last_characters("I have a dream.")
Out: ['I', 'a', 'e', 'a', 'e', 'a']
```

#### Tips:
1. Remember strings can be treated as Lists of characters in python. Try the list comprehension treating the string as a list.
2. In english, vowels are 'a', 'e', 'i' 'o' and 'u'. Remember you can use `in [...]` to check if a value is in a list.


## Challenge 4
Write a function that will make an [Acronym](https://en.wikipedia.org/wiki/Acronym) from a string. An acronym is an abbreviation of the first letter of the words such as N.A.S.A for National Aeronautics and Space Administration or W.H.O for "World Health Organisation".

The function should look like this:
```python
def make_acronym(phrase: str) -> str:
  ...
```
#### Example input and output
```
In : make_acronym("World Health Organisation")
Out: 'W.H.O'

In : make_acronym("Southern African Development Community")
Out: 'S.A.D.C'
```

#### Tips:
1. Remember that you can index strings just like arrays in python `"hello"[4]` will return `'o'`
2. Look at the `join` function in python (https://www.geeksforgeeks.org/join-function-python/) to join the characters with a dot.
3. For-loops, or 'list comprehensions' might help iterate over the words in the phrase.
4. (BONUS) Try using the isupper() and islower() methods to make sure `National Aeronautics and Space Administration` becomes `N.A.S.A` and not `N.A.a.S.A`.


## Challenge 5
Write a function that performs a [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).
This is a weak form on encryption, but fun to play around with. We'll limit it to only the upper-case characters, and we won't use any spaces.

#### Some background:
Every ASCII character has an integer representation (http://www.asciitable.com/). The integer for 'A' is 65 and the integer for 'Z' is 90.
In python, you can find this integer using the `ord()` function.

For example:
```
In : ord('A')
Out: 65

In : ord('B')
Out: 66
...
In : ord('Z')
Out: 90
```

The opposite of this function is the `chr()` function. `chr()` takes an integer and returns the character that is represented by that integer.
For example:
```
In : chr(65)
Out: 'A'

In : ord(66)
Out: 'B'
...
In : chr(90)
Out: 'Z'
```

The Caesar Cipher works by shifting each of the characters a certain number of steps, making sure to loop back to A from Z.
For example, shifting 2 steps, A becomes C, B becomes D and so on. We have to be careful by the end of the sequence to loop back to the start. Y should become A, and Z should become B.

#### The challenge:
Write a function, that takes a message (in all CAPS, without spaces) and the number of steps to shift the message as an integer. Return the shifted message.
```python
def shift(message: str, steps: int) -> str:
  ...
```

#### Example input and output
```
In : shift("THEFOXWASQUICK", 10)
Out: 'DROPYHGKCAESMU'

In : shift("HELLOWORLD", 1)
Out: 'IFMMPXPSME'

In : shift("NOTHINGCHANGES", 0)
Out: 'NOTHINGCHANGES'
```   





