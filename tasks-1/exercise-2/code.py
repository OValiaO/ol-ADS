def reverseList(arr, n, m):
    
    while n < m:
        arr[n], arr[m] = arr[m], arr[n]
        n += 1
        m -= 1

    return arr