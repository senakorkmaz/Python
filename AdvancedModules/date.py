#from datetime import datetime
import datetime

#hangi fonksiyonlar var görebilmek için
result = dir(datetime.datetime)
#print(result)
dateNow = datetime.datetime.now()
print(dateNow)
print(dateNow.year,dateNow.month,dateNow.day,dateNow.hour,dateNow.minute,dateNow.second)
print(datetime.datetime.ctime(dateNow))
print('--------------------------------')
print(datetime.datetime.strftime(dateNow,'Weekday, short version: %a'))
print(datetime.datetime.strftime(dateNow,'Weekday, full version: %A'))
print(datetime.datetime.strftime(dateNow,'Weekday as a number: %w'))
print(datetime.datetime.strftime(dateNow,'Day of month 01-31: %d'))
print(datetime.datetime.strftime(dateNow,'Month name, short version: %b'))
print(datetime.datetime.strftime(dateNow,'Month name, full version: %B'))
print(datetime.datetime.strftime(dateNow,'Month as a number 01-12: %m'))
print(datetime.datetime.strftime(dateNow,'Year, short version, without century: %y'))
print(datetime.datetime.strftime(dateNow,'Year, full version: %Y'))
print(datetime.datetime.strftime(dateNow,'Hour 00-23: %H'))
print(datetime.datetime.strftime(dateNow,'Hour 00-12: %I'))
print(datetime.datetime.strftime(dateNow,'AM/PM: %p'))
print(datetime.datetime.strftime(dateNow,'Minute 00-59: %M'))
print(datetime.datetime.strftime(dateNow,'Week number of year, Sunday as the first day of week, 00-53: %U'))
print(datetime.datetime.strftime(dateNow,'Week number of year, Monday as the first day of week, 00-53: %W'))
print(datetime.datetime.strftime(dateNow,'Local version of date and time: %c'))
print(datetime.datetime.strftime(dateNow,'Local version of date: %x'))
print(datetime.datetime.strftime(dateNow,'Local version of time: %X'))
t= '21 April 2019 hour 10:12:30'
result = datetime.datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(result)
print(result.year)

birthday = datetime.datetime(2000,5,15)
print(birthday)

result = datetime.datetime.timestamp(birthday) #saniye
print(result)
result = datetime.datetime.fromtimestamp(result)
print(result)
result = datetime.datetime.fromtimestamp(0)