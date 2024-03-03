# Write a script that finds the sum of all numbers 1-500 that are divisible by
# 3 and 7. Do these two ways. First using a for loop, then using a
# comprehension.

"""for loop"""
for number in range(1, 501):
    #if number%3 == 0 and number%7 == 0:
    if number%21 == 0:
        print(number)

"""comprehension"""
# This is powerful stuff! A first time for me!
lst = [x for x in range(1, 501) if x%21 == 0]
print(lst)
