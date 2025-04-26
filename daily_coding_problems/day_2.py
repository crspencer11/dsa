def product_of_array_except_self(arr):
    n = len(arr)
    final = [1] * n
    first = 1
    for i in range(n):
        final[i] =first
        first *= arr[i]

    second = 1
    for i in range(n-1, -1, -1):
        final[i] *= second
        second *= arr[i]
    return final
