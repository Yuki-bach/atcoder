a, b = map(int, input().split())
if (b - a == 1 or (a == 1 and b == 10)):
  print("Yes")
else:
  print("No")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder