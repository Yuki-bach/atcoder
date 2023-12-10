import time
start = time.perf_counter()

######################
H, W = map(int, input().split())
pieces = []

for i in range(H):
  S = input()
  for j in range(W):
    if S[j] == "o":
      pieces.append([i, j])

ans = abs(pieces[0][0]-pieces[1][0]) + abs(pieces[0][1]-pieces[1][1])
print(ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder