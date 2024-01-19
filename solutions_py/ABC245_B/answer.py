N = input()
A = list(map(int, input().split()))

for i in range(2002):
  if i not in A:
    exit(print(i))

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder