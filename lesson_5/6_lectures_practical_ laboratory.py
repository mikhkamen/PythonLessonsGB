dict = {}
with open('6_lectures_practical_laboratory.txt', encoding='UTF-8') as f:
    for line in f:
        lst = line.split()
        num_list = [lst[0][:-1]]
        sum = 0
        for el in lst[1:]:
            word = ''
            num = ''
            for char in el:
                if char.isdigit():
                    num = num + char
                else:
                    word = word + char
            el = (int(num), word[1:-1])
            num_list.append(el)
            sum += int(num)
        key = lst[0][:-1]
        dict[key] = sum
print(dict)
