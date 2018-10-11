from datetime import date, timedelta

def touslesvendredis(annee):
   d = date(annee, 1, 1)                    
   d += timedelta(days = 4 - d.weekday())  
   while d.year == annee:
      d += timedelta(days = 7)
      print (d)

