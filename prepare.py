import random
import fasttext
import re

# Prepare train file
model = fasttext.train_supervised(input="topic_detection_train.v1.0.txt", epoch=1, loss='hs')

with open('topic_detection_train.v1.0.txt', 'r', encoding='utf-8') as original:
    with open('prep.txt', 'w', encoding='utf-8') as ppfile:
        for i in range(0, 16000):
            line = original.readline()
            line = line.replace('\n', '')
            text, label = model.get_line(line)

            for l in label:
                ppfile.write(l + ' ')

            for t in text:
                # Lowercase
                t = t.lower()
                # Remove HTML tag and links
                if t == '</s>' or 'https' in t or 'http' in t or 'www' in t or '.com' in t:
                    t = ''
                # Remove dash
                t = t.replace('_', ' ')
                # Remove number
                t = re.sub(r'\d+', ' ', t)
                # Remove special symbol
                t = re.sub(r'[^\w\s]', ' ', t)
                # Remove Chinese
                t = re.sub(r'[\uac00-\ud7a3]', ' ', t)
                # Remove Japanese
                t = re.sub(r'[\u3040-\u30ff]', ' ', t)
                # Remove Korean
                t = re.sub(r'[\u4e00-\u9FFF]', ' ', t)

                t = t.strip()
                ppfile.write(t + ' ')

            ppfile.write('\n')

# Prepare test file
with open('topic_detection_test.v1.0.txt', 'r', encoding='utf-8') as original:
    with open('preptest.txt', 'w', encoding='utf-8') as ppfile:
        for i in range(0, 16000):
            line = original.readline()
            line = line.replace('\n', '')
            text = line.split(' ')

            for t in text:
                # Lowercase
                t = t.lower()
                # Remove HTML tag and links
                if t == '</s>' or 'https' in t or 'http' in t or 'www' in t or '.com' in t:
                    t = ''
                # Remove dash
                t = t.replace('_', ' ')
                # Remove number
                t = re.sub(r'\d+', ' ', t)
                # Remove special symbol
                t = re.sub(r'[^\w\s]', ' ', t)
                # Remove Chinese
                t = re.sub(r'[\uac00-\ud7a3]', ' ', t)
                # Remove Japanese
                t = re.sub(r'[\u3040-\u30ff]', ' ', t)
                # Remove Korean
                t = re.sub(r'[\u4e00-\u9FFF]', ' ', t)

                t = t.strip()
                ppfile.write(t + ' ')

            ppfile.write('\n')

# Create vocab, labels file
model = fasttext.train_supervised(input="prep.txt", epoch=1, loss='hs')

vocab = model.get_words()
with open('vocab.txt', 'w', encoding='utf-8') as vfile:
    for w in vocab:
        vfile.write(w + '\n')

allLabels = model.get_labels()
with open('allLabels.txt', 'w', encoding='utf-8') as lfile:
    for w in allLabels:
        lfile.write(w + '\n')

# Create label-ordered file
with open('allLabels.txt', 'r', encoding='utf-8') as lfile:
    with open('aprep.txt', 'w', encoding='utf-8') as sort:
        for i in range(0, 23):
            k = 0
            l = lfile.readline()
            l = l.strip()
            with open('prep.txt', 'r', encoding='utf-8') as original:
                lines = original.readlines()
                random.shuffle(lines)
                for d in lines:
                    if l in d:
                        sort.write(d)
                        k += 1
            print(k)

# Split file into train.txt, dev.txt, test.txt as 0.8, 0.1, 0.1
with open('prep.txt', 'r', encoding='utf-8') as original:
    with open('train.txt', 'w', encoding='utf-8') as train:
        with open('dev.txt', 'w', encoding='utf-8') as dev:
            with open('test.txt', 'w', encoding='utf-8') as test:
                lines = original.readlines()
                random.shuffle(lines)
                k = 0
                for l in lines:
                    if k in range(0, int(16000*0.8)):
                        train.write(l)
                    if k in range(int(16000*0.8), int(16000*0.9)):
                        dev.write(l)
                    if k in range(int(16000*0.9), 16000):
                        test.write(l)
                    k += 1
                print(k)

# Create smaller embedding file
with open('vocab.txt', 'r', encoding='utf-8') as vocab:
    with open('embedding.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(str("24945 300\n"))
        k = 0
        for i in range(0, 24945):
            w = vocab.readline()
            w = w.strip()
            w = w + " "
            with open('cc.vi.300.vec', 'r', encoding='utf-8') as infile:
                for j in range(0, 2000000+1):
                    l = infile.readline()
                    if l[:len(w)] == w:
                        outfile.write(l)
                        break
            k += 1
            print(k)
