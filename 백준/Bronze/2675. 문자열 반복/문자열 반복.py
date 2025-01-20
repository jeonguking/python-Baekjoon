
n = int(input())

for _ in range(n):
    a,b = input().split()
    a = int(a)
    new_word = ""
    for item in b:
        new_word += item *a
    print(new_word)
