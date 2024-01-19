import time
start = time.perf_counter()

######################
Y = int(input())
print((Y+1)//4 * 4 + 2)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder