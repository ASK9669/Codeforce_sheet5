def get_max(arr):
    return max(arr)


def get_min(arr):
    return min(arr)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def count_primes(arr):
    cnt = 0
    for x in arr:
        if is_prime(x):
            cnt += 1
    return cnt


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def count_palindromes(arr):
    cnt = 0
    for x in arr:
        if is_palindrome(x):
            cnt += 1
    return cnt


def count_divisors(n):
    cnt = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1

    return cnt


def max_divisors(arr):
    ans = arr[0]
    mx = count_divisors(arr[0])

    for x in arr:
        divs = count_divisors(x)

        if divs > mx or (divs == mx and x > ans):
            mx = divs
            ans = x

    return ans


# Main
n = int(input())
arr = list(map(int, input().split()))

print("The maximum number :", get_max(arr))
print("The minimum number :", get_min(arr))
print("The number of prime numbers :", count_primes(arr))
print("The number of palindrome numbers :", count_palindromes(arr))
print("The number that has the maximum number of divisors :", max_divisors(arr))
