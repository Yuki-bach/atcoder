import time
start = time.perf_counter()

######################

## TLE
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = [0 for _ in range(N)]

counter = 0
found = True
while counter < 2**N:
  X = format(counter, '0{}b'.format(N))
  for i in range(M):
    if X[A[i]-1] == X[B[i]-1]:
      found = False
      break
  if found:
    print("Yes")
    exit()
  counter += 1
  found = True

print("No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder