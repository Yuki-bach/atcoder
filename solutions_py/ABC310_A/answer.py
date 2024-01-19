import time
start = time.perf_counter()

######################
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

## 1st attempt
minPrice = P
for i in range(N):
  salePrice = Q + D[i]
  if minPrice > salePrice:
    minPrice = salePrice
print(minPrice)

## 2nd attempt
salePrice = min([Q+d for d in D])
print (salePrice if salePrice < P else P)

## 3rd attempt
print(min(P, Q+min(D)))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")
# python3 ./folder/answer.py < ./folder/input.txt