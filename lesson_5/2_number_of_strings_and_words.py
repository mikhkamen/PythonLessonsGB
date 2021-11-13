lines = 0
count = 0
with open('2_num_str_words.txt', encoding='UTF-8') as f:
    for line in f:
        n_words = len(line.split())
        count += n_words
        print(f'Строка {lines + 1} состоит из {n_words} слов')
        lines = lines + 1
print(f'\nВсего в тексте {lines} строк и {count} слов')
