def memoize(f):
    '''Memoizes the fibonacci function, stores already calculated values and looks them up for time-space tradeoff'''
    cached = {}
    def lookup(x):
        '''Checks if a value has already been computed, else it calls fib to calculate that value''' 
        if x not in cached:
            cached[x] = f(x)
        return cached[x] #looks up the value in the dict and returns it
    return lookup 

@memoize #func wrapper memoized, fib = memoize(fib) 
def fibonacci(n):
    '''Computes a fibonacci number recursively, but only if the value hasn't been memoized, else looks it up in constant time'''
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)