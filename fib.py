# Conor Smith
# Date: 4/21/21
# Description: Takes a number as the position in Fibonacci sequence and gives value of that position

def fib(num):
    """takes a number that is the position in fibonacci sequence and gives the value of that position"""
    a = 0
    b = 1

    if num == 1:
        return b
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return b
