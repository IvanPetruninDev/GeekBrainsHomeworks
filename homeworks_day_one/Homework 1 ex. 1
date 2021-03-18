duration = int(input('Введите секунды: '))

min = duration // 60
hour = min // 60
day = hour // 24
month = day // 30
year = month // 12

if duration >= 0:
    if duration < 60:
        print(str(duration) + ' сек')
    elif 0 < min < 60:
        seconds = duration - (min * 60)
        print(str(min) + ' минут ' + (str(seconds) + ' секунд'))
    elif 0 <  hour < 24:
        seconds = duration - (min * 60)
        minutes = min - (hour * 60)
        print(str(hour) + ' часов ' + (str(minutes) + ' минут ' + (str(seconds) + ' секунд')))
    elif 0 < day < 30:
        seconds = duration - (min * 60)
        minutes = min - (hour * 60)
        hours = hour - (day * 24)
        print(str(day) + ' дней ' + (str(hours) + ' часов ' + (str(minutes) + ' минут ' + (str(seconds) + ' секунд'))))
    elif 0 < month < 12:
        seconds = duration - (min * 60)
        minutes = min - (hour * 60)
        hours = hour - (day * 24)
        days = day - (month * 30)
        print(str(month) + ' месяцев ' + (str(days) + ' дней ' + (str(hours) + ' часов ' + (str(minutes) + ' минут ' + (str(seconds) + ' секунд')))))
    elif year > 0:
        seconds = duration - (min * 60)
        minutes = min - (hour * 60)
        hours = hour - (day * 24)
        days = day - (month * 30)
        months = month - (year * 12)
        print(str(year) + ' лет ' + (str(months) + ' месяцев ' + (str(days) + ' дней ' + (str(hours) + ' часов ' + (str(minutes) + ' минут ' + (str(seconds) + ' секунд'))))))

else:
    print('Введите не отрицательное число')
