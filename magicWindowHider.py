import win32gui, win32con
while True: win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)