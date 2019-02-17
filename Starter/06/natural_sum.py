def nsum(n, m):
    if m == n:
        return m
    else:
        return m + nsum(n, m - 1)

print(nsum(3, 6))

    
