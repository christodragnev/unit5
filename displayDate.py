#Christo Dragnev
#4/26/18
#displayDate.py

from datetime import date
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

today = date.today()


today.day
today.month
today.year
today.weekday()

print('Today is ', days[today.weekday()], ',', months[today.month-1], today.day, today.year)