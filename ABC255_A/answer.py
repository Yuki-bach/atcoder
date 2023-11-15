import time
start = time.perf_counter()

######################
R, C = map(int, input().split())
A = [list(map(int, input().split())), list(map(int, input().split()))]
print(A[R-1][C-1])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder