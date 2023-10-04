
def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)

def fib2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers,now append the sum of the two previous numbers to the list
    for i in range(1, n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

print(fib(5))
print(fib2(5))