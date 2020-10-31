# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_time = int(input('Введите время в секундах: '))
get_hour = user_time // 3600
get_minute = (user_time // 60) % 60
get_second = user_time % 60
print(f'Время: {get_hour:02}:{get_minute:02}:{get_second:02}')
