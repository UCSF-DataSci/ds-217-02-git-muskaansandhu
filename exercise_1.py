#Exercise #1: 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get (3, 5, 6, 9). 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000



final_sum = 0 
x = 0 

while x < 1000: 
    if x % 3 == 0 or x % 5 == 0:
        final_sum += x
    x += 1

print(f"The sum of all multiples of 3 or 5 below 100 is:", final_sum)
