# zoneinfo
from datetime import datetime

now = datetime.now() #naive (pas d'info de fuseau horraire)

print(now.tzinfo)

from zoneinfo import ZoneInfo

now_in_drc = datetime.now(tz=ZoneInfo("America/Newyork"))
print(now_in_drc) #aware (a info de fh)