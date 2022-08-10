
res = int(input("Введите выручку:"))
costs = int(input("Укажите издержки"))
profit = res-costs

if profit>0:
    print(f"Вы в прибыли. Его велина - {profit}")

    rent = profit/res
    print(f"Рентабельность ={rent}")
    emp_number = int(input("Сколько у вас работников :"))
    emp_prof = profit/emp_number
    print(f"Прибыль на одного работка составляет:{emp_prof}")
elif profit<0:
    print(f"Вы в убытках. Его величина-{profit}")
else:
   print(f"У вас нулевой показатель")