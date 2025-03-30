def fibonacci(i):
    if (i <= 1):
        return i
   else:
    return fibonacci(i - 1) + fibonacci(i - 2)

def oddsum:
    for i in range (10000000):
        sum = 0
        if (fibonacci(i) % 2 != 0):
            sum += fibonacci(i)
        return sum
