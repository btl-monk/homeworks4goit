print("_____________________________task01________________________________________________________________")

def caching_fibonacci():
    # dictionary for caching results
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        # recursive calculate Fibonacci numbers and save result to cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()

# using the fibonacci function to calculate Fibonacci numbers
print(fib(66))
print(fib(15))