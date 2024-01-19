import time
start = time.perf_counter()

######################
[n, h, x] = list(map(int, input().split()))
p = list(map(int, input().split()))

for i in range(n):
  if h + p[i] >= x:
    print(i+1)
    exit()

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder