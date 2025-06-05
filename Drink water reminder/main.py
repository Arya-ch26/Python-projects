import time
from plyer import notification

try:
    while True:
        print("Please drink some water!")
        notification.notify(
            title="Please drink some water",
            message="You need to drink some water",
        )
        time.sleep(10)
except KeyboardInterrupt:
    print("\nStopped hydration reminder. Stay healthy! 💧")
