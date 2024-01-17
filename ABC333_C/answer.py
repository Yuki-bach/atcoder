N = int(input())

ans = set()

for i in range(1,15):
  I = int("1" * i)
  for j in range(1,15):
    J = int("1" * j)
    for k in range(1,15):
      K = int("1" * k)
      ans.add(I + J + K)

ans = sorted(list(ans))
print(ans[N - 1])


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder