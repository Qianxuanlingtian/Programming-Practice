n = 10
def fib(n):
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
        print(num1)

fib(10)