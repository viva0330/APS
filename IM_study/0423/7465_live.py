def find_set(n):
    while n != p[n]:
        n = p[n]
    return n