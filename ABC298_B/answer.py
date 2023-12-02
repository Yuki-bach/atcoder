import time
start = time.perf_counter()

######################
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
  B = list(zip(*B[::-1]))
  if all(A[i][j] == 0 or (A[i][j] == B[i][j] == 1) for i in range(N) for j in range(N)):
    exit(print("Yes"))
print("No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder