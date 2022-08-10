a = int(input("Введите начальную дистанцию:"))
b = int(input("Введите финальную дистанцию:"))
day_count = 1

while a<b:
   day_count +=1
   a*=1.1
   print(f" {a} км")
print(f"на {day_count} день спортсмен достигнет больше {b} км")