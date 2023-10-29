import time
start = time.perf_counter()

######################
N = int(input())
while N < 1000:
  if (N//100) * (N//10%10) == N%10:
    print(N)
    exit()
  N += 1


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder