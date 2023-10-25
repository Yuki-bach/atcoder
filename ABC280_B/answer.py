import time
start = time.perf_counter()

######################
N = int(input())
S = list(map(int, input().split()))
ans = [S[0]]
for i in range(N-1):
  ans.append(S[i+1]-S[i])
print(*ans)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder