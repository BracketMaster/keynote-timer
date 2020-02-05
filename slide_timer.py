import wx
from time import time

start = time()
slide = 0
old_time_elapsed = 0
print("| Slide | Start Time | End Time |")
print("| ----- | ---------- | -------- |")

def onButton(event):
    time_elapsed = time() - start
    global slide
    global old_time_elapsed
    slide = slide + 1
    start_time = f"{int(old_time_elapsed//60)}:{int(old_time_elapsed%60)}"
    end_time = f"{int(time_elapsed//60)}:{int(time_elapsed%60)}"
    print(f"| {slide} | {start_time} | {end_time} |")
    old_time_elapsed = time_elapsed

app = wx.App()
frame = wx.Frame(None, -1, 'Slide Timer')
frame.SetSize(200,200)

panel = wx.Panel(frame, wx.ID_ANY)
button = wx.Button(panel, wx.ID_ANY, 'Advance Slide', (10, 10))
button.Bind(wx.EVT_BUTTON, onButton)

frame.Show()
frame.Centre()
app.MainLoop()in() 

