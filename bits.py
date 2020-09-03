def countBits(n):
    bitList = []
    while n >= 1:
        bitList.append(n%2)
        n = n//2
    return bitList.count(1)
