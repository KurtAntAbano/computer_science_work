import timeit


def timeMeasure(fun):
    start = timeit.default_timer()
    timefun = fun
    end = timeit.default_timer()
    t = (end -start)*1000000 # time in microseconds. To convert it milliseconds multiply times 1000, and for second multiply by 1
    print("Time of execution is " + str(t)+ " microseconds")