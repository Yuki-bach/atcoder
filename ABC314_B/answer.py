import time
start = time.perf_counter()

######################
N = int(input())
A = []
for i in range(N):
  c = int(input())
  A.append(list(map(int, input().split())))
X = int(input())

counts = []
for i in range(N):
  counts.append(len(A[i]) if X in A[i] else 40)

min_count = min(counts)
if (min_count == 40):
  print(0)
  exit()
  
output_list = []
for i in range(N):
  if counts[i] == min_count:
    output_list.append(str(i+1))
print(len(output_list))
print(" ".join(output_list))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder