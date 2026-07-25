N = int(input())

def is_odd(n):
    return n % 2 == 1

def is_palindrome_binary(n):
    binary = bin(n)[2:]     
    return binary == binary[::-1]

if is_odd(N) and is_palindrome_binary(N):
    print("YES")
else:
    print("NO")