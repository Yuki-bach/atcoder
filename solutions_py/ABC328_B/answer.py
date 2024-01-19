import time
start = time.perf_counter()

######################
N = int(input())
D = list(map(int, input().split()))
ans = 0

for m, days in enumerate(D, 1):
  for d in range(1, days+1):
    if len(set(list(str(d)) + list(str(m)))) == 1:
      ans += 1
print(ans)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder