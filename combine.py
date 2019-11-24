from collections import defaultdict

# Combine result
pred1 = open('predlabel.txt', 'r', encoding='utf-8')
pred2 = open('predlabel2.txt', 'r', encoding='utf-8')
pred3 = open('predlabel3.txt', 'r', encoding='utf-8')
pred4 = open('predlabel4.txt', 'r', encoding='utf-8')
pred5 = open('predlabel5.txt', 'r', encoding='utf-8')
pred6 = open('predlabel6.txt', 'r', encoding='utf-8')
tempres = open('tempres.txt', 'w', encoding='utf-8')

for i in range(10017):
    line1 = pred1.readline()[:-1]
    line2 = pred2.readline()[:-1]
    line3 = pred3.readline()[:-1]
    line4 = pred4.readline()[:-1]
    line5 = pred5.readline()[:-1]
    line6 = pred6.readline()[:-1]
    if line1 == line2 == line3 == line4 == line5 == line6:
        tempres.write(line1 + '\n')
    else:
        e = defaultdict(list)
        if line1 not in e.keys():
            e[line1] = 1
        else:
            e[line1] += 1
        if line2 not in e.keys():
            e[line2] = 1
        else:
            e[line2] += 1
        if line3 not in e.keys():
            e[line3] = 1
        else:
            e[line3] += 1
        if line4 not in e.keys():
            e[line4] = 1
        else:
            e[line4] += 1
        if line5 not in e.keys():
            e[line5] = 1
        else:
            e[line5] += 1
        if line6 not in e.keys():
            e[line6] = 1
        else:
            e[line6] += 1
        max = 0
        predlabel = ''
        for k in e.keys():
            if e[k] > max:
                predlabel = k
                max = e[k]
        tempres.write(predlabel + '\n')

# Check for right format
labels = open('allLabels.txt', 'r', encoding='utf-8')
result = open('tempres.txt', 'r', encoding='utf-8')
label = labels.readlines()
for i in range(len(label)):
    label[i] = label[i][:-1]
# print(label)
label = list(label)
res = result.readlines()
for i in range(len(res)):
    res[i] = res[i][:-1]
# print(res)
for i in range(len(res)):
    if res[i] not in label:
        print(i+1)
