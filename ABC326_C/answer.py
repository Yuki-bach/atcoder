import time
start = time.perf_counter()

######################
"""O(N^2)
"""
# N, M = map(int, input().split())
# A = sorted(list(map(int, input().split())))

# ans = 0
# for idx, x in enumerate(A):
#   count = 0
#   i = idx
#   while(i < N and A[i] < x+M):
#     count += 1
#     i += 1
#   ans = max(ans, count)
# print(ans)

"""O(N logN) ?
"""
from bisect import bisect_right

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans_list = []

for i, x in enumerate(A):
  right_index = bisect_right(A, x + M - 1)
  ans_list.append(right_index - i)

print(max(ans_list))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder