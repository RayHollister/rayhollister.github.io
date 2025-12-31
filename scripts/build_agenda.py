import os
import json
import datetime as dt
from zoneinfo import ZoneInfo
import requests
from icalendar import Calendar
import recurring_ical_events

DEFAULT_TZ = os.getenv("AGENDA_TZ", "America/New_York")
DEFAULT_WEATHER_LAT = "30.41306218504568"
DEFAULT_WEATHER_LON = "-81.6948559753448"

def describe_weather(code):
  if code is None:
    return ("", "")
  if code == 0:
    return ("Clear", "☀")
  if code in (1, 2):
    return ("Partly cloudy", "⛅")
  if code == 3:
    return ("Cloudy", "☁")
  if code in (45, 48):
    return ("Fog", "🌫")
  if code in (51, 53, 55, 56, 57):
    return ("Drizzle", "🌦")
  if code in (61, 63, 65, 80, 81, 82, 66, 67):
    return ("Rain", "🌧")
  if code in (71, 73, 75, 77, 85, 86):
    return ("Snow", "❄")
  if code in (95, 96, 99):
    return ("Thunderstorms", "⛈")
  return ("", "")

def to_local_naive(x, tz):
  if x is None:
    return None

  # date only
  if isinstance(x, dt.date) and not isinstance(x, dt.datetime):
    return dt.datetime(x.year, x.month, x.day)

  # datetime
  if isinstance(x, dt.datetime):
    if x.tzinfo is None:
      # treat naive as local wall time in target tz
      return x
    return x.astimezone(tz).replace(tzinfo=None)

  raise TypeError(f"Unsupported datetime type: {type(x)}")

def iso_local(naive_local_dt):
  if naive_local_dt is None:
    return None
  return naive_local_dt.isoformat()

def clean(s, limit=260):
  s = (s or "").strip().replace("\r\n", "\n").replace("\r", "\n")
  if len(s) > limit:
    s = s[:limit].rstrip() + "…"
  return s

def parse_ics(label, url, now_local, tz, days_ahead=30):
  r = requests.get(url, timeout=30)
  r.raise_for_status()

  cal = Calendar.from_ical(r.text)
  events = []

  range_start = now_local - dt.timedelta(days=1)
  range_end = now_local + dt.timedelta(days=days_ahead)
  range_start_naive = range_start.replace(tzinfo=None)
  range_end_naive = range_end.replace(tzinfo=None)

  try:
    components = recurring_ical_events.of(cal).between(range_start, range_end)
  except Exception:
    components = [c for c in cal.walk() if c.name == "VEVENT"]

  for component in components:
    dtstart = component.get("dtstart")
    if not dtstart:
      continue
    dtend = component.get("dtend")

    raw_start = dtstart.dt
    raw_end = dtend.dt if dtend else None

    all_day = isinstance(raw_start, dt.date) and not isinstance(raw_start, dt.datetime)

    if all_day:
      start_dt = to_local_naive(raw_start, tz)
      if raw_end and isinstance(raw_end, dt.date) and not isinstance(raw_end, dt.datetime):
        end_dt = to_local_naive(raw_end, tz)
      else:
        end_dt = start_dt + dt.timedelta(days=1)
    else:
      start_dt = to_local_naive(raw_start, tz)
      end_dt = to_local_naive(raw_end, tz) if raw_end else (start_dt + dt.timedelta(hours=1))

    if end_dt <= range_start_naive or start_dt >= range_end_naive:
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
      "start": iso_local(start_dt),
      "end": iso_local(end_dt),
    })

  return events

def fetch_weather(now_local, tz_name):
  lat = os.getenv("WEATHER_LAT", DEFAULT_WEATHER_LAT)
  lon = os.getenv("WEATHER_LON", DEFAULT_WEATHER_LON)
  if not lat or not lon:
    return None

  params = {
    "latitude": lat,
    "longitude": lon,
    "daily": "temperature_2m_max,temperature_2m_min,weathercode",
    "temperature_unit": "fahrenheit",
    "timezone": tz_name,
  }
  r = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=30)
  r.raise_for_status()
  data = r.json()

  daily = data.get("daily", {})
  times = daily.get("time", [])
  highs = daily.get("temperature_2m_max", [])
  lows = daily.get("temperature_2m_min", [])
  codes = daily.get("weathercode", [])
  today_key = now_local.strftime("%Y-%m-%d")

  if today_key in times:
    idx = times.index(today_key)
  else:
    idx = 0 if times else None

  if idx is None or idx >= len(highs) or idx >= len(lows):
    return None

  code = codes[idx] if idx < len(codes) else None
  condition, icon = describe_weather(code)

  return {
    "date": times[idx],
    "high": highs[idx],
    "low": lows[idx],
    "weathercode": code,
    "condition": condition,
    "icon": icon,
    "units": "F",
    "generatedAt": now_local.strftime("%Y-%m-%d %H:%M %Z"),
    "source": "open-meteo",
  }

def main():
  tz = ZoneInfo(DEFAULT_TZ)
  now_local = dt.datetime.now(tz)

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
    all_events.extend(parse_ics(label, url, now_local, tz))

  all_events.sort(key=lambda e: e["start"] or "")

  out = {
    "generatedAt": now_local.strftime("%Y-%m-%d %H:%M %Z"),
    "events": all_events
  }

  os.makedirs("kc", exist_ok=True)
  with open("kc/agenda.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

  try:
    weather = fetch_weather(now_local, DEFAULT_TZ)
  except Exception:
    weather = None

  if weather:
    with open("kc/weather.json", "w", encoding="utf-8") as f:
      json.dump(weather, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  main()
