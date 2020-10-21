from functools import reduce
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b): #euclid
    return (a*b)//gcd(a,b)

def convertFracts(lst): #lcm can be computed by iteratively computing the lcm of the current value and the next element of the list
    lcd = reduce(lcm, [elem[1] for elem in lst]) #least common denom
    for i in range(len(lst)):
        lst[i][0] = lst[i][0]*(lcd//lst[i][1]) #numerator, ex. 1/2 = 1*(12/2) / 12
        lst[i][1] = lcd
    return lst
    
a = [[1, 2], [1, 3], [1, 4]]
print(convertFracts(a))