try:
    from win10toast import ToastNotifier

    def notify(title, msg):
        toaster = ToastNotifier()
        toaster.show_toast(title, msg, duration=10)
except:
    def notify(title, msg):
        print(f"ALERT: {title} - {msg}")
