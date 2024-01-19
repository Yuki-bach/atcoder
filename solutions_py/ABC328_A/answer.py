import time
start = time.perf_counter()

######################
N, X = map(int, input().split())
S = list(map(int, input().split()))
ans = sum([s for s in S if s <= X ])
print(ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder