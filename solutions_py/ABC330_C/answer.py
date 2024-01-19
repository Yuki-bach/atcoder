D  = int(input())
ans = 2 * 10**12

for x in range(int(D**0.5) + 1):
  y_squared = D - x**2
  y_floor = int(y_squared**0.5)
  y_ceil = y_floor + 1

  if y_floor**2 == y_squared:
    print(0)
    exit()
  else:
    ans = min(ans, abs(x**2 + y_floor**2 - D), abs(x**2 + y_ceil**2 - D))
print(ans)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder