N, K = map(int, input().split())
A = list(map(int, input().split()))

if K % 2 == 0:
  ans = 0
  for i in range(0, K - 1, 2):
    ans += A[i + 1] - A[i]
  print(ans)
else:
  p = [0] * ((K + 1) // 2)
  m = 0
  for i in range(1, K, 2):
    m += A[i] - A[i - 1]
    p[(i + 1) // 2] = m
  m = 0
  for i in range(K-2, 0, -2):
    m += A[i + 1] - A[i]
    p[(i - 1) // 2] += m
  ans = min(p)
  print(ans)





## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder