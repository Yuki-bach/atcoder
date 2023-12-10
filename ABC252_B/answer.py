import time
start = time.perf_counter()

######################
N, K  = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

most_tasty_idx = [i+1 for i, a in enumerate(A) if a == max(A)]

for mti in most_tasty_idx:
  if mti in B:
    exit(print("Yes"))
    
print("No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder