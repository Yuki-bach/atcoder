import time
start = time.perf_counter()

######################
N = int(input())

output = []
for i in range(N+1):
  tmp = 10000
  for j in range(1, 10):
    if N % j == 0 and i % (N//j) == 0:
      tmp = min(tmp, j)
  output.append(str(tmp) if tmp != 10000 else "-")

print("".join(output))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder