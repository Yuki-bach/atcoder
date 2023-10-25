import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
road = {i: [] for i in range(1, N+1)}

for _ in range(M):
  a,b = map(int, input().split())
  road[a].append(b)
  road[b].append(a)
for i in range(1,N+1):
  print(len(road[i]), *sorted(road[i]))


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder