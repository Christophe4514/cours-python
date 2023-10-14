# les classes date, time et datetime

from datetime import date, time, datetime

print(date(year=2001, month=8, day=18))
print(time(hour=22, second=45, minute=30))
print(datetime(year=2001, month=8, day=18,hour=22, second=45, minute=30))

print(datetime.now())
print(datetime.today())

now = datetime.now()
print(f"{now.hour}  {now.minute}  {now.second}")

today = date.today()
tomorrow = today.replace(day=today.day + 1)

print(tomorrow)

# inconvenient de replace est qu'il ne prends pas en charge le fuseau horraire et le passage d'été

# creer date à partir de chaine de caractère
# utiliser la norme ISO8601 YYYY-MM-DD

date_formater = date.fromisoformat("2001-08-18")
print(date_formater)

# avec une chaine tq: 22 oct 2021 on peut utiliser strptime"date"
# stringftime.org

date_forma = datetime.strptime("22 Oct 2021", "%d %b %Y")
print(date_forma)

today_format = today.strftime("%d %B %Y")
print(today_format)

# module dateutil et parser

from dateutil import parser

a = parser.parse("18 August 2001")
print(a)
# on peut aussi utiliser dateparser à installer depuis pip
# import dateparser
# dateparser.parse("aujourd'hui")
# demain, hier, il y a un mois, ... pas de limite