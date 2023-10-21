import time
start = time.perf_counter()

######################
N, K = map(int, input().split())
S = [input() for _ in range(K)]
S.sort()
print(*S, sep="\n")



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder