from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    print("💧 Please drink some water!")
    toaster.show_toast("Hydration Reminder", "Time to drink water!", duration=5, threaded=True)
    time.sleep(60 * 30)  # every 30 minutes
