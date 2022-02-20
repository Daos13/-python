
duration = int(input('Промежуток времени: '))
#
if duration >=1 and duration <=60:
    print(duration, 'сек')
if duration >=60 and duration <=3600:
    m = duration // 60
    s = duration % 60
    print(m, 'мин ', s, 'сек')
if duration >=3600 and duration <=86400:
    h = duration // 3600
    m = duration % 3600 // 60
    s = duration % 3600 % 60
    print(h, 'час', m, 'мин', s, 'сек')
if duration >=86400 and duration <=2592000:
    d = duration // 86400
    h = duration % 86400 // 3600
    m = duration % 86400 % 3600 // 60
    s = duration % 86400 % 3600 % 60

    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')

