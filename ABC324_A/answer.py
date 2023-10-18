import time
start = time.perf_counter()

######################
N = int(input())
A = set(list(map(int, input().split())))
print("Yes" if len(A) == 1 else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder