import time
start = time.perf_counter()

######################

N,X,Y,Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []

for _ in range(X):
  max_A = max(A)
  for i in range(N):
    if A[i]==max_A:
      ans.append(i+1)
      A[i] = -1
      B[i] = -1
      break

for _ in range(Y):
  max_B = max(B)
  for i in range(N):
    if B[i]==max_B:
      ans.append(i+1)
      A[i] = -1
      B[i] = -1
      break

sum_scores = [A[i] + B[i] for i in range(N)]
for _ in range(Z):
  max_sum_scores = max(sum_scores)
  for i in range(N):
    if sum_scores[i]==max_sum_scores:
      ans.append(i+1)
      sum_scores[i] = -1
      break

print("\n".join(map(str, sorted(ans))))

## another solution
# n,x,y,z = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# abi = [[a[i],b[i],i+1] for i in range(n)]
# ans = []

# abi.sort(key=lambda ABI:(-ABI[0],ABI[2]))

# for X in range(x):
#     ans.append(abi[X][2])
#     abi[X][0] = 0
#     abi[X][1] = -1

# abi.sort(key=lambda ABI:(-ABI[1],ABI[2]))

# for Y in range(y):
#     ans.append(abi[Y][2])
#     abi[Y][0] = 0
#     abi[Y][1] = -1

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder