import time
start = time.perf_counter()

######################
X,Y,N = map(int, input().split())
ans = 0
if X < Y/3:
  ans = X * N
else:
  ans = Y * (N // 3) + X * (N % 3)
print(ans)
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder