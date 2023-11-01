import time
start = time.perf_counter()

######################
N,M,X,T,D = map(int, input().split())
if (M >= X):
  print(T)
else:
  print(T-(X-M)*D)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder