import holidays

year = 2024
tw_holidays = holidays.TW(years=year)

for date, name in tw_holidays.items():
    print(f"{date}: {name}")

year = 2025
tw_holidays = holidays.TW(years=year)

for date, name in tw_holidays.items():
    print(f"{date}: {name}")