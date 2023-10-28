import time
start = time.perf_counter()

######################
R, C = map(int, input().split())

for i in range(8):
  if R==1+i or R == 15-i or C == 1+i or C == 15-i:
    print("black" if i%2==0 else "white")
    exit()

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder