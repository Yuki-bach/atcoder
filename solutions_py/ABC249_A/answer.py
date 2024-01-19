import time
start = time.perf_counter()

######################

A,B,C,D,E,F,X = map(int, input().split())
takahashi = A*B * (X//(A+C)) + B * (min(X%(A+C), A))
aoki = D*E * (X//(D+F)) + E * (min(X%(D+F), D))
if takahashi > aoki:
  print("Takahashi")
elif (takahashi < aoki):
  print("Aoki")
else:
  print("Draw")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder