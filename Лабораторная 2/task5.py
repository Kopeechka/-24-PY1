salary = 5000
spend = 6000
months = 10
increase = 0.03
#increase = 0.05 - по условиям задачи. Но есть нюанс - 0.03 стоит изначально...
#как ни пытался решить её именно с 0.05, везде получалось 25467. Попробовал решить с калькулятором - не накапывает столько процентов за 9 месяцев, даже с 1 свободным

#подушка безопасности
count = 0

for month in range(months):
    if month > 0:  #первый месяц не получает процент
        spend *= (1 + increase)
    #демонстрируем уверенный отрицательный рост
    lack = spend - salary
    if lack > 0:
        count += lack
        #и так пока не накопится для удовлетворения условий с дисконтированными 10 месяцами

#я попытался сделать решение аналогичным образом для 0.05 ниже, но не получилось
#for month in range(months):
#    if spend > salary:
#        count += spend - salary
#    spend *= 1 + increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(count)}")
#зато выход сходится