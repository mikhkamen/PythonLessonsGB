import string as st


def uppers(line):
    return ' '.join(a[:1].upper() + a[1:] for a in line.split(' '))


stroka = input('Введите строку, каждое слово через пробел.\n')

print(str.title(stroka))  # Это самый простой метод, но не всегда работающий.  Попробуйте вставить
                            # слова с апострофом или аббревиатуру из заглавных букв, например
                            #   "the uncle’s house in USA"

print(st.capwords(stroka))  # Этот метод из модуля string работает лучше, но тоже недостаточно хорошо

print(uppers(stroka))       #  Руками всегда лучше получается )).
