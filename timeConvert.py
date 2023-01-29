from datetime import datetime
s = 1014163200

print(datetime.utcfromtimestamp(s).strftime('%d.%m.%Y'))
