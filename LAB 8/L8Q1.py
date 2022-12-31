fib1 = 1
fib2 = 2
sum = 0
fib3 = fib1 + fib2
while (fib3 < 4000000):
    if (fib3 % 2 == 0):
        sum = sum + fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
print("The sum of even fibonacci numbers below 4 million is: {}".format(sum))
