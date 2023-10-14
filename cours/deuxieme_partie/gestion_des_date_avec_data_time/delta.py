from datetime import timedelta
from datetime import datetime

delta = timedelta(days=30)

now = datetime.now()

now_in_15_days = now + timedelta(days=15, hours=-5)

print(now)

print(now_in_15_days)

from dateutil.relativedelta import relativedelta

lelo = datetime.now()

lelo_dans_2_mois = now + relativedelta(months=5)

print(lelo)
print(lelo_dans_2_mois)