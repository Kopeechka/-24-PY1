numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#случайно выбранная позиция в списке не обязательно равна 4,
#поэтому вместо использования numbers[4] добавил новую величину

random_missing_item = 4
sum_numbers = sum(numbers[:random_missing_item]) + \
              sum(numbers[random_missing_item+1:])
numbers[random_missing_item] = round(sum_numbers /
                                     len(numbers), 2)
#не понял исходя из pep8 нужно ли переносить подобным образом строки,
#если они слишком длинные, но сделал так на всякий случай

print("Измененный список:", numbers)
