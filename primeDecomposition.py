def primeFactors(n):
    p = 2 #number that will divide n
    factors = {}
    string = ""
    while n >= p:
        if n%p == 0:
            try: #puts that factor in a dictionary that counts how many times it appears
                factors[p] += 1
            except KeyError:
                factors[p] = 1 
            n //= p
        else:
            p+=1
            
    for keys in factors.keys():
        string += "(" + str(keys)
        if factors[keys] > 1:
            string += "**" + str(factors[keys])
        string += ")"
    return string      

print(primeFactors(86240)) #should return "(2**5)(5)(7**2)(11)"