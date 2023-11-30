import time
start = time.perf_counter()

######################
N = int(input())
S = input()
ans = [0]*(N-1)

for i in range(1,N):
  for j in range(N-i):
    if S[j] == S[j+i]:
      break
    ans[i-1] += 1
for n in ans:
  print(n)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder