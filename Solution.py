import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

if n == 1:
    print(a[0] + 1)
    sys.exit(0)

def divn(d):
    return sum(num%d == 0 for num in a)

def gcd(a, b):
    if min(a,b) == 0:
        return max(a, b)
    return gcd(b, a%b)

g = a[0]
for i in range(n):
    g = gcd(g, a[i])
for i in range(n):
    a[i] //= g
res = g
    
culprit = -1
g = a[0]
for i in range(n):
    g = gcd(g, a[i])
    if g == 1:
        culprit = i
        break
g = a[0 if culprit else 1]
for i in range(n):
    if i != culprit:
        g = gcd(g, a[i])
print(res * g)
