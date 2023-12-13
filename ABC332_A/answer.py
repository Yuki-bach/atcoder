N, S, K = map(int, input().split())
ans = 0

for _ in range(N):
  P, Q = map(int, input().split())
  ans += P * Q
  
ans += K if (ans < S) else 0
print(ans)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder