import time
start = time.perf_counter()

######################

### TLE
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# reversed_days = [int(d in A) for d in range(N, 0, -1)]
# ans = []
# for d in reversed_days:
#   if d == 1:
#     ans.append(0)
#   else:
#     ans.append(ans[-1]+1)
# print('\n'.join(map(str, ans[::-1])))

N, M = map(int, input().split())
A_set = set(map(int, input().split()))
ans = [0] * N

last_seen_1 = -1
for d in range(N - 1, -1, -1):
  if d + 1 in A_set:
    last_seen_1 = d
  elif last_seen_1 != -1:
    ans[d] = ans[d + 1] + 1

print('\n'.join(map(str, ans)))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder