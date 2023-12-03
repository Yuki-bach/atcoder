import time
start = time.perf_counter()

######################
H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 4
if (R==1 or R==H):
  ans -= 1
if (C==1 or C==W):
  ans -= 1
if (H==1):
  ans -= 1
if (W==1):
  ans -= 1
print(ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder