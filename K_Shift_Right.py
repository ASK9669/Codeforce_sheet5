N, X = map(int, input().split())

def shift_right(arr):
    x = arr.pop()
    arr.insert(0, x)
    return arr

arr = list(map(int, input().split()))

for i in range(X):
    arr = shift_right(arr)

print(*arr)
