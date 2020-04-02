import win32api

def moveMouse(x, y):
    win32api.SetCursorPos((x, y))

