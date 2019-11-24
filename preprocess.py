import re
import codecs
import os
import string

vn_sw = 'vietnamese-stopwords.txt'
input = 'topic_detection_train.v1.0.txt'
output = 'pre_process_' + input


def remove_all_characters_except_letters_and_numbers():
    try:
        count = 0
        stopwords = load_vietnamese_stopwords()
        if os.path.exists(output):
            os.remove(output)
        with codecs.open(output, 'a', 'utf-8') as o:
            with open(input, 'rb') as i:
                while True:
                    line = i.readline()
                    if line:
                        line = line.decode('utf-8')
                        index = line.find(' ')
                        label = line[:index]
                        content = line[index:]

                        content = content.lower()
                        content = re.sub(r'\d+', '', content)
                        content = content.translate(str.maketrans('', '', string.punctuation))
                        content = re.sub('[\W_]+', ' ', content.strip())
                        content = content.strip()
                        for w in stopwords:
                            content = content.replace(w, '')

                        line = label + ' ' + content + '\n'
                        count = count + 1
                        o.write(line)
                        print('writing: ' + str(count) + ' line')
                    else:
                        o.close()
                        i.close()
                        print('done')
                        return True
    except Exception as e:
        print('error: '+str(e))
        return False


def load_vietnamese_stopwords():
    try:
        resulf = []
        with open(vn_sw, 'rb') as i:
            while True:
                line = i.readline()
                if line:
                    resulf.append(line.decode('utf-8'))
                else:
                    i.close()
                    return resulf
    except Exception as e:
        print('error: '+str(e))
        return []


remove_all_characters_except_letters_and_numbers()
