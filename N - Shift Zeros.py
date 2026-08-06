def shift_zeros(arr):
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    zeros = len(arr) - len(result)
    result.extend([0] * zeros)

    return result


n = int(input())
arr = list(map(int, input().split()))

print(*shift_zeros(arr))
