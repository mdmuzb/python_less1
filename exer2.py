total = int(input("Введите время секундах= "))
hours = int(total/3600)
minuts = int((total-3600)/60)
secs = total-hours-minuts

print(f"Врем в формате чч:мм:сс - {hours}:{minuts}:{secs}")
