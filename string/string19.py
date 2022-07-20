'''
Given a day, print 'yes' if it is a holiday otherwise print'no'.Assume that weekend days are holidays
Sample Testcase :
INPUT
saturday
OUTPUT
yes
INPUT
monday
OUTPUT
no
'''


def holidays(day: str):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    holiday = ['sunday', 'saturday']
    if day in holiday:
        print("It's holiday")
    elif day not in days and day not in holiday:
        print("It's not a day in weekdays")
    else:
        print("It's not holiday")


print('Pls enter day in small case')
day = input('Enter the a day:')

if __name__ == "__main__":
    holidays(day)
