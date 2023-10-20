import time
start = time.perf_counter()

######################
N, X = map(int, input().split())
P = list(map(int, input().split()))
print(P.index(X)+1)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder