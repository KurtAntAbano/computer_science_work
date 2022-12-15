def factorial (n):
    if n ==0:
        return 1
    else:
        return (n*factorial(n-1))


def factorial_it(n):
    count = 1
    while n > 1:
        count *= n
        n -= 1
    return count


print(factorial_it(8))
print(factorial(8))
