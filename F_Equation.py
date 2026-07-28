X, N = map(int, input().split())

def Equation(x, n):
    total = 0
    for i in range(2, n + 1, 2):
        total += x ** i
    return total

print(Equation(X, N))