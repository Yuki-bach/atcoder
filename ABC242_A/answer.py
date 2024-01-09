A, B, C, X = map(int, input().split())
if (X <= A):
  exit(print(1))
if (A < X <= B):
  exit(print(C / (B - A)))
print(0)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder