N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def arre(X, Y):
    arr = []
    for i in X:
        arr.append(i)
    for i in Y:
        arr.append(i)
    return arr

print(*arre(B ,A))
