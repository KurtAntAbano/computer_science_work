def Nilakanthas(N):
    y = 0
    for n in range(1, N+1):
        term = (-1)**(n+1) * (4/ ((2*n)*(2*n+1)* (2*n+2)))
        y += term
    print(y+ 3)
    return (y + 3)

Nilakanthas(50000)


def compare():
    import math
    pi = math.pi
    print(pi)
    difference = pi - Nilakanthas(50000)
    print("the difference is ", difference)

compare()
