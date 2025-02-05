n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for a in range(n):
    for b in range(n):
        ok = True
        for i in range(m):
            for j in range(m):
                if a + i >= n or b + j >= n:
                    ok = False
                    break
                if s[a + i][b + j] != t[i][j]:
                    ok = False
                    break
        if ok:
            print(a + 1, b + 1)
            break
