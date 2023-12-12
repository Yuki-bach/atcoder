import time
start = time.perf_counter()

######################
"""TLE"""
# from itertools import combinations
# N, M = map(int, input().split())
# lines = [tuple(map(int, input().split())) for _ in range(M)]
# ans = 0

# for a,b,c in combinations(range(1, N+1), 3):
#   if (a,b) in lines and (b,c) in lines and (a,c) in lines:
#     ans += 1

# print(ans)

from collections import defaultdict
N, M = map(int, input().split())
D = defaultdict(list)

for _ in range(M):
  u, v = map(int, input().split())
  D[u].append(v)

ans = 0
for a in list(D.keys()):
  for b in D[a]:
    for c in range(1, N+1):
      if c in D[a] and c in D[b]:
        ans += 1

print(ans)





#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder