<h1 align="center">Python Learning</h1>

<div>
1. Intro to all:
  
```py
1. list = ["apple", "banana", "cherry"]
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

2. tuple = ("apple", "banana", "cherry")
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

3. set = {"apple", "banana", "cherry"}
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

4. dictonary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
```
2. How to take input
  
```py 
  n = int(sys.stdin.readline().strip())
  a = list(map(int, sys.stdin.readline().split()))
  #input:
  # 5
  # 1 2 3 4 5
```
```py
  n = int(input())
  a = [input() for _ in range(n)]
  #This reads n separate lines, each as a string.
  #3
  #1
  #2
  #3
```
</div>

<div>

### Upper and Lower bound
  
```py
import bisect

def lower_bound(arr, x):
    """Returns the index of the first element >= x"""
    return bisect.bisect_left(arr, x)

def upper_bound(arr, x):
    """Returns the index of the first element > x"""
    return bisect.bisect_right(arr, x)

arr = [1, 2, 4, 4, 5, 6]
x = 4
print("Lower Bound of", x, ":", lower_bound(arr, x))  # Output: 2 
print("Upper Bound of", x, ":", upper_bound(arr, x))  # Output: 4 
```
</div>
