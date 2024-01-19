import time
start = time.perf_counter()

######################
n = int(input())
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
print(pi[:n+2])
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder