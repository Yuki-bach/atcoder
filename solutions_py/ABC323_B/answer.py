import time
start = time.perf_counter()

######################
N = int(input())
wins = [input().count("o") for _ in range(N)]
ans = []
for win_count in range(max(wins), -1, -1):
  for i in range(N):
    if wins[i] == win_count:
      ans.append(i+1)
print(*ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder