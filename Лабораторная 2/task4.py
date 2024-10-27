money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

#как с count, начинаю отсчёт с нуля для цикла
months = 0
#цикл будет повторяться, пока расходы не будут больше суммы подушки и зарплаты
while money_capital + salary >= spend:
    money_capital += salary - spend
    spend *= 1 + increase
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)

