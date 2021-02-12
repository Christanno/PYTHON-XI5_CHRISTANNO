Script modul

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result





Script program induk

#import modul
import fibo

#pemanggilan fungsi pertama
print(fibo.fib(100))

#pemanggilan fungsi ke dua
print(fibo.fib2(100))

#pemanggilan fungsi dengan nama lokal
fib = fibo.fib
print(fib(100))


