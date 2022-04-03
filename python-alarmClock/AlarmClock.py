import os;os.system('cls')
import tkinter as tk
from tkinter.messagebox import showinfo
window = tk.Tk()
window.geometry("300x180")
window.resizable(False,False)
###Get the alarm time from the user
Format = [
"12",
"24"
]
Form = tk.StringVar(window)
Form.set(Format[0])
hrformat=tk.OptionMenu(window,Form,*Format)
Hour = tk.StringVar(window)
Min = tk.StringVar(window)
entry_Hour = tk.Entry(window, textvariable=Hour,width=5)
entry_Min = tk.Entry(window, textvariable=Min,width=5)
hrformat.grid(row=1,column=1)
hrformat.pack(padx=5, pady=15, side=tk.LEFT)
entry_Hour.pack(padx=5, pady=20, side=tk.LEFT)
entry_Min.pack(padx=5, pady=25, side=tk.LEFT)


def ErrorMsg():
    """ callback when the login button clicked
    """
    msg = f'Incorrect Details entered'
    showinfo(
        title='Error',
        message=msg
    )

def SuccessMsg():
    """ callback when the login button clicked
    """
    msg = f'Alarm set for {Hour.get()} : {Min.get()}'
    showinfo(
        title='Success',
        message=msg
    )
    window.destroy()

def ok():
    format = int(Form.get())
    hr,min = Hour.get(),Min.get()
    hr = 0 if hr == '' else int(hr)
    min = 0 if min == '' else int(min)
    print(Hour.get() + ':' + Min.get())
    # print(min)
    # print(hr)
    # print(format)
    if min > 59 or min < 0:
        print('Invalid Minutes')
        ErrorMsg()
    else:
        print('Valid format of minutes')

    if format == 12:
        print('12 format')
        if hr > 12 or hr < 1 :
            print('Invalid Hours')
            ErrorMsg()
        else:
            print('Valid format of hour')
            SuccessMsg()
        # return (hr < 13 or hr > 0) and (min < 59 or min >= 0)
    else:
        print('24 format')
        if hr > 24 or hr < 0 :
            print('Invalid Hours')
            ErrorMsg()
        else:
            print('Valid format of hour')
            SuccessMsg()



button = tk.Button(window, text="Set the Alarm", command=ok)

button.pack(padx=5, pady=25,side=tk.LEFT)

window.mainloop()

def RunAlarm():
    from playsound import playsound

    # for playing note.wav file
    playsound('audio.wav')
    print('playing sound using  playsound')


def RunTheTimer(alarmTime):
    val=alarmTime.split(":")
    import datetime,time
    now = datetime.datetime.now()
    month=now.month
    year=now.year
    day=now.day
    b = datetime.datetime(year, month, day, int(val[0]), int(val[1]), 00)
    c=b-now
    time.sleep(c.total_seconds())
    RunAlarm()

d=Hour.get()+':'+Min.get()
RunTheTimer(d)
