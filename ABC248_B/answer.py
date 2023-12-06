import time
start = time.perf_counter()

######################
A, B, K = map(int, input().split())

for i in range(10 ** 9):
  if A * (K**i) >= B:
    exit(print(i))


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder