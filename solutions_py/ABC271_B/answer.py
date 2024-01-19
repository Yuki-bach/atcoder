import time
start = time.perf_counter()

######################
N, Q = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(N)]
for _ in range(Q):
  i,j = map(int, input().split())
  print(a[i-1][j-1])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder