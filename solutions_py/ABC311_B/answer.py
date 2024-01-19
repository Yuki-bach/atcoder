import time
start = time.perf_counter()

######################
N, D = list(map(int, input().split()))
S = []
for _ in range(N):
  S.append(input())

def isFree(day):
  for i in range(N):
    if S[i][day] == 'x':
      return False
  return True

isFree_list = [] ## ex. [False, True, True, False, False]
for i in range(D):
  isFree_list.append(isFree(i))

output = 0
count = 0
for i in range(D):
  if isFree_list[i]:
    count += 1
  else:
    count = 0
  if count > output:
    output = count
print(output)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder