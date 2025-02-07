<h1 align="center">Python Learning</h1>

<div>
1. input a array 
  
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
