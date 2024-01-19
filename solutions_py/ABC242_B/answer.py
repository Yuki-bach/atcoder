S = input()
S_ascii_list = [ord(char) for char in S]
S_ascii_list.sort()
ans = [chr(asc) for asc in S_ascii_list]
print(*ans, sep="")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder