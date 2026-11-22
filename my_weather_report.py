city = input("Enter your city name:")
temp = float(input("Enter today's temperature in C:"))
if temp > 35:
    print("Warning: It is very hot today!")
if temp > 25:
    print("Great day to go outside!")
else:
    print("grab a jacket and before you go outside!")
if temp > 35:
    print("Weather: Scorching Hot ")
elif temp > 25:
    print("Weather: Warm and Sunny")
elif temp > 55:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - Stay warm")

import datetime
import calendar
from zoneinfo import ZoneInfo
now = datetime.datetime.now(ZoneInfo("America/New_York"))
print("City:" , city)
print("Time now:", now)
print(calendar.calendar(now.year))
