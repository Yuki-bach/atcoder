import time
start = time.perf_counter()

######################
N, K = list(map(int, input().split()))
S = list(input())

count = 0
for i in range(N):
  if count <= K and S[i]=="o":
    count += 1
  if count > K and S[i]=="o":
    S[i]="x"
print(*S, sep="")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder