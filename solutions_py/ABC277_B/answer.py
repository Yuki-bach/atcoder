import time
start = time.perf_counter()

######################
N = int(input())
S = []
for _ in range(N):
  s = input()
  is_satisfied = s[0] in ['H','D','C','S'] \
    and s[1] in ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K' ] \
    and s not in S
  if (is_satisfied==False):
    print("No")
    exit()
  S.append(s)
print("Yes")



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder