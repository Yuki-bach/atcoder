import time
start = time.perf_counter()

######################
N, A, B = map(int, input().split())

for i in range(N):
  ans = ""
  for j in range(N):
    if (i%2==0 and j%2 == 0) or (i%2==1 and j%2 == 1):
      ans += ("."*B)
    else:
      ans += ("#"*B)
  for _ in range(A):
    print(ans)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder