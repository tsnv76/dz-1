time_duration = int(input('Введите количество секунд>'))
seconds = str(60 - time_duration % 60)
minutes = str(59 - time_duration // 60 % 60)
hours = str(24 - time_duration // 3600 % 24)
day = str(30 - time_duration // 86400 % 31)
week = str(6 - time_duration // 86400 % 7)
month = str(30 - time_duration // 86400 % 31)
year = str(11 - time_duration // 86400 % 12)

print('До минуты: ' + seconds + ' секунд')
print('До часа: ' + minutes + ' минут и ' + seconds + ' секунд')
print('До суток: ' + hours + ' часов и ' + minutes + ' минут и ' + seconds + ' секунд')
print('До недели: ' + week + ' дней ' + hours + ' часов и ' + minutes + ' минут и ' + seconds + ' секунд')
print('До месяца: ' + day + ' дней ' + hours + ' часов и ' + minutes + ' минут и ' + seconds + ' секунд')
print('До года: ' + year + ' месяцев ' + day + ' дней ' + hours + ' часов и ' + minutes + ' минут и ' + seconds + ' секунд')

