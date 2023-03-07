#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:b} is postive")
elif number == 0:
    print("f{number:b} is zero")
else:
    print(f"{number:b} is negative")
