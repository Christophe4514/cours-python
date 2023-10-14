from zoneinfo import ZoneInfo
from datetime import datetime

utc = ZoneInfo("UTC")
montreal_tz = ZoneInfo('America/Montreal')

march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_10 = datetime(year=2020, month=3, day=10, hour=13, minute=0, second=0, tzinfo=montreal_tz)
march_7_utc = march_7.astimezone(utc)
march_10_utc = march_10.astimezone(utc)

print(march_10 - march_7)
print(march_10_utc - march_7_utc)