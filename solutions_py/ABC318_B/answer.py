import time
start = time.perf_counter()

######################
N = int(input())
sheets = []
for _ in range(N):
  sheets.append(list(map(int, input().split())))

def get_tiles(sheet):
  output = set()
  for i in range(sheet[0], sheet[1]):
    for j in range(sheet[2], sheet[3]):
      output.add(str(i)+"_"+str(j))
  return output

result = set()
for sheet in sheets:
  result = result | get_tiles(sheet)
print(len(result))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder