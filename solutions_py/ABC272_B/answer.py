import time
start = time.perf_counter()

######################
from itertools import permutations
N, M = list(map(int, input().split()))
check = [[i==j for j in range(N)] for i in range(N)]

for i in range(M):
  k, *x = list(map(int, input().split()))
  all_combinations = list(permutations(x, 2))
  for (p_1, p_2) in all_combinations:
    check[p_1-1][p_2-1] = True
print("Yes" if all(all(row) for row in check) else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder