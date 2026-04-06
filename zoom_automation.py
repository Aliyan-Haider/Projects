from pywinauto.application import Application
from pathlib import Path

zoom_path = str(Path.home() / "AppData" / "Roaming" / "Zoom" / "bin" / "Zoom.exe")
win = Application(backend="uia").start(zoom_path)
win = Application(backend="uia").connect(title="Zoom Workplace", timeout=20)

join_meeting = win.ZoomWorkplace.child_window(title="Join a meeting", control_type="Button").wrapper_object()
join_meeting.click_input()