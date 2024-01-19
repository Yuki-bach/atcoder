N = int(input())
A = list(map(int, input().split()))
remaining = [0] * N

for a in A:
  remaining[a - 1] += 1

print(*[i + 1 for i in range(N) if remaining[i]==3])


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder