V, *ABC = map(int, input().split())
ans = "FMT"
i = 0
while True:
  V -= ABC[i%3]
  if (V) < 0:
    exit(print(ans[i%3]))
  i += 1


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder