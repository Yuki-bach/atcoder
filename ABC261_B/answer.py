import time
start = time.perf_counter()

######################
N = int(input())
A = [list(input()) for _ in range(N)]
for i in range(N):
  for j in range(i+1, N):
    if (A[i][j]=='W' and A[j][i]=='L') \
        or (A[i][j]=='L' and A[j][i]=='W') \
        or (A[i][j]=='D' and A[j][i]=='D'):
      "correct"
    else:
      print("incorrect")
      exit()
print("correct")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder