import datetime

str = '2012-11-19'
date_time = datetime.datetime.strptime(str, '%Y-%m-%d')
print(date_time)
