def swap(a,b):
    # c = a
    # a = b
    # b = c
    a,b = b,a
    print(a,b)

X , Y = map(int, input().split())
swap(X,Y)