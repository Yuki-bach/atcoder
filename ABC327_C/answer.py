import time
start = time.perf_counter()

######################
def checker(arr):
  if sorted(arr) != [i for i in range(1,10)]:
    print("No")
    exit()

A = [list(map(int, input().split())) for _ in range(9)]

## row checker
for i in range(9):
  checker(A[i])

## column checker
for i in range(9):
  tmp = []
  for j in range(9):
    tmp.append(A[j][i])
  checker(tmp)

## box checker
for i in range(0,7,3):
  for j in range(0,7,3):
    tmp = [A[i][j], A[i][j+1], A[i][j+2],
           A[i+1][j], A[i+1][j+1], A[i+1][j+2],
           A[i+2][j], A[i+2][j+1], A[i+2][j+2]]
    checker(tmp)
print("Yes")




#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder