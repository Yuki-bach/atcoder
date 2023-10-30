import time
start = time.perf_counter()

######################
L1, R1, L2, R2 = map(int, input().split())
if (R1 < L2 or R2 < L1):
  print(0)
  exit()
print(min(R1,R2) - max(L1,L2))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder