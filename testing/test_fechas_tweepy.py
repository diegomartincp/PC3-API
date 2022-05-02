from datetime import datetime, timedelta

date_ahora = d = datetime.today()
date_anterior = d = datetime.today() - timedelta(days=5) #Restamos un dia

print(date_ahora.strftime("%Y%m%d%H%M"))
print(date_anterior.strftime("%Y%m%d%H%M"))