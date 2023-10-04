#3.141592653589793

def Leibniz(N):
    y = 0
    for n in range(1, N+1):
        term = 4 / ((-1)**(n+1) * ((2*n)-1))
        y += term
    print(y)
    return y

Leibniz(50000)