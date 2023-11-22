# Qs 3
import random

t = 3
while t > 0:
    t -= 1
    n = 100
    c = 0
    sam = int(input("Enter sample size: "))

    while n > 0:
        n -= 1
        c1 = 0
        cnot1 = 0
        for i in range(sam):
            ind = random.randint(0, 1000000)
         
            if (ind<520000):
                c1 += 1
            else:
                cnot1 += 1

        if (c1 > cnot1):
            c += 1

    p = c / 100
    print(f"Probability with {sam} samples is {p}")
