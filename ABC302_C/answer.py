
"""attempt 1
if, elifが同時にtrueの時に対応できない
"""
# from collections import deque

# N, M = map(int, input().split())
# S = deque([input() for _ in range(N)])
# ans = deque([S.popleft()])

# def checker(str1, str2):
#   diff_counter = 0
#   for i in range(M):
#     if str1[i] != str2[i]:
#       diff_counter += 1
#   return diff_counter == 1

# counter = 0
# while (len(S) > 0):
#   if (checker(ans[0], S[-1])):
#     ans.appendleft(S.pop())
#     counter = 0
#   elif (len(ans) > 1 and checker(ans[-1], S[-1])):
#     ans.append(S.pop())
#     counter = 0
#   else:
#     S.appendleft(S.pop())
#     counter += 1
#     if counter >= len(S):
#       exit(print("No"))
# print("Yes")

"""attempt 2
"""
from itertools import permutations
N, M = map(int, input().split())
S = [input() for _ in range(N)]

def checker(str1, str2):
  diff_counter = 0
  for i in range(M):
    if str1[i] != str2[i]:
      diff_counter += 1
  return 1 if diff_counter == 1 else 0

for t in permutations(S, N):
  true_count = 0
  for i in range(N-1):
    true_count += checker(t[i], t[i+1])
  if true_count == N-1:
    exit(print("Yes"))
print("No")



## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder