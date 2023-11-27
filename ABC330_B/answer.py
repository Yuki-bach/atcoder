import time
start = time.perf_counter()

######################
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
  if a>=L and a<=R:
    print(a)
  elif a<L:
    print(L)
  else:
    print(R)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder