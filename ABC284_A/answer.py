import time
start = time.perf_counter()

######################
N = int(input())
S = [input() for _ in range(N)]
print(*S[::-1], sep = "\n")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder