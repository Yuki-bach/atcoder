import time
start = time.perf_counter()

######################
def recursive(n):
  if n == 0: return 1
  return n * recursive(n-1)
print(recursive(int(input())))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder