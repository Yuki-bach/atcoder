import time
start = time.perf_counter()

######################
N, S, M, L = map(int, input().split())
ans = float('inf')

for i in range(20):
  for j in range(20):
    for k in range(20):
      if i*6 + j*8 + k*12 >= N:
        ans = min(ans, i * S + j * M + k * L)

print(ans)
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder