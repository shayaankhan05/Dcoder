N = int(input())
words = list(input().split())
x = "Nemo"

for i in range(len(words)):
    if x == words[i]:
        print(i+1)
    else:
        continue
