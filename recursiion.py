def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def math(n):
    if n < 2:
        return 7
    else:
        return 3 + 2 * math(n - 3)



print("Hello world")