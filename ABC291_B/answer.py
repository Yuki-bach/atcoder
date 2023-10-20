import time
start = time.perf_counter()

######################
N = int(input())
X = list(map(int, input().split()))

for _ in range(N):
  X.remove(max(X))
  X.remove(min(X))

print(sum(X) / len(X))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder