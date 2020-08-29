# seconds = int(input('Please, enter how many seconds:'))
#
# hours = (seconds // 3600) % 24
# minutes = (seconds // 60) % 60
# seconds = seconds % 60
#
# print('{0}:{1:=02}:{2:=02}'.format(hours, minutes, seconds))


# Solution from teacher

time = int(input("Enter time in seconds: "))

hours = time //3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')


