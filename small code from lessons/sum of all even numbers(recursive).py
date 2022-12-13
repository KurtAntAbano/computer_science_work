def sum_of_even(n):
    if n == 0:
        return 0
    else:
        print(n)
        if n % 2 == 0:
            return n + sum_of_even(n-2)
        else:
            return n + sum_of_even(n-1)

print(f"the sum of even numbers is {sum_of_even(8)}")
