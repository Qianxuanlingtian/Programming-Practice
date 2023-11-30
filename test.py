# import pytest
# init = input('请输入需要计算第几项斐波那契数列（需要是一个正整数）：')
# while True:
#     if not init.isalnum():
#         init = input('输入不正确，请重新输入一个正整数：')

def fib(n):
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
    print(num1)

print('结果为：')
# fib(int(init))
fib(10)
