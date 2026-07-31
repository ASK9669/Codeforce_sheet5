N = int(input())
a = list(map(int, input().split()))
a.sort()
def maximum(b):
    ma = b[-1]
    return (ma)
def minimum(b):
    mi = b[0]
    return (mi)
print(minimum(a),maximum(a))
