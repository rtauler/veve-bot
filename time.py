# import the time module
import time
import datetime

target_hour = int(input('Enter hour, format 9/20, no 0 in front: '))
target_min = int(input('Enter minute, format 1/42, no 0 in front: '))

# target_hour = 19
# target_min = 17

# print(now.hour, now.minute, now.second)

while True:
    now = datetime.datetime.now()
    if target_hour is not now.hour:
        print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second), end="\r")
    elif target_hour is now.hour and target_min is not now.minute:
        print(
            'target_hour is true!',
            str(now.hour) + ":" + str(now.minute) + ":" + str(now.second),
            end="\r",
        )
    elif target_hour is now.hour and target_min is now.minute:
        print(
            'target_hour is true!',
            'target_min is true!',
            str(now.hour) + ":" + str(now.minute) + ":" + str(now.second),
            end="\r",
        )
        print('fire in the hole!')
        break
