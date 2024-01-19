import time
start = time.perf_counter()

######################
N = input()
if len(N) == 1:
  print("Yes")
  exit()
for i in range(len(N)-1):
  if int(N[i]) <= int(N[i+1]):
    print("No")
    exit()
print("Yes")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder