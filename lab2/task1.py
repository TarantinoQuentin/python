money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month_count = 0
while money_capital + salary >= spend:
    money_capital += salary - spend
    spend += spend * increase
    month_count += 1

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
