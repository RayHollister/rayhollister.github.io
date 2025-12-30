import os
import json
import datetime as dt
import requests
from icalendar import Calendar

UTC = dt.timezone.utc

def to_naive_utc(x):
  if x is None:
    return None

  # date only
  if isinstance(x, dt.date) and not isinstance(x, dt.datetime):
    return dt.datetime(x.year, x.month, x.day)

  # datetime
  if isinstance(x, dt.datetime):
    if x.tzinfo is None:
      # treat naive as UTC
      return x
    return x.astimezone(UTC).replace(tzinfo=None)

  raise TypeError(f"Unsupported datetime type: {type(x)}")

def iso_z(naive_utc_dt):
  if naive_utc_dt is None:
    return None
  # expects naive UTC, add Z
  return naive_utc_dt.isoformat() + "Z"

def clean(s, limit=260):
  s = (s or "").strip().replace("\r\n", "\n").replace("\r", "\n")
  if len(s) > limit:
    s = s[:limit].rstrip() + "…"
  return s

def parse_ics(label, url, now_utc_naive, days_ahead=30):
  r = requests.get(url, timeout=30)
  r.raise_for_status()

  cal = Calendar.from_ical(r.text)
  events = []

  range_start = now_utc_naive - dt.timedelta(days=1)
  range_end = now_utc_naive + dt.timedelta(days=days_ahead)

  for component in cal.walk():
    if component.name != "VEVENT":
      continue

    dtstart = component.get("dtstart")
    if not dtstart:
      continue
    dtend = component.get("dtend")

    raw_start = dtstart.dt
    raw_end = dtend.dt if dtend else None

    all_day = isinstance(raw_start, dt.date) and not isinstance(raw_start, dt.datetime)

    if all_day:
      start_dt = to_naive_utc(raw_start)
      if raw_end and isinstance(raw_end, dt.date) and not isinstance(raw_end, dt.datetime):
        end_dt = to_naive_utc(raw_end)
      else:
        end_dt = start_dt + dt.timedelta(days=1)
    else:
      start_dt = to_naive_utc(raw_start)
      end_dt = to_naive_utc(raw_end) if raw_end else (start_dt + dt.timedelta(hours=1))

    # safe comparisons: all are naive UTC now
    if end_dt <= range_start or start_dt >= range_end:
      continue

    summary = str(component.get("summary", "") or "")
    location = str(component.get("location", "") or "")
    description = str(component.get("description", "") or "")

    events.append({
      "title": clean(summary, 140),
      "location": clean(location, 120),
      "description": clean(description, 220),
      "calendarLabel": label,
      "allDay": all_day,
      "start": iso_z(start_dt),
      "end": iso_z(end_dt),
    })

  return events

def main():
  now_naive_utc = dt.datetime.now(UTC).replace(tzinfo=None)

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
    all_events.extend(parse_ics(label, url, now_naive_utc))

  all_events.sort(key=lambda e: e["start"] or "")

  out = {
    "generatedAt": now_naive_utc.strftime("%Y-%m-%d %H:%M UTC"),
    "events": all_events
  }

  os.makedirs("kc", exist_ok=True)
  with open("kc/agenda.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  main()
