from tkinter import *
from tkinter import messagebox
import threading
from time import *

#initialize window
root = Tk()
root.geometry('1000x550')
root.resizable(0, 0)
root.configure(bg="black")
root.title("Water Reminder")
Label(root, text ='Water Reminder', font = 'arial 30 bold', bg="black",fg='#424242').pack()
class sleeping():
    def sleep():
        time.sleep(2)
def water_reminder():
    interval = 60 * 60  # 1 hour by default

    Label(root, text="Set Reminder Interval (minutes):").pack(pady=10)
    global Entry
    Entry=Entry(root,width=10).pack()
    if Entry==None:
        Entry='1'
    start_button=Button(root, text="Start Reminders", command=start_reminder)
    start_button.pack(pady=10)
    global running
    running = False

def start_reminder():
    try:
        global Entry
        global interval
        minutes = int(Entry)
        interval = minutes * 60
        global running
        if not running:
            running = True
            messagebox.showinfo("Started", f"Water reminder set for every {minutes} minutes.")
        while running:
                sleeping.sleep()
                show_notification()    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def Reset():
    Entry.set("")
    water_reminder()      

def show_notification(self):
    messagebox.showinfo("Hydration Reminder", "Time to drink water!")
##    restart_button=Button(root, text="Start Reminder again",width=10, command=Reset).place(x=90, y = 410)
def Exit():
    root.destroy()
water_reminder()
