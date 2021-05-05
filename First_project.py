#Bismillah
#Notification Reminder Project
import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Alhamdulillah",
            message = "My First Python Project "
                        "I Would Like to Thank Almighty For "
                        "This Very First Project "
                        "I am Blessed",
                timeout = 20
            )
        time.sleep(7)