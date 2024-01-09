N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
  if (b in A):
    A.remove(b)
  else:
    exit(print("No"))
print("Yes")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder