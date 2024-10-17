disk_volume = 1.44
pages_amount = 100
lines_per_page = 50
symbols_per_line = 25
symbol_volume = 4

#исходные значения вынесены в начало

book_volume = round((symbol_volume*symbols_per_line*lines_per_page*pages_amount)/1024**2, 2)
book_amount = int(disk_volume / book_volume)
#я пытался сделать так, чтобы целое число получилось через //, но не понял как, поэтому оставил int()

print("Количество книг, помещающихся на дискету:", book_amount)
