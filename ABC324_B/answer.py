import time
start = time.perf_counter()

######################
N = int(input())
while(N % 2==0):
  N = N/2
while(N % 3==0):
  N = N/3
print("Yes" if N == 1 else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder