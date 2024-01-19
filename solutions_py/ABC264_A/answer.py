import time
start = time.perf_counter()

######################
L, R = map(int, input().split())
print("atcoder"[L-1:R])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder