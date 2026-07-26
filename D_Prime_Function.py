# def prime(a):
#     c = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             c += 1
#     if c == 2:
#         print("YES")
#     else:
#         print("NO")
# T = int(input())
# for t in range(T):
#     N = int(input())
#     prime(N)
import math

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    print("YES" if prime(n) else "NO")