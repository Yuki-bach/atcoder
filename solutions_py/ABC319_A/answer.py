import time
start = time.perf_counter()

######################
S = input()
rankings = [
  "tourist 3858",
"ksun48 3679",
"Benq 3658",
"Um_nik 3648",
"apiad 3638",
"Stonefeang 3630",
"ecnerwala 3613",
"mnbvmar 3555",
"newbiedmy 3516",
"semiexp 3481"
]
for line in rankings:
  if S == line.split()[0]:
    print(line.split()[1])

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder