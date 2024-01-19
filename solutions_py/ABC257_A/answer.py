import time
start = time.perf_counter()

######################
N, X = map(int, input().split())
S = ""
for i in range(26):
  S += ("".join([chr(ord('A') + i) for _ in range(N)]))
print(S[X-1])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder