import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
a = list(map(int, input().split()))

ans = []
tmp_stack = []

for i in range(1, N+1):
  tmp_stack.append(i)
  if i not in a:
    ans += tmp_stack[::-1]
    tmp_stack = []
print(*ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder