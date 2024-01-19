N = int(input())
S, T = zip(*[input().split() for _ in range(N)])

for i in range(N):
  checker1, checker2 = False, False
  for j in range(N):
    checker1 = (i!=j) and (S[i]==T[j] or S[i]==S[j])
    checker2 = (i!=j) and (S[j]==T[i] or T[i]==T[j])
  if (checker1 and checker2):
    exit(print("No"))
print("Yes")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder