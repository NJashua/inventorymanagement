month = input("Enter the month: ").lower()
day = int(input("Enter the day: "))

if month in ('january', 'february', 'march'):
    season = 'winter'
elif month in ('april', 'may', 'june'):
    season = 'spring'
elif month in ('july', 'august', 'september'):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'march' and day > 19) or (month == 'june' and day < 21):
    season = 'spring'
elif (month == 'june' and day > 20) or (month == 'september' and day < 22):
    season = 'summer'
elif (month == 'september' and day > 21) or (month == 'december' and day < 21):
    season = 'autumn'
elif (month == 'december' and day > 20) or (month == 'march' and day < 20):
    season = 'winter'

print("The season is", season)
