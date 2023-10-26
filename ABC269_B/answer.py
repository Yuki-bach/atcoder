import time
start = time.perf_counter()

######################
found_upper = False
ab = [0] * 2
cd = [0] * 2
for row in range(10):
  s = input()
  if (s == "."*10 and found_upper==False): continue

  index = s.find('#')
  if (index != -1 and found_upper == False):
    d = index + s[index:].find('.') if s[index:].find('.') != -1 else 10
    cd = [index+1, d]
    ab[0] = row+1
    found_upper = True

  if (s == "."*10 and found_upper):
    ab[1] = row
    break
if (ab[1]==0): ab[1] = 10

print(*ab)
print(*cd)





#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder