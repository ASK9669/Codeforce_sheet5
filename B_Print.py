N = int(input())

def numbers(b):
    for i in range(1, b + 1):
        if i > 1:
            print(" ", end="")
        print(i, end="")

numbers(N)