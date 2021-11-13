n = int(input('Введите время в секундах: '))
h = n // 3600
m = (n % 3600) // 60
s = (n % 3600) % 60

if s < 10:
    s = f'0{s}'
else:
    s = str(s)
if m < 10:
    m = f'0{m}'
else:
    m = str(m)
if h < 10:
    h = f'0{h}'
else:
    h = str(h)
print(f'{n} секунд в формате чч:мм:сс - это {h}:{m}:{s}')
