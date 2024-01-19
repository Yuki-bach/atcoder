import time
start = time.perf_counter()

######################

N, M = map(int, input().split())
p = []
f = []
for _ in range(N):
  product = list(map(int,input().split()))
  p.append(product[0])
  f.append(set(product[2:]))
for i in range(N):
  for j in range(N):
    if p[j] < p[i] and f[i] <= f[j]:
      print("Yes")
      exit()
    if p[i] == p[j] and (f[i] < f[j]):
      print("Yes")
      exit()
print("No")


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder