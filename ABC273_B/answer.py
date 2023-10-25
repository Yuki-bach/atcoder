import time
start = time.perf_counter()

######################

X, K = map(int, input().split())
for i in range(1,K+1):
  digits = 10**i
  X = ((X + digits // 2) // digits) * digits
print(X)
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder