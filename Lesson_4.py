# Общий объем продаж. Покупатель приобретает в магазине пять товаров. Напишите программу, которая запрашивает цену
# каждого товара и затем выводит накопленную стоимость приобретаемых товаров, сумму налога с продаж и итоговую сумму.
# Допустим, что налог с продаж составляет 7%.

NALOG = 7

price_tovar_1 = int(input('Цена товара 1 - '))
summ = price_tovar_1
nalog = summ / 100 * NALOG
itog = summ - nalog
print(f'Накопленная стоимость: {summ}, сумма налога: {nalog}, итоговая сумма: {itog}')

price_tovar_2 = int(input('Цена товара 2 - '))
summ += price_tovar_2
nalog = summ / 100 * NALOG
itog = summ - nalog
print(f'Накопленная стоимость: {summ}, сумма налога: {nalog}, итоговая сумма: {itog}')

price_tovar_3 = int(input('Цена товара 3 - '))
summ += price_tovar_3
nalog = summ / 100 * NALOG
itog = summ - nalog
print(f'Накопленная стоимость: {summ}, сумма налога: {nalog}, итоговая сумма: {itog}')

price_tovar_4 = int(input('Цена товара 4 - '))
summ += price_tovar_4
nalog = summ / 100 * NALOG
itog = summ - nalog
print(f'Накопленная стоимость: {summ}, сумма налога: {nalog}, итоговая сумма: {itog}')

price_tovar_5 = int(input('Цена товара 5 - '))
summ += price_tovar_5
nalog = summ / 100 * NALOG
itog = summ - nalog
print(f'Накопленная стоимость: {summ}, сумма налога: {nalog}, итоговая сумма: {itog}')