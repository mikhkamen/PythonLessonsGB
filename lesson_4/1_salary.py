from sys import argv

salary, working_hours, rate_per_hour, bonus = argv

print("Имя скрипта: ", salary)
print("Отработано часов: ", working_hours)
print("Ставка за час: ", rate_per_hour)
print("Премия : ", bonus)

working_hours = int(working_hours)
rate_per_hour = float(rate_per_hour)
bonus = int(bonus)
salary = working_hours * rate_per_hour
print(f'За период выработка составила {working_hours} часов по ставке {rate_per_hour} руб/час,'
      f'к оплате {salary} руб. Премия - {bonus} руб. Итого к оплате {salary + bonus} рублей ')