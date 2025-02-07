import sys
from bisect import bisect_right

# def find(a, val):
#     return bisect_right(a, val)
def find(a, val):
    l, r, ans = 0, len(a) - 1, -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= val:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans + 1

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(n):
        half = a[i] // 2
        ans += find(a, half)
    print(ans)

if __name__ == "__main__":
    main()
