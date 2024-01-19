S = input()
a, b = map(int, input().split())
ans = S[:a - 1] + S[b - 1] + S[a:b - 1] + S[a - 1] + S[b:]
print(ans)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder