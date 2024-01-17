N = int(input())
if (N == 1): exit(print(0))

def convert_to_base_5(n):
  digits = []
  while n > 0:
    digits.append(n % 5)
    n = n // 5
  digits.reverse()
  return digits

base_5 = convert_to_base_5(N-1)
for x in base_5:
  print(x * 2, end="")



## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder