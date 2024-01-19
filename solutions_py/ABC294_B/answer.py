import time
start = time.perf_counter()

######################
H, W = map(int, input().split())

for _ in range(H):
  A = list(map(int, input().split()))
  ans = ""
  for a in A:
    ans += '.' if a==0 else chr(ord("A")+a-1)
  print(ans)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder