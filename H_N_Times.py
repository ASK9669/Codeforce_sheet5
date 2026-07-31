
T = int(input())
def times(n, s):
   
    return (" ".join(n*s))

for i in range(T):
    a, b = input().split()
    a = int(a)

    print(times(a,b))
