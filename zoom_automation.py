from pywinauto.application import Application
from pathlib import Path

zoom_path = str(Path.home() / "AppData" / "Roaming" / "Zoom" / "bin" / "Zoom.exe")
win = Application(backend="uia").start(zoom_path)
win = Application(backend="uia").connect(title="Zoom Workplace", timeout=20)

join_meeting = win.ZoomWorkplace.child_window(title="Join a meeting", control_type="Button").wrapper_object()
join_meeting.click_input()

child_win = Application(backend="uia").connect(title="Join meeting", timeout=20)

meeting_id = child_win.JoinMeeting.child_window(title="Meeting ID or personal link name", control_type="Edit")
audio = child_win.JoinMeeting.child_window(title="Don't connect to audio", control_type="CheckBox")
video = child_win.JoinMeeting.child_window(title="Turn off my video", control_type="CheckBox")
join = child_win.JoinMeeting.child_window(title="Join", control_type="Button")

meeting_id.type_keys("7743816469")
audio.click_input()
video.click_input()
join.click_input()