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

# enter your meeting id below.
meeting_id.type_keys("")
audio.click_input()
video.click_input()
join.click_input()

passcode_dialogue = Application(backend="uia").connect(title="Enter meeting passcode", timeout=5)

passcode_box = passcode_dialogue.EnterMeetngPasscode.child_window(title="Meeting passcode", control_type="Edit")
join_2 = passcode_dialogue.EnterMeetingPasscode.child_window(title="Join meeting", control_type="Button")

# enter your meeting passcode below.
passcode_box.type_keys("")
join_2.click_input()