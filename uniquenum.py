def dig_pow(n, p):
    digSum = 0
    digitList = list(str(n))
    k = 1
    for digits in digitList:
        digSum += int(digits)**p
        p+=1

    while n*k <= digSum:
        if digSum == n*k:
            return k
        k+=1
    return -1