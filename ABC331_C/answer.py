import time
start = time.perf_counter()

######################
## TLE
# N = int(input())
# A = list(map(int, input().split()))
# for a in A:
#   print(sum(x for x in A if x > a), end=" ")

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A, reverse=True)
sums = {}

tmp = 0
for a in A_sorted:
  if a not in sums:
    sums[a] = tmp
  tmp += a

print(*[sums[a] for a in A])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder