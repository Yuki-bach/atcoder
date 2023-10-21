import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0
for s in S:
  if s[3:] in T:
    ans+=1
print(ans)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder