def average(n, arr):
    return sum(arr) / n

n = int(input())
arr = list(map(float, input().split()))

print(f"{average(n, arr):.7f}")
