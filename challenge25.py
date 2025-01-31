# Wap to print the Fibonacci Series upto n terms
N = int(input("Enter no. of terms"))


def fibonacciNumGen(n):
    series = []
    if n == 1:
        series = [0]
    elif n == 2:
        series = [0, 1]
    else:
        series = [0, 1]
        i = 2
        while i < n:
            series.append(series[-2] + series[-1])
            i += 1
    return series


print(fibonacciNumGen(N))
