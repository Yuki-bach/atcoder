import time
start = time.perf_counter()

######################
import re
S = [int(s) for s in input()]

if (S[0]==1):
  print("No")
else:
  lanes = [
    S[6],
    S[3],
    int(S[1] + S[7] >= 1),
    int(S[0] + S[4] >= 1),
    int(S[2] + S[8] >= 1),
    S[5],
    S[9]
  ]

  str_lanes = ''.join(map(str, lanes))
  print("Yes" if re.search('10+1', str_lanes) else "No")





#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder