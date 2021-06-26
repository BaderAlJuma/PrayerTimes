from prayertime import *
from datetime import *
print("Current Date: ",datetime.today().year, datetime.today().month, datetime.today().day)
print()
pt = Prayertime(47.9774, 29.3759, 3, datetime.today().year, datetime.today().month, datetime.today().day, Calendar.MuslimWorldLeague, Mazhab.Default, Season.Winter)
pt.calculate()
pt.report()

print("Prayer times from top to bottom: Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha.")
print("All timings are based on Kuwait City.")
print()
timeNoPm = pt.fajr_time().split()[0]
hour = int(timeNoPm.split(':')[0])
clean = pt.fajr_time()[1:]
cleanNoPm = pt.fajr_time()[1:-2]
inHour= int(input("How many hours would you like to sleep before Fajr?"))
sub= inHour - hour
if inHour < hour:
    result= str(hour-inHour)+ clean
elif sub==0:
    result= "12"+ clean
else:
    result= str(12 - sub) + cleanNoPm + "PM"
    
print("You should sleep at "+ result)
