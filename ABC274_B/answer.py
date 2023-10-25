import time
start = time.perf_counter()

######################

## my submission
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = []
for i in range(W):
  col = [row[i] for row in S]
  ans.append(col.count('#'))
print(*ans)

'''
comment from chatGPT:
creating a new list for each column, which might increase memory usage

bette way:

C = [input() for _ in range(H)]
cnt = [0] * W
for i in range(H):
  for j in range(W):
    if C[i][j] == "#": cnt[j] += 1
print(*cnt)
'''

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder