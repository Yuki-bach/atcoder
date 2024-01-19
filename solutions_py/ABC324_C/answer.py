import time
start = time.perf_counter()

######################
"""
attempts 1
"""
# import math
# N, T_dash = input().split()
# N = int(N)

# def checker(S):
#   if S == T_dash:
#     return True
#   if math.fabs(len(S)-len(T_dash))>1:
#     return False
#   if len(S)-len(T_dash) == 1 and T_dash in [S[:i]+S[i+1:] for i in range(len(S))]:
#     return True
#   if len(T_dash)-len(S) == 1 and T_dash in [S[:i]+T_dash[i]+S[i:] for i in range(len(T_dash))]:
#     return True
#   if len(S) == len(T_dash) and sum(1 for a, b in zip(S, T_dash) if a != b) == 1:
#     return True
#   return False

# ans = []
# for i in range(1,N+1):
#   S = input()
#   if checker(S):
#     ans.append(i)

# print(len(ans))
# print(*ans)

"""
attempt2
"""
N, T_dash = input().split()
N = int(N)

def checker(S, T_dash):
  if S == T_dash:
    return True
  if abs(len(S) - len(T_dash)) > 1:
    return False
  if len(S) - len(T_dash) == 1 and is_inserting(S, T_dash):
    return True
  if len(T_dash) - len(S) == 1 and is_deleting(S, T_dash):
    return True
  if len(S) == len(T_dash) and is_changing(S, T_dash):
    return True
  return False

def is_inserting(S, T_dash):
  for i in range(len(T_dash)):
    if S[i] != T_dash[i]:
      return S[:i] + S[i+1:] == T_dash
  return True

def is_deleting(S, T_dash):
  for i in range(len(T_dash)):
    if i < len(S) and S[i] != T_dash[i]:
      return S[:i] + T_dash[i] + S[i:] == T_dash
  return True

def is_changing(S, T_dash):
  diff = 0
  for a, b in zip(S, T_dash):
    if a != b:
      diff += 1
    if diff > 1:
      return False
  return diff <= 1

ans = []
for i in range(1,N+1):
  S = input()
  if checker(S, T_dash):
    ans.append(i)

print(len(ans))
print(*ans)
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder