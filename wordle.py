import random
from termcolor import colored

number = random.randint(10000, 99999)
number = 11111
yellow_text = (colored("жовтим", "yellow"))
green_text = (colored("зеленим", "green"))
grey_text = (colored("сірим", "grey"))
rules = f"""
Мета гри: Вгадати п'ятицифирне число за допомогою максимум шести спроб.

Процес гри:
Гравець вводить п'ятицифирне слово в поле.
Після введення числа, натискається кнопка "Відправити" або подібна для перевірки числа.
Система перевіряє, чи є введене число правильним, і відображає результат.

Зворотний зв'язок:
Якщо цифра числа є в правильному місці, вона підсвічується {green_text}, та це не означає що дана цифра вже не може зустрітіся в числі.
Якщо цифра числа є в числі, але в неправильному місці, вона підсвічується {yellow_text}.
Якщо цифра числа не входить у слово, вона підсвічується {grey_text}.

Гра продовжується, поки гравець або не вгадає число, або не використає всі шість спроб.

Кінець гри:
Якщо число вгадане, гра завершена, і гравець може побачити правильне число.
Якщо всі спроби використані, але число не вгадане, також показується правильна відповідь.
"""
user_consent = int(input("Хочете ознайомитись з правилами? 1 - так, 2 - ні: "))

if user_consent == 1:
    print(rules)


matrix_number = [] * 6

count = 0
win = False
while count < 6:
    user_number = None
    while user_number is None:
        try:
            user_number = int(input("Bведіть ваше число: "))
        except ValueError:
            print("Ви ввели щось не те, введіть число будь ласка")
    if len(list(str(user_number))) != 5:
        print("число не містить 5 символів")
        continue
    if user_number == number:
         print(colored(f"""ВІТАЄМО ВИ ВИГРАЛИ!!!!!!!!!!! Ви впорались за {count+1} ходи """, "green"))
         win = True
         break
    else:
        user_number_list = list(str(user_number))
        number_list = list(str(number))
        feedback = []
        for j in range(5):
            if user_number_list[j] == number_list[j]:
               feedback.append(colored(user_number_list[j] , "green"))
            elif user_number_list[j] in number_list :
               feedback.append(colored(user_number_list[j] , "yellow"))
            else:
                feedback.append(colored(user_number_list[j] , "grey"))
        
        matrix_number.append("".join(feedback))
        count += 1        
        for num in matrix_number:
            print(num)
if not win:                   
    print(colored("Ви програли, правильне число було:", "red"), colored(number, "red"))
                     