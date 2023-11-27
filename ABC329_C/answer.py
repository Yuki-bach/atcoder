import time
start = time.perf_counter()

######################
"""
first attempt -> WA
"""
# N = int(input())
# S = input()
# ans_set = set()
# idx = 0

# for i in range(N-1):
#   for j in range(i, N):
#     if len(set(list(S[i:j]))) == 1:
#       ans_set.add(S[i:j])
# print(len(ans_set))
# print(ans_set)
"""
second attempt -> TLE, MLE
"""
# N = int(input())
# S = input()
# ans_set = set()
# idx = 0

# while idx < N:
#   end_idx = idx + 1
#   ans_set.add(S[idx:end_idx])
#   while end_idx < N and S[end_idx] == S[idx]:
#     end_idx += 1
#     ans_set.add(S[idx:end_idx])
#   idx = end_idx

# print(len(ans_set))
"""
third attmept
"""
from collections import defaultdict
N = int(input())
S = input()
ans_dict = defaultdict(int)
idx = 0

while idx < N:
  end_idx = idx+1
  while end_idx < N and S[end_idx] == S[idx]:
    end_idx += 1
  ans_dict[S[idx]] = max(ans_dict[S[idx]], end_idx - idx)
  idx = end_idx
print(sum(ans_dict.values()))



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder