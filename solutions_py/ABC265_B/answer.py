import time
start = time.perf_counter()

######################
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonus = {}
for _ in range(M):
  X,Y = map(int, input().split())
  bonus[X-1] = Y

for i in range(N-1):
  if (i in bonus.keys()):
    T += bonus[i]
  T -= A[i]
  if (T <= 0):
    print("No")
    exit()
print("Yes")


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder