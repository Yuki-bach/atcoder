N = int(input())
binary = bin(N)[2:]
count = 0

for char in reversed(binary):
  if char == '0':
    count += 1
  else:
    break
print(count)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder