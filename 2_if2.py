"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
   
    def string(str_1, str_2):
      if type(str_1) == str and type(str_2) == str:
        
        if str_1 == str_2:
          print("строки одинаковые, вернуть 1")
        else:
          str_1 != str_2
          if str_2 == "learn":
            print("строки разные и вторая строка 'learn', возвращает 3")
          else:
            print("строки разные и первая длиннее, вернуть 2")
            
      else:
        print("Не строка, вернуть 0")

    string(1, 3)
    string("Python", "Python")
    string("Python", "bet")
    string("Python", "learn")

if __name__ == "__main__":
    main()
# почему не срабатывает str_1) != len(str_2) and str_2 == "learn"