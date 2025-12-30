import os
import json
import datetime as dt
import requests
from icalendar import Calendar

def iso(dtobj):
  if dtobj is None:
    return None
  if isinstance(dtobj, dt.date) and not isinstance(dtobj, dt.datetime):
    dtobj = dt.datetime(dtobj.year, dtobj.month, dtobj.day)
  if dtobj.tzinfo is not None:
    dtobj = dtobj.astimezone(dt.timezone.utc).replace(tzinfo=None)
  return dtobj.isoformat() + "Z"

def clean(s, limit=260):
  s = (s or "").strip().replace("\r\n", "\n").replace("\r", "\n")
  if len(s) > limit:
    s = s[:limit].rstrip() + "…"
  return s

def parse_ics(label, url, now_utc, days_ahead=30):
  r = requests.get(url, timeout=30)
  r.raise_for_status()

  cal = Calendar.from_ical(r.text)
  events = []

  range_start = now_utc - dt.timedelta(days=1)
  range_end = now_utc + dt.timedelta(days=days_ahead)

  for component in cal.walk():
    if component.name != "VEVENT":
      continue

    summary = str(component.get("summary", "") or "")
    location = str(component.get("location", "") or "")
    description = str(component.get("description", "") or "")

    dtstart = component.get("dtstart")
    dtend = component.get("dtend")

    if not dtstart:
      continue

    start = dtstart.dt
    end = dtend.dt if dtend else None

    all_day = isinstance(start, dt.date) and not isinstance(start, dt.datetime)

    if all_day:
      start_dt = dt.datetime(start.year, start.month, start.day)
      if end and isinstance(end, dt.date) and not isinstance(end, dt.datetime):
        end_dt = dt.datetime(end.year, end.month, end.day)
      else:
        end_dt = start_dt + dt.timedelta(days=1)
    else:
      start_dt = start if isinstance(start, dt.datetime) else dt.datetime(start.year, start.month, start.day)
      if end:
        end_dt = end if isinstance(end, dt.datetime) else dt.datetime(end.year, end.month, end.day)
      else:
        end_dt = start_dt + dt.timedelta(hours=1)

    if end_dt <= range_start or start_dt >= range_end:
      continue

    events.append({
      "title": clean(summary, 140),
      "location": clean(location, 120),
      "description": clean(description, 220),
      "calendarLabel": label,
      "allDay": all_day,
      "start": iso(start_dt),
      "end": iso(end_dt),
    })

  return events

def main():
  now = dt.datetime.utcnow()

  calendars = []
  if os.getenv("ICS_PERSONAL_URL"):
    calendars.append(("Personal", os.environ["ICS_PERSONAL_URL"]))
  if os.getenv("ICS_WJCT_URL"):
    calendars.append(("WJCT", os.environ["ICS_WJCT_URL"]))
  if os.getenv("ICS_JAXPLAYS_URL"):
    calendars.append(("JaxPlays", os.environ["ICS_JAXPLAYS_URL"]))

  if not calendars:
    raise SystemExit("No ICS_*_URL env vars found.")

  all_events = []
  for label, url in calendars:
    all_events.extend(parse_ics(label, url, now))

  all_events.sort(key=lambda e: e["start"] or "")

  out = {
    "generatedAt": now.strftime("%Y-%m-%d %H:%M UTC"),
    "events": all_events
  }

  os.makedirs("kc", exist_ok=True)
  with open("kc/agenda.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  main()
