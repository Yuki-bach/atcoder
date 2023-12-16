N = int(input())
A = list(map(int, input().split()))
counter = {i: 0 for i in range(1, N + 1)}

for a in A:
  counter[a] += 1
  if counter[a] == 2:
    print(a, end=" ")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder