import time
start = time.perf_counter()

######################
S = input()
T = input()
print("Yes" if T.startswith(S) else "No")
## re.match(r"^{S}", T)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder