import datetime



def get_to_past(n):
    today = datetime.datetime.fromtimestamp(n)
    two_weeks_ago = today - datetime.timedelta(weeks=2)
    return two_weeks_ago
n = float(input())
print(get_to_past(n))

