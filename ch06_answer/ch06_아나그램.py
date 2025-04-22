word_1 = input()
word_2 = input()

word_1_d = dict()
word_2_d = dict()

for x in word_1:
    word_1_d[x] = word_1_d.get(x, 0) + 1

for x in word_2:
    word_2_d[x] = word_2_d.get(x, 0) + 1

if word_1_d == word_2_d:
    print("YES")
else:
    print("NO")
