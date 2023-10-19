import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
B = set()

for _ in range(M):
  a, b = map(int, input().split())
  B.add(b)

candidates = set([i+1 for i in range(N)])
candidates = candidates - B

for c in candidates:
  if c in B:
    candidates.remove(c)
print(candidates.pop() if len(candidates) == 1 else -1)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder