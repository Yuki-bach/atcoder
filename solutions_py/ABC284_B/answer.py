import time
start = time.perf_counter()

######################
T = int(input())
for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  print(len([a for a in A if a%2==1]))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder