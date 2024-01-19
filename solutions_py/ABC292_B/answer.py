import time
start = time.perf_counter()

######################
N, Q = map(int, input().split())
players = [0 for _ in range(N)]

for _ in range(Q):
  event, x = map(int, input().split())
  if (event==3):
    print("Yes" if players[x-1]>=2 else "No")
  else:
    players[x-1] += event



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder