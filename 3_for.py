"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара!
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров!
"""

def main():

    stoke = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

# Посчитать и вывести среднее количество продаж для каждого товара
    def avg_sales(phone_sales):
      scores_sum = 0
      for sale in phone_sales:
         scores_sum += sale
      return round(scores_sum / len(phone_sales), 2)

#Посчитать и вывести среднее количество продаж всех товаров
    product_avg_sales = 0
    for one_product in stoke:
       product_avg = avg_sales(one_product['items_sold'])
       print(f'Ср. кол-во продаж для каждого товара {one_product["product"]}: {product_avg}')
       product_avg_sales += product_avg
       stoke_avr = round(product_avg_sales / len(stoke), 2)
    print(f'Ср. кол-во всех продаж {stoke_avr}')

#Посчитать и вывести суммарное количество продаж для каждого товара
    def total_sales(total_summ):
       sales = 0
       for sale in total_summ:
         sales += sale
       return sales

#Посчитать и вывести суммарное количество продаж всех товаров
    all_sales = 0
    for one_product in stoke:
       product_summ = total_sales(one_product['items_sold'])
       print(f'Суммарное кол-во продаж всех товаров {one_product["product"]}: {product_summ}')
       all_sales += product_summ
    print(f'Суммарное кол-во продаж каждого телефона {all_sales}')




if __name__ == "__main__":
    main()
