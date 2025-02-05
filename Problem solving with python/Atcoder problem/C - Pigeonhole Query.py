def solve():
    n, q = map(int, input().split())
    cnt = {} 
    ind = {}
    for i in range(1, n + 1):
        cnt[i] = 1
        ind[i] = i;

    ans = 0;
    for i in range(q):
        type = list(map(int, input().split()))
        if type[0] == 1:
            p, h = type[1], type[2]
            cur = ind[p] 
            ind[p] = h
            if cnt[cur] != 0:
                if cnt[cur] > 1 and cnt[cur] - 1 <= 1:
                   ans -= 1;
                cnt[cur] -= 1;
            
            if cnt[h] > 1: 
                cnt[h] += 1;
            else:
                cnt[h] += 1
                if cnt[h] > 1:
                   ans += 1;
        else:
            print(ans)

    
def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
