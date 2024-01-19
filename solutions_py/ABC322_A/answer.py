import time
start = time.perf_counter()

######################
N = int(input())
S = input()
for i in range(N-2):
  if S[i:i+3] == "ABC":
    print(i+1)
    exit()
print(-1)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder