import time
start = time.perf_counter()

######################
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
  piece = A[L[i]-1]
  if piece < N and piece+1 not in A:
    A[L[i]-1] += 1
print(*A)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder