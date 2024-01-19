import time
start = time.perf_counter()

######################
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
  if sum(sorted(A+[i])[1:-1]) >= X:
    print(i)
    exit()
print(-1)



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder