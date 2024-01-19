import time
start = time.perf_counter()

######################
import itertools
N, W = map(int, input().split())
A = list(map(int, input().split()))
sums = set()

for comb_num in range(1, min(3,N)+1):
  for v in itertools.combinations(A, comb_num):
    sums.add(sum(v))

ans = sum(1 for num in sums if num <= W)
print(ans)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder