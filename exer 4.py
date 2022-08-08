number = input("Введите число:")
count = int(len(number))
max=0
for i in range(0,count):
    tmp = int(number[i])
    if tmp>max:
        max = tmp
print(max)
