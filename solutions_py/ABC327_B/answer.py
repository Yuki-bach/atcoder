import time
start = time.perf_counter()

######################
B = int(input())
i = 1
while (i**i<=B):
  if i**i==B:
    print(i)
    exit()
  i += 1
print(-1)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder