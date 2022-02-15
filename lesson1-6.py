way = int(input("Введите результаты пробежки первого дня в км "))
way_X = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = way
while result_km < way_X:
        way = way + 0.1 * way
        result_days += 1
        result_km = result_km + way
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
