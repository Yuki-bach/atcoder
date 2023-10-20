import time
start = time.perf_counter()

######################
H ,W = map(int, input().split())
counter = 0
for _ in range(H):
  counter += input().count("#")
print(counter)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder