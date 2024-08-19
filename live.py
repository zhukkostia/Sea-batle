from termcolor import colored as col
import time
def count_alive_neighbor(world, i , j):
     count = 0
     if i == 0 and j == 0:   
          if world[i+1][j] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1
          if world[i+1][j+1] == 1:
               count+=1
     elif i == 19 and j == 19:   
          if world[i-1][j] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1
          if world[i-1][j-1] == 1:
               count+=1
     elif i == 0 and j == 19:    
          if world[i+1][j] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1
          if world[i+1][j-1] == 1:
               count+=1
     elif i == 19 and j == 0:
          if world[i-1][j] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1
          if world[i-1][j+1] == 1:
               count+=1    
     elif i == 0:     
          if world[i+1][j] == 1:
               count+=1 
          if world[i+1][j-1] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1    
          if world[i+1][j+1] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1
     elif i == 19:     
          if world[i-1][j] == 1:
               count+=1 
          if world[i-1][j-1] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1    
          if world[i-1][j+1] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1
     elif j == 0:
          if world[i+1][j] == 1:
               count+=1 
          if world[i+1][j+1] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1    
          if world[i-1][j+1] == 1:
               count+=1
          if world[i-1][j] == 1:
               count+=1
     elif j == 19:
          if world[i+1][j] == 1:
               count+=1 
          if world[i+1][j-1] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1    
          if world[i-1][j-1] == 1:
               count+=1
          if world[i-1][j] == 1:
               count+=1          
     else:     
          if world[i+1][j] == 1:
               count+=1
          if world[i][j-1] == 1:
               count+=1     
          if world[i+1][j+1] == 1:
               count+=1
          if world[i][j+1] == 1:
               count+=1
          if world[i+1][j-1] == 1:
               count+=1
          if world[i-1][j-1] == 1:
               count+=1     
          if world[i-1][j+1] == 1:
               count+=1
          if world[i-1][j] == 1:
               count+=1
     return count


world = matrix = [[0 for _ in range(20)] for _ in range(20)]

print(col("""Натисніть "Enter" коли введете всі данні""", "blue"))
try:
    while True:
        x, y = map(int, input().split())
        world[x-1][y-1] = 1
        for i in world:
               print(*[col(cell, 'green') if cell == 1 else col(cell, 'red') for cell in i])
except ValueError:
    print(col("Дані прийняті, починається генерація", "blue"))

rows = 20
generation = 1
while True:
    new_world = [[0 for _ in range(20)] for _ in range(20)]
    change = False
    for i in range(rows):
            for j in range(rows):
               count_neighbor_alive = 0
               count_neighbor_alive = count_alive_neighbor(world, i , j)
               if world[i][j] == 1:
                    if count_neighbor_alive == 2 or count_neighbor_alive == 3:
                         continue
                    else:
                         new_world[i][j] = 0
                         change = True
               elif world[i][j] == 0 and count_neighbor_alive == 3:
                    new_world[i][j] = 1
                    change = True
    world = new_world
    
    print(col(f"""Покоління: {generation}""", "blue"))
    generation += 1
    for i in world:
        print(*[col(cell, 'green') if cell == 1 else col(cell, 'red') for cell in i])
    if not change:
         print(col("Гра завершена", "blue"))
         break
    time.sleep(3)          