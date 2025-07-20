from datetime import datetime, date, timedelta

def get_days_from_today(date):
    try:
        datetime_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        difference = today_date - datetime_date
        return difference.days
    except ValueError:
        print("Ви ввели дату у неправильному форматі. Потрібно: '%Y-%m-%d'")

print(get_days_from_today("2021-10-09"))