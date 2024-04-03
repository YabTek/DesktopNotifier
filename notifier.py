import tkinter as tk
from plyer import notification

def notify():
    notification.notify(
        title="Hello, World!",
        message="This is a desktop notification.",
        app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
        timeout=200,  # seconds
    )
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Click the button below to receive notifications")
label.pack()

button = tk.Button(frame, 
                   text="Notify", 
                   fg="red",
                   font=("Arial", 16),
                   command=notify)

button.pack(side=tk.LEFT, padx=20, pady=20, ipadx=10, ipady=10)

root.mainloop()