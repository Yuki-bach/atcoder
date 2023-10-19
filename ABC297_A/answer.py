import time
start = time.perf_counter()

######################
N, D = list(map(int, input().split()))
T = list(map(int, input().split(" ")))
for i in range(N-1):
  if T[i+1] - T[i] <= D:
    print(T[i+1])
    exit()
print(-1)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder