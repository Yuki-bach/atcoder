import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
S = input()
T = input()

def check(S, T):
  is_prefix = T.startswith(S)
  is_suffix = T.endswith(S)
  if is_prefix and is_suffix: return 0
  if is_prefix: return 1
  if is_suffix: return 2
  else: return 3

print(check(S, T))


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder