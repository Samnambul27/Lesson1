print('Привет, Я программа занимательные конвектор, могу по количеству секунд сказать сколько это время')
u_sec = int(input('Введи время в секундах: '))
hour = u_sec//3600
sec = u_sec%3600
min = sec//60
sec = sec%60
print('Получилось', hour, ':', min, ':', sec)
