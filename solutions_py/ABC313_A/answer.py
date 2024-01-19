import time
start = time.perf_counter()

######################
n = int(input())
p = list(map(int, input().split()))
if n == 1:
  print(0)
  exit()
x = max(p[1:]) - p[0] + 1
print(x if x>0 else 0)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder