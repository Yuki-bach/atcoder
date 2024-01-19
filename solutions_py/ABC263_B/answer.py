import time
start = time.perf_counter()

######################
N = int(input())
P = list(map(int, input().split()))
ans = 0

while N > 1:
  N = P[N-2]
  ans += 1
print(ans)



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder