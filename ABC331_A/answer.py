import time
start = time.perf_counter()

######################
M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d < D:
  exit(print(y, m, d+1))
if m < M:
  exit(print(y, m+1, 1))
exit(print(y+1, 1, 1))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder