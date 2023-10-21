import time
start = time.perf_counter()

######################
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0]==1:
    A[query[1]-1] = query[2]
  else:
    print(A[query[1]-1])


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder