import time
start = time.perf_counter()

######################
S = input()
check_1 = (S.find("B") + S.rfind("B")) % 2 == 1
check_2 = S.find("R") < S.find("K") < S.rfind("R")
print("Yes" if check_1 and check_2 else "No")
#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder