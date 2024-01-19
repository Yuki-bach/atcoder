import time
start = time.perf_counter()

######################
R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

def is_number(r, c):
  return B[r][c] != "." and B[r][c] != "#"

def explode(r,c):
  power = int(B[r][c])
  for tmp_r in range(max(r-power,0), min(r+power+1, R)):
    for tmp_c in range(max(c-power,0), min(c+power+1, C)):
      if (abs(r-tmp_r) + abs(c-tmp_c) <= power) and (not is_number(tmp_r,tmp_c)):
        B[tmp_r][tmp_c] = "."
  B[r][c] = "."

for r in range(R):
  for c in range(C):
    if is_number(r,c):
      explode(r,c)
for b in B:
  print("".join(b))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder