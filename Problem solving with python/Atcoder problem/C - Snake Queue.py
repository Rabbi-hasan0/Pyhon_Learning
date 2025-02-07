from collections import deque
import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

head = deque()
lngth = deque()
decrease = 0

for _ in range(t):
    type = int(data[index])
    index += 1

    if type == 1:
        lng = int(data[index])
        index += 1
        pre = lngth[-1] if lngth else 0
        headd = head[-1] if head else 0
        if pre + headd != 0:
            head.append(pre + headd)
        lngth.append(lng)

    elif type == 2:
        if head:
            decrease = head.popleft()

    elif type == 3:
        k = int(data[index])
        index += 1
        if k - 2 >= 0 and k - 2 < len(head):
            print(head[k - 2] - decrease)
        else:
            print(0)
