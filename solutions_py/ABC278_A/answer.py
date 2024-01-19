import time
start = time.perf_counter()

######################
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(*(A[K:] + [0 for _ in range(min(K,N))]))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder