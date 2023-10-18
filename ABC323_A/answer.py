import time
start = time.perf_counter()

######################
S = input()
for i in range(1, 17, 2):
  if S[i] != "0":
    print("No")
    exit()
print("Yes")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder