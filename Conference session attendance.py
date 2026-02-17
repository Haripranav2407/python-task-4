attendance = [
    ("S1", "A101"),
    ("S1", "A102"),
    ("S2", "A101"),
    ("S2", "A103"),
    ("S3", "A104"),
    ("S3", "A101")
]
session_attendees = {}
attendee_sessions = {}
for session, attendee in attendance:
    session_attendees.setdefault(session, set()).add(attendee)
    attendee_sessions.setdefault(attendee, set()).add(session)
total_attendees_per_session = {
    s: len(a) for s, a in session_attendees.items()
}
multi_session_attendees = [
    a for a, s in attendee_sessions.items() if len(s) > 1
]
print("Total attendees per session:")
print(total_attendees_per_session)
print("\nAttendees who attended more than one session:")
print(multi_session_attendees)