
import random

def pi_calculator(n):
    number_in = 0
    number_total = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            number_in += 1
        number_total += 1

    return 4 * number_in/number_total
        
print(pi_calculator(100000000))