import time
start = time.perf_counter()

######################
N = int(input())
S = input()

## first attempt
# isA = False
# isB = False
# isC = False

# for i in range(N):
#   if S[i] == "A":
#     isA = True
#   if S[i] == "B":
#     isB = True
#   if S[i] == "C":
#     isC = True
#   if (isA and isB and isC):
#     print(i+1)
#     exit()

## second attempt
check_list = set(["A", "B", "C"])
for i in range(N):
  if S[i] in check_list:
    check_list.remove(S[i])
  if len(check_list) == 0:
    print(i+1)
    exit()


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder