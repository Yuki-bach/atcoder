import time
start = time.perf_counter()

######################
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = A.copy()

B[P-1:Q] = A[R-1:S]
B[R-1:S] = A[P-1:Q]
print(*B, sep=" ")


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder