# Pyhon_Learning

<div>
# upper and lower bound
  
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
