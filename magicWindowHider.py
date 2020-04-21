import win32gui, win32con
while True:
	The_program_to_hide = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)