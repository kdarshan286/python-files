import tkinter as tk
from tkinter import messagebox
import threading
import time

class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Reminder")
        self.root.geometry("300x200")
        self.interval = 60 * 60  # 1 hour by default

        tk.Label(root, text="Set Reminder Interval (minutes):").pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.insert(0, "60")

        self.start_button = tk.Button(root, text="Start Reminders", command=self.start_reminder)
        self.start_button.pack(pady=10)

        self.running = False

    def start_reminder(self):
        try:
            minutes = int(self.entry.get())
            self.interval = minutes * 60
            if not self.running:
                self.running = True
                threading.Thread(target=self.reminder_loop, daemon=True).start()
                messagebox.showinfo("Started", f"Water reminder set for every {minutes} minutes.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reminder_loop(self):
        while self.running:
            time.sleep(self.interval)
            self.show_notification()

    def show_notification(self):
        messagebox.showinfo("Hydration Reminder", "Time to drink water!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()
