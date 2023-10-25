import time
start = time.perf_counter()

######################
H, M = map(lambda x: f"{int(x):02}", input().split())

def does_misjudge(h, m):
  check_min =  0 <= int(h[1]) <= 5
  check_hour = 0 <= int(h[0]) <= 1 or (int(h[0])==2 and 0 <= int(m[0]) <= 3)
  if (check_min and check_hour):
    print(h, m)
    exit()

i = 0
while i < 3600:
  does_misjudge(H, M)
  if M!="59":
    M = f"{int(M)+1:02}"
  else:
    H = f"{int(H)+1:02}" if int(H)<23 else "00"
    M = "00"
  i+=1


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder