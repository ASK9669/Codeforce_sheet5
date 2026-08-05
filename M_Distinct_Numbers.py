N = int(input())

def Distinct(arr):
    return len(set(arr))

if N == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    print(Distinct(arr))
