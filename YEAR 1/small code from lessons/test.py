def sum_function(N):
    y = 0
    for n in range(0, N+1):
        y += n
    print(y)
    return y

# sum_function(6)


def sum_odd_function(N):
    y = 0
    for n in range(1, N+1):
        y += ((2*n)-1)
    print(y)
    return y

# sum_odd_function(6)

def sum_odd_sign_function(N):
    y = 0
    for n in range(1, N+1):
        y += ((-1)**(n+1) * ((2*n)-1))
        #((-1)**(n+1) switches the sign
    print(y)
    return y

#sum_odd_sign_function(6)


def sum_odd_fraction_function(N):
    y = 0
    for n in range(1, N+1):
        y += (1/((2*n)-1))
        #(1/((2*n)-1)) this adds fraction of odd numbers
    print(y)
    return y

#sum_odd_fraction_function(6)


def sum_evenfraction_function(N):
    y = 0
    for n in range(1, N+1):
        y += (1/((2*n)))
    print(y + 1)
    return y + 1
#this return sum of even number fracion (1/2, 1/4, 1/6) then adds 1 at the end

#sum_evenfraction_function(6)

def multiplication_fraction_function(N):
    y = 1
    for n in range(1, N+1):
        term = (1/(2*n))
        y *= term
    print(y)
    return y

multiplication_fraction_function(4)





