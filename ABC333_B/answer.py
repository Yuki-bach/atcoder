line1 = input()
line2 = input()

def get_length(line):
  length = abs(ord(line[0]) - ord(line[1]))
  return 5 - length if length >= 3 else length

print("Yes" if get_length(line1) == get_length(line2) else "No")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder