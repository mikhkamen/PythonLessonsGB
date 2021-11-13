dict = {'1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре'
        }
with open('4_russian.txt', 'w') as f:
    f.seek(0)
with open('4_english.txt', encoding='UTF-8') as f:
    for line in f:
        lst = line.split()
        lst[0] = dict.get(lst[2])
        with open('4_russian.txt', 'a', encoding='UTF-8') as f:
            string = ' '.join(lst)
            f.write(string + '\n')

