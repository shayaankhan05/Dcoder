N = int(input())
words = list(input())
i = len(words)
for i in range(len(words)):
    if words[i].isdigit() == True:
        print(words[i], end=" ")
        continue
    else:
        continue
