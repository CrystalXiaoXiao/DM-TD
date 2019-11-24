import fasttext

# BoW 1
model = fasttext.load_model('model.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)

# BoW 2
model = fasttext.load_model('model2.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel2.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)

# FastText 1
model = fasttext.load_model('model3.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel3.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)

# FastText 2
model = fasttext.load_model('model4.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel4.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)

# word2vec 300
model = fasttext.load_model('model5.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel5.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)

# word2vec 400
model = fasttext.load_model('model6.bin')
test = open('preptest.txt', 'r', encoding='utf-8')
pred_label = open('predlabel6.txt', 'w', encoding='utf-8')
k = 0
for line in test:
  line = line[:-1]
  labels, probs = model.predict(line)
  pred_label.write(labels[0]+'\n')
  k += 1
  print(labels[0])
print(k)