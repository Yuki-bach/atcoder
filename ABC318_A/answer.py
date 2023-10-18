import time
import math
start = time.perf_counter()

######################
N, M, P = list(map(int, input().split()))
if N < M:
  print(0)
  exit()
print(math.floor((N - M)/P) + 1)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder