import time
start = time.perf_counter()

######################
N, Q = map(int, input().split())
S = input()

consecutive = [0]
for i in range(N-1):
  consecutive.append(consecutive[-1] + (S[i] == S[i+1]))

for _ in range(Q):
  l, r = map(int, input().split())
  print(consecutive[r-1] - consecutive[l-1])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder