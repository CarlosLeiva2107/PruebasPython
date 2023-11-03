import itertools

def zeroSubsequences(arr, n):
    c = 0
    for i in range(1, len(arr) + 1):
        for j in itertools.combinations(arr, i):
            print(j)
            if len(j) and min(j) * max(j) == 0:
                    c += 1

    return c


zeroSubsequences([1,0,-2,3], 3)
