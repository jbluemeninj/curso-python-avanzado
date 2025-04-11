# Fibonacci
def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return  fib_series

if __name__ == "__main__":
    n = int(input("Ingrese el numero de elementos de la serie de Fibonacci: "))
    serie = fibonacci(n)
    for s in serie:
        print(s)

