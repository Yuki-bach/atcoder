import time
start = time.perf_counter()

######################
counter = {}
for chr in input():
  counter[chr] = counter.get(chr, 0) + 1

if len(counter) < 2:
  print(-1)
else:
  print([key for key, value in counter.items() if value == 1][0])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder