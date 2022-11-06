#Necessary Imports
import psutil
from plyer import notification


def clearNotifications(self):         
        '''
        Clears all messages in the notification bar.
        '''
        if self._notifBar:
            self._notifBar.clear()


#Created variabled with imbedded psutil variables
battery = psutil.sensors_battery()
percent = battery.percent

#Calculating the needed subtraction to alert @ 15%
wantedNum = percent - 15

print("You will be notified at 15%")
#Prompting and getting frequency
# print("Enter " + wantedNum)
# freq = int(input("to alert at 15%: "))

#Calculating frequency
while(True):
    battery = psutil.sensors_battery()
    current_percent = battery.percent
    change = current_percent - percent
    diff = abs(change)

    if(diff>= wantedNum):
        notification.notify(
            title = "Current Battery Percentage",
            message = str(current_percent) + "% Battery Remaining",
            timeout = 5 
            )

        percent = current_percent
    continue

