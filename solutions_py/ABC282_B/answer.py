import time
start = time.perf_counter()

######################
N, M = map(int, input().split())
S = [input() for _ in range(N)]
S_decimals = [int(''.join('1' if c == 'o' else '0' for c in s), 2) for s in S]
## S_decimals = [int(input().replace("x", "0").replace("o", "1"), 2) for _ in range(N)]

count = 0
for i in range(len(S_decimals)):
  for j in range(i + 1, len(S_decimals)):
    if S_decimals[i] | S_decimals[j] == 2**M-1:
      count += 1

print(count)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder