train_num = input("Введіть номер поїзду: ")
train_sending_hour = int(input("Введіть годину відправки: "))
train_sending_minute = int(input("Введіть хвилину відправки: "))
train_duration = int(input("Введіть тривалість поїздки у хвилинах: "))

duration_in_sec = train_duration * 60 #Отримуємо довжину поїздки в секундах
sending_hour_in_sec = train_sending_hour * 3600 #
sending_minute_in_sec = train_sending_minute * 60
sending_time = sending_hour_in_sec + sending_minute_in_sec

#12 30 - відпр 12* 3600 + 30 * 60 = 
arrival_time = sending_time + duration_in_sec

arrival_hour = arrival_time // 3600
arrival_minute = (arrival_time - arrival_hour * 3600) // 60

if arrival_hour >= 24:
    day_shift = arrival_hour//24
    arrival_hour = arrival_hour - 24*(day_shift)


if arrival_minute >= 60:
    arrival_hour += arrival_minute//60
    arrival_minute -= 60*(arrival_minute//60)
   

print(f"TRAIN: {train_num}")
print(f"DAY SHIFT: {day_shift}")
print(f"ARRIVAL TIME: {arrival_hour} {arrival_minute}")