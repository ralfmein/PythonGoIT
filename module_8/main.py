from datetime import date, timedelta


def get_birthdays_per_week(users):
    today = date.today()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    for user in users:
        name = user['name']
        birthday = user['birthday']
        print(name, birthday)

        if start_of_week <= birthday <= end_of_week:
            day_of_week = birthday.strftime('%A')
            if day_of_week in birthdays_per_week:
                birthdays_per_week[day_of_week].append(name)
            else:
                birthdays_per_week['Monday'].append(name)

    birthdays_per_week = {key: value for key, value in birthdays_per_week.items() if value}
    return birthdays_per_week
