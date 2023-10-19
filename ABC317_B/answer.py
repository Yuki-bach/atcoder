import time
start = time.perf_counter()

######################
N = int(input())
A = list(map(int, input().split()))

for v in range(min(A)+1, max(A)):
  if v not in A:
    print(v)
    exit()

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder