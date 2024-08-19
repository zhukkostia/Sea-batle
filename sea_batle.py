from termcolor import colored as col

def start_finish_swap (x1, y1, x2, y2):
    if x1 > x2:
        t = x1
        x1 = x2
        x2 = t
    if y1 > y2:
        t = y1
        y1 = y2
        y2 = t
    return x1, y1, x2, y2

def do_cell_none (start_x, start_y, finish_x, finish_y, ship_player):
    if start_x == finish_x:
        if start_x == 0 and start_y == 0:
            ship_player[start_x+1][start_y] = col(0, "blue")
            for i in range (start_y+1 , finish_y):
                ship_player[start_x+1][i] = col(0, "blue")
            ship_player[finish_x+1][finish_y] = col(0, "blue") 
            ship_player[finish_x+1][finish_y+1] = col(0, "blue")
            ship_player[finish_x][finish_y+1] = col(0, "blue") 
        elif finish_x == 0 and finish_y == 9:
            ship_player[finish_x+1][finish_y] = col(0, "blue")
            for i in range (start_y , finish_y+1):
                ship_player[start_x+1][i] = col(0, "blue")
            ship_player[start_x+1][start_y] = col(0, "blue")
            ship_player[start_x+1][start_y-1] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
        elif start_x == 9 and start_y == 0:
            ship_player[finish_x-1][finish_y] = col(0, "blue")
            for i in range (start_y , finish_y):
                ship_player[start_x-1][i] = col(0, "blue")
            ship_player[finish_x-1][finish_y] = col(0, "blue")
            ship_player[finish_x-1][finish_y+1] = col(0, "blue")
            ship_player[finish_x][finish_y+1] = col(0, "blue")
        elif finish_x == 9 and finish_y == 9:
            for i in range (start_y , finish_y+1):
                ship_player[start_x-1][i] = col(0, "blue")
            ship_player[start_x-1][start_y-1] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
        elif start_x == 0:
            ship_player[finish_x+1][finish_y+1] = col(0, "blue")
            ship_player[finish_x][finish_y+1] = col(0, "blue")
            ship_player[start_x+1][start_y-1] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
            for i in range (start_y , finish_y+1):
                ship_player[start_x+1][i] = col(0, "blue")
        elif finish_x == 9:
            for i in range (start_y , finish_y+1):
                ship_player[start_x-1][i] = col(0, "blue")
            ship_player[finish_x - 1 ][finish_y+1] = col(0, "blue")
            ship_player[finish_x][finish_y+1] = col(0, "blue")
            ship_player[start_x-1][start_y-1] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
        elif start_x > 0 and start_x < 9 and start_y == 0:
            for i in range (start_y , finish_y+1):
                ship_player[start_x-1][i] = col(0, "blue")
                ship_player[start_x+1][i] = col(0, "blue")
            ship_player[start_x][finish_y+1] = col(0, "blue")
            ship_player[start_x-1][finish_y+1] = col(0, "blue")
            ship_player[start_x+1][finish_y+1] = col(0, "blue")
        elif start_x > 0 and start_x < 9 and finish_y == 9:
            for i in range (start_y , finish_y+1):
                ship_player[start_x-1][i] = col(0, "blue")
                ship_player[start_x+1][i] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
            ship_player[start_x-1][start_y-1] = col(0, "blue")
            ship_player[start_x+1][start_y-1] = col(0, "blue")
        else:
            for i in range (start_y , finish_y+1):
                ship_player[start_x-1][i] = col(0, "blue")
                ship_player[start_x+1][i] = col(0, "blue")
            ship_player[start_x][start_y-1] = col(0, "blue")
            ship_player[start_x-1][start_y-1] = col(0, "blue")
            ship_player[start_x+1][start_y-1] = col(0, "blue")
            ship_player[start_x][finish_y+1] = col(0, "blue")
            ship_player[start_x-1][finish_y+1] = col(0, "blue")
            ship_player[start_x+1][finish_y+1] = col(0, "blue")
    elif start_y == finish_y :
            if start_y == 0 and start_x == 0:
                for i in range (start_x , finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                ship_player[finish_x + 1][finish_y] = col(0, "blue")  
                ship_player[finish_x + 1][finish_y + 1] = col(0, "blue")  
                ship_player[finish_x][finish_y + 1] = col(0, "blue")  
            elif finish_y == 9 and start_x == 0:
                for i in range (start_x , finish_x+1):
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[finish_x + 1][finish_y] = col(0, "blue")  
                ship_player[finish_x + 1][finish_y - 1] = col(0, "blue")  
            elif start_y == 0 and finish_x == 9:
                for i in range (start_x , finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                ship_player[start_x - 1][finish_y] = col(0, "blue")  
                ship_player[start_x - 1][finish_y + 1] = col(0, "blue")
            elif finish_y == 9 and finish_x == 9:
                for i in range (start_x , finish_x+1):
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y] = col(0, "blue")
                ship_player[start_x-1][start_y-1] = col(0, "blue")
                ship_player[start_x][start_y-1] = col(0, "blue")
            elif  start_y == 0:
                for i in range(start_x, finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                ship_player[start_x - 1][start_y] = col(0, "blue")
                ship_player[start_x - 1][start_y+1] = col(0, "blue")
                ship_player[finish_x + 1][start_y] = col(0, "blue")
                ship_player[finish_x + 1][start_y+1] = col(0, "blue")
            elif finish_y == 9:
                for i in range(start_x, finish_x+1):
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y] = col(0, "blue")
                ship_player[finish_x+1][start_y] = col(0, "blue")
                ship_player[start_x-1][start_y-1] = col(0, "blue")
                ship_player[finish_x+1][start_y-1] = col(0, "blue")
            elif start_y > 0 and finish_y < 9 and start_x == 0:
                for i in range(start_x, finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[finish_x+1][start_y] = col(0, "blue")
                ship_player[finish_x+1][start_y-1] = col(0, "blue")
                ship_player[finish_x+1][start_y+1] = col(0, "blue")
            elif start_y > 0 and finish_y < 9 and finish_x == 9:
                for i in range(start_x, finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y] = col(0, "blue")
                ship_player[start_x-1][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y+1] = col(0, "blue")
            else:
                for i in range(start_x, finish_x+1):
                    ship_player[i][start_y+1] = col(0, "blue")
                    ship_player[i][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y] = col(0, "blue")
                ship_player[start_x-1][start_y-1] = col(0, "blue")
                ship_player[start_x-1][start_y+1] = col(0, "blue")
                ship_player[finish_x+1][start_y] = col(0, "blue")
                ship_player[finish_x+1][start_y-1] = col(0, "blue")
                ship_player[finish_x+1][start_y+1] = col(0, "blue")

def can_ship_be_hear(start_x, start_y, finish_x, finish_y, player_sea):
    if start_x - 1 >= 0:
        start_x -= 1
    if start_y - 1 >= 0:
        start_y -= 1
    if finish_x + 1 <= 9:
        finish_x += 1
    if finish_y + 1 <= 9:
        finish_y += 1
    can = True
    for i in range(start_x, finish_x+1):
        for j in range(start_y, finish_y + 1):
            if player_sea[i][j] == col(1, "green"):
                can = False
                break
        if not can:
            break
    return can

def ship_on_sea(start_x, start_y, finish_x, finish_y, sea_player):
    if start_x == finish_x:
        for i in range(start_y, finish_y+1):
            sea_player[start_x][i] = col(1, "green")
    elif start_y == finish_y :
        for i in range(start_x, finish_x+1):
            sea_player[i][start_y] = col(1, "green")
    else:
        return False
    
def min_max_cord(x, y, shots_matrix):
    direction = None
    if x == 0 and y == 0:
        if shots_matrix[x][y + 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
    elif x == 0 and y == 9:    
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
    elif x == 9 and y == 0:
        if shots_matrix[y+1][y] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"    
    elif x == 9 and y == 9:
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"   
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"
    elif  y == 0:
        if shots_matrix[x][y + 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"    
    elif y == 9:    
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"
    elif  x == 0: 
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x][y + 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
    elif x == 9:
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x][y + 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"
    else:    
        if shots_matrix[x][y - 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x][y + 1] == col(1, "green"):
            direction = "y"
        elif shots_matrix[x+1][y] == col(1, "green"):
            direction = "x"
        elif shots_matrix[x-1][y] == col(1, "green"):
            direction = "x"
    
    
    min_x, min_y = x, y
    max_x , max_y = min_x, min_y
    
    if direction == "x":
        while x-1  >= 0 and shots_matrix[x-1][y] == col(1, "green"):  
                min_x -= 1
                x-=1
        max_x = min_x
        while x + 1 < 10 and shots_matrix[x+1][y] == col(1, "green"): 
            max_x  += 1   
            x += 1
    elif direction == "y":    
        while y-1 >= 0 and shots_matrix[x][y-1] == col(1, "green"): 
            min_y -= 1
            y -=1
        max_y = min_y
        while y + 1 < 10 and shots_matrix[x][y+1] == col(1, "green"):
            max_y += 1
            y +=1
    elif direction is None:
        min_x, min_y = x, y
        max_x, max_y = x, y
    
    if min_x == max_x:
        len_ship = max_y-min_y 
    else:
        len_ship = max_x-min_x
    return min_x, min_y, max_x, max_y, len_ship + 1

def is_ship_kill(minx, miny, maxx, maxy, sea):
    kill = True
    if minx == maxx:
        for i in range(miny, maxy):
            if sea[minx][i] != col(1, "green"):
               kill =  False
               break 
    elif miny == maxy:
        for i in range(minx, maxx):
            if sea[miny][i] != col(1, "green"):
                kill = False
                break
    return kill

def kill_ship (minx, miny, maxx, maxy, atack):
    if minx == maxx:
            for i in range(miny, maxy+1):
                atack[minx][i] = col("x", "green")
                
    elif miny == maxy:
            for i in range(minx, maxx+1):
                atack[miny][i] = col("x", "green")





ship_player_1 = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
ship_player_2 = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
sea_player_1 = [[0 for _ in range(10)]for _ in range(10)]
sea_player_2 = [[0 for _ in range(10)]for _ in range(10)]
is_has_Ship_player_1 = True
print(col("Гравець 1 розтавляйте кораблі", "blue"))
print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
j = 1
for i in sea_player_2:
        print(j, *i)
        j +=1
while True:
    if len(ship_player_1) == 0:
        break
    #Отримання вхідних даних та їх обробка для зручніого подальшого працбвання з ними
    try:
        start_x, start_y, finish_x, finish_y = map(int,input(col("Введіть кординати початку та кординати кінця корабля: ", "blue")).split())
    except ValueError:
        print(col("Ви ввели щось не те!!!", "red"))
    if (start_x > 10 or start_y > 10 or finish_x > 10 or finish_y > 10) or (start_x < 1 or start_y < 1 or finish_x < 1 or finish_y < 1):
        print(col("Координати завеликі або замаленькі!!!", "red"))
        continue
    start_x -= 1
    start_y -= 1
    finish_x -= 1
    finish_y -= 1
    start_x, start_y, finish_x, finish_y = start_finish_swap(start_x, start_y, finish_x, finish_y)
    
    #Перевірка на правильність даних та їх коректність
    can_1 = True
    if start_x == finish_x:
        count_deck = finish_y - start_y + 1
    elif start_y == finish_y :
        count_deck = finish_x - start_x  + 1
    else: 
        can_1 = False
    if count_deck > 4 or  not can_1:
        print(col("Ви ввели щось не те!!!", "red"))
        continue
    try:
        ship_player_1.remove(count_deck)
    except ValueError:
        print(col("Всі кораблі такої довжини використані!!!", "red"))
        continue
    
    #Перевірка чи можна так розмістити корабель та його розміщення з заблокуванням клітинок
    can = can_ship_be_hear(start_x, start_y, finish_x, finish_y, sea_player_1)
    if can:
        ship_on_sea(start_x, start_y, finish_x, finish_y, sea_player_1)
        do_cell_none(start_x, start_y, finish_x, finish_y, sea_player_1)
    else: 
        print(col("Ви не можете так поставити корабель!!!", "red" ))
        continue
    
    #Вивід поля гравця з розміщеним на ньому кораблем
    print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
    j = 1
    for i in sea_player_1:
        print(j, *i)
        j +=1

print(col("Гравець 2 розтавляйте кораблі", "blue"))
print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
j = 1
for i in sea_player_2:
        print(j, *i)
        j +=1
while True:
    if len(ship_player_2) == 0:
        break
    #Отримання вхідних даних та їх обробка для зручніого подальшого працбвання з ними
    try:
        start_x, start_y, finish_x, finish_y = map(int,input(col("Введіть кординати початку та кординати кінця корабля: ", "blue")).split())
    except ValueError:
        print(col("Ви ввели щось не те!!!", "red"))
        continue
    if (start_x > 10 or start_y > 10 or finish_x > 10 or finish_y > 10) or (start_x < 1 or start_y < 1 or finish_x < 1 or finish_y < 1):
        print(col("Координати завеликі або замаленькі!!!", "red"))
        continue
    start_x -= 1
    start_y -= 1
    finish_x -= 1
    finish_y -= 1
    start_x, start_y, finish_x, finish_y = start_finish_swap(start_x, start_y, finish_x, finish_y)
    
    #Перевірка на правильність даних та їх коректність
    can_1 = True
    if start_x == finish_x:
        count_deck = abs(start_y - finish_y) + 1
    elif start_y == finish_y :
        count_deck = abs(start_x - finish_x) + 1
    else: 
        can_1 = False
    can = can_ship_be_hear(start_x, start_y, finish_x, finish_y, sea_player_2)
    if count_deck > 4 or  not can_1:
        print(col("Ви ввели щось не те!!!", "red"))
        continue
    try:
        ship_player_2.remove(count_deck)
    except ValueError:
        print(col("Всі кораблі такої довжини використані!!!", "red"))
        continue
    
    #Перевірка чи можна так розмістити корабель та його розміщення з заблокуванням клітинок
    if can:
        ship_on_sea(start_x, start_y, finish_x, finish_y, sea_player_2)
        do_cell_none(start_x, start_y, finish_x, finish_y, sea_player_2)
    else: 
        print(col("Ви не можете так поставити корабель!!!", "red"))
        continue
    
    #Вивід поля гравця з розміщеним на ньому кораблем
    print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
    j = 1
    for i in sea_player_2:
        print(j, *i)
        j +=1
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")



alive_ship_player_1 = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
alive_ship_player_2 = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
atack_player_1 = [[0 for _ in range(10)]for _ in range(10)]
atack_player_2 = [[0 for _ in range(10)]for _ in range(10)]
turn = 1
while True:
    if len(alive_ship_player_1) == 0:
        print(col("Вітаю гравець номер 2 переміг!!!!", "green"))
        break  
    elif len(alive_ship_player_2) == 0:
        print(col("Вітаю гравець номер 1 переміг!!!!", "green"))
        break 
    try:
        x_atack, y_atack = map(int,input(col(f"Хід гравця номер: {turn}, введіть кординати пострілу", "green")).split())
    except ValueError:
        print(col("Ви ввели щось не те", "green"))
        continue
    if x_atack < 1 or x_atack > 10 or y_atack < 1 or y_atack > 10:
        print(col("Координати завеликі або замаленькі!!!", "green"))
        continue
    x_atack -=1
    y_atack -=1
    if turn == 1:
        if sea_player_2[x_atack][y_atack] == col(1, "green"):
            minx, miny, maxx, maxy, len_ship = min_max_cord(x_atack, y_atack, sea_player_2)
            kill = is_ship_kill(minx, miny, maxx, maxy, atack_player_1)
            if kill:
                print(col("Вбив", "green"))
                atack_player_1[x_atack][y_atack] = col(1, "green")
                do_cell_none(minx, miny, maxx, maxy, atack_player_1)
                alive_ship_player_2.remove(len_ship)
                kill_ship(minx, miny, maxx, maxy, atack_player_1)
                print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
                j = 1
                for i in atack_player_1:
                    print(j, *i)
                    j +=1
            else:
                atack_player_1[x_atack][y_atack] =  col(1, "green")
                print(col("Влучив", "blue"))
                print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
                j = 1
                for i in atack_player_1:
                    print(j, *i)
                    j +=1
        else:
            print(col("Промах", "red"))
            atack_player_1[x_atack][y_atack] = col(0, "red")
            turn = 2
            j = 1
            for i in atack_player_1:
                print(j, *i)
                j +=1
    else:
        if sea_player_1[x_atack][y_atack] == col(1, "green"):
            minx, miny, maxx, maxy, len_ship = min_max_cord(x_atack, y_atack, sea_player_1)
            kill = is_ship_kill(minx, miny, maxx, maxy, atack_player_2)
            if kill:
                    print(col("Вбив", "green"))
                    atack_player_2[x_atack][y_atack] = col(1, "green")
                    do_cell_none(minx, miny, maxx, maxy, atack_player_2)
                    alive_ship_player_1.remove(len_ship)
                    kill_ship(minx, miny, maxx, maxy, atack_player_2)
                    print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
                    j = 1
                    for i in atack_player_2:
                        print(j, *i)
                        j +=1
            else:   
                    print(col("Влучив", "blue"))
                    atack_player_2[x_atack][y_atack] = col(1, "green")
                    j = 1
                    for i in atack_player_2:
                        print(j, *i)
                        j +=1
        else:
                print(col("Промах", "red"))
                atack_player_2[x_atack][y_atack] = col(0, "red")
                turn = 1
                j = 1
                for i in atack_player_2:
                    print(j, *i)
                    j +=1
