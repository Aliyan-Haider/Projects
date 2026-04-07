from pywinauto.application import Application
from pathlib import Path

zoom_path = str(Path.home() / "AppData" / "Roaming" / "Zoom" / "bin" / "Zoom.exe")

# these varables take your meeting id and passcode.
meeting_id = ""
passcode = ""

# open and connects to the first window.
win = Application(backend="uia").start(zoom_path)
win = Application(backend="uia").connect(title="Zoom Workplace", timeout=20)

join_meeting = win.ZoomWorkplace.child_window(title="Join a meeting", control_type="Button").wrapper_object()
join_meeting.click_input()

# connects to the second window. here, you enter the details of the meeting.
child_win = Application(backend="uia").connect(title="Join meeting", timeout=20)

meeting_id_input = child_win.JoinMeeting.child_window(title="Meeting ID or personal link name", control_type="Edit")
audio = child_win.JoinMeeting.child_window(title="Don't connect to audio", control_type="CheckBox")
video = child_win.JoinMeeting.child_window(title="Turn off my video", control_type="CheckBox")
join = child_win.JoinMeeting.child_window(title="Join", control_type="Button")

# the line directly below enters your meeting id into the text box.
meeting_id_input.type_keys(meeting_id)
audio.click_input()
video.click_input()
join.click_input()

# connects to the third window. here, you enter your passcode.
passcode_dialogue = Application(backend="uia").connect(title="Enter meeting passcode", timeout=5)

passcode_input = passcode_dialogue.EnterMeetngPasscode.child_window(title="Meeting passcode", control_type="Edit")
join_2 = passcode_dialogue.EnterMeetingPasscode.child_window(title="Join meeting", control_type="Button")

# the line directly below enters your passcode into the passcode text box.
passcode_input.type_keys(passcode)
join_2.click_input()

# connects to the fourth window. the window can be toggled to not appear, but this program assumes it always appears.
meeting_room = Application(backend="uia").connect(class_name="VideoPreviewWndClass", timeout=5)

# this variable stores the title for the fourth window. the title is not hardcoded for this window.
window_4_title = meeting_room.windows()[0].window_text()

join_3 = meeting_room.window(best_match=window_4_title).child_window(title="Join", control_type="Button")

join_3.click_input()