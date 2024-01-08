import math

A, B = map(int, input().split())
if A == 0 and B != 0:
  exit(print(0, 1))
if A != 0 and B == 0:
  exit(print(1, 0))
if A == 0 and B == 0:
  exit(print(0, 0))
'''
## find x**2 + y**2 = 1
y = (B / A) * x
x**2 + ((B / A) * x) ** 2 = 1
((B / A) ** 2 + 1) * (x**2) = 1
x**2 = 1 / ((B / A) ** 2 + 1)
'''
x_squared = 1 / ((B / A) ** 2 + 1)
print(math.sqrt(x_squared), math.sqrt(x_squared) * B / A)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder