def Maxsum(b,c):
    msum = 0
    csum = 0
    j = 0
    for i in range(len(c)):
        csum += c[i]

        while csum > b:
            csum -= c[j]
            j += 1

        msum = max(msum, csum)
    return msum

n=int(input())
c = list(map(int, input().split()))
print(Maxsum(n,c))