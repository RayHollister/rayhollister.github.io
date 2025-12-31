---
sitemap: false
exclude: true
title: Kindle Calendar
layout: null
permalink: /kc
---
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover" />
  <title>Kindle Calendar Agenda</title>
  <style>
    :root { color-scheme: light; }
    body { margin: 0; font-family: "Bookerly", Georgia, serif; background: #fff; color: #000; }
    .wrap { padding: 12px 14px; gap: 10px; max-width: 618px; margin: 0 auto; min-height: calc(100vh - 25px); display: flex; flex-direction: column; }
    header { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; border-bottom: 1px solid #ddd; padding-bottom: 8px; margin-bottom: 10px; }
    h1 { font-size: 20px; margin: 0; font-weight: 700; }
    .clock { text-align: left; padding: 0; }
    .clock-time { font-size: 48px; font-weight: 700; line-height: 1; margin-bottom: 10px; color: #000; }
    .clock-date { font-size: 24px; color: #000; font-weight: 700; }
    .clock-day { font-size: 24px; color: #000; font-weight: 700; }
    .weather { margin-top: 10px; padding-top: 8px; border-top: 1px solid #ddd; display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; }
    .weather-title { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
    .weather-row { display: flex; gap: 10px; align-items: baseline; font-size: 14px; }
    .weather-label { color: #000; font-weight: 700; margin-right: 4px; }
    .weather-condition { display: flex; align-items: center; gap: 8px; margin: 6px 0; font-size: 18px; font-weight: 700; color: #000; }
    .weather-icon { width: 125px; height: 75px; display: inline-flex; align-items: center; justify-content: center; font-size: 48px; line-height: 1; flex-shrink: 0; }
    .weather-icon svg { width: 125px; height: 75px; display: block; }
    .weather-status { font-size: 12px; color: #777; margin-top: 2px; }
    .month-calendar { width: 100%; max-width: 300px; margin-left: auto; margin-right: 0; }
    .month-title { font-size: 16px; font-weight: 700; margin-bottom: 6px; }
    .month-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; }
    .month-weekday { font-size: 12px; text-align: center; color: #333; font-weight: 700; }
    .month-day { font-size: 13px; text-align: center; padding: 4px 0; border: 1px solid #666; border-radius: 4px; }
    .month-day.is-today { background: #111; color: #fff; border-color: #111; }
    .meta { font-size: 13px; color: #333; }
    .notice { font-size: 14px; padding: 10px; border: 1px solid #ddd; background: #fafafa; border-radius: 6px; }
    .controls { display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0 12px; }
    button { font: inherit; padding: 8px 10px; border: 1px solid #ddd; background: #fff; border-radius: 6px; }
    button:active { background: #f0f0f0; }
    .agenda { margin-top: auto; }
    .day { margin: 14px 0; }
    .day h2 { font-size: 16px; margin: 0 0 8px; padding-top: 10px; border-top: 1px solid #eee; }
    ul { list-style: none; padding: 0; margin: 0; }
    li { padding: 10px 0; border-bottom: 1px solid #eee; }
    .row { display: grid; grid-template-columns: 90px 1fr; gap: 10px; align-items: start; }
    .time { font-size: 14px; color: #111; font-weight: 700; }
    .title { font-size: 15px; font-weight: 700; margin: 0 0 3px; }
    .sub { font-size: 13px; color: #333; margin: 0; line-height: 1.25; }
    .tag { display: inline-block; font-size: 12px; padding: 1px 6px; border: 1px solid #ccc; border-radius: 999px; margin-right: 6px; margin-left: 0; color: #333; }
    .muted { color: #555; font-weight: 400; }
    .error { color: #a00; }
    .top-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; border-bottom: 1px solid #ddd; padding-bottom: 8px; }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="top-row">
      <div class="clock">
        <div class="clock-time" id="clockTime"></div>
        <div class="clock-day" id="clockDay"></div>
        <div class="clock-date" id="clockDate"></div>
        <div class="weather" id="weather">
          <div class="weather-main">
            <div class="weather-title">Weather</div>
            <div class="weather-condition">
              <span id="weatherSummary"></span>
            </div>
            <div class="weather-row">
              <span class="weather-label">High</span>
              <span id="weatherHigh">--</span>
              <span class="weather-label">Low</span>
              <span id="weatherLow">--</span>
            </div>

            <div class="weather-status" id="weatherStatus"></div>
          </div>
          <span class="weather-icon" id="weatherIcon"></span>
        </div>
      </div>
      <div class="month-calendar" id="monthCalendar"></div>
    </div>

    <div id="kindleGate" class="notice" style="display:none"></div>

    <div class="agenda">
      <header>
        <h1>Agenda</h1>
        <div class="meta" id="meta"><span id="metaUpdated"></span></div>
      </header>

      <div class="controls">
        <button id="btnToday" type="button">Today</button>
        <button id="btnTomorrow" type="button">Tomorrow</button>
        <button id="btnWeek" type="button">Next 7 Days</button>
        <button id="btnRefresh" type="button">Refresh</button>
      </div>

      <div id="status" class="meta"></div>
      <div id="agenda"></div>
    </div>
  </div>

  <script>
    window.WEATHER_LAT = 30.41306218504568;
    window.WEATHER_LON = -81.6948559753448;
    (function () {
      function isKindle() {
        var ua = (navigator.userAgent || "").toLowerCase();
        return ua.includes("kindle") || ua.includes("silk") || ua.includes("kfapwi") || ua.includes("kfw") || ua.includes("kftt") || ua.includes("kfjwi") || ua.includes("kfsowi") || ua.includes("kfa") || ua.includes("kfo") || ua.includes("kfdow");
      }

      var gate = document.getElementById("kindleGate");
      var DISABLE_KINDLE_GATE = true;

      if (!DISABLE_KINDLE_GATE && !isKindle()) {
        gate.style.display = "block";
        gate.innerHTML = "This page only loads the agenda view on a Kindle. You can still view it on desktop, but it will not fetch calendar data here.";
        return;
      }

      var meta = document.getElementById("meta");
      var metaUpdated = document.getElementById("metaUpdated");
      if (meta && !metaUpdated) {
        metaUpdated = document.createElement("span");
        metaUpdated.id = "metaUpdated";
        meta.appendChild(metaUpdated);
      }
      var status = document.getElementById("status");
      var agendaEl = document.getElementById("agenda");
      var clockTimeEl = document.getElementById("clockTime");
      var clockDayEl = document.getElementById("clockDay");
      var clockDateEl = document.getElementById("clockDate");
      var monthCalendarEl = document.getElementById("monthCalendar");
      var weatherHighEl = document.getElementById("weatherHigh");
      var weatherLowEl = document.getElementById("weatherLow");
      var weatherIconEl = document.getElementById("weatherIcon");
      var weatherSummaryEl = document.getElementById("weatherSummary");
      var weatherStatusEl = document.getElementById("weatherStatus");
      var lastClockDayKey = "";

      function pad2(n) { return (n < 10 ? "0" : "") + n; }

      function formatTime(d) {
        var h = d.getHours();
        var m = d.getMinutes();
        var am = h >= 12 ? "PM" : "AM";
        var hh = h % 12; if (hh === 0) hh = 12;
        return hh + ":" + pad2(m) + " " + am;
      }

      function formatTimeParts(h, m) {
        var am = h >= 12 ? "PM" : "AM";
        var hh = h % 12; if (hh === 0) hh = 12;
        return hh + ":" + pad2(m) + " " + am;
      }

      function startOfDay(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate(), 0, 0, 0, 0); }
      function addDays(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }

      var DAY_NAMES = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
      var MONTH_NAMES = ["January","February","March","April","May","June","July","August","September","October","November","December"];

      function ymd(d) {
        return d.getFullYear() + "-" + pad2(d.getMonth() + 1) + "-" + pad2(d.getDate());
      }

      function niceDay(d) {
        return DAY_NAMES[d.getDay()] + ", " + MONTH_NAMES[d.getMonth()] + " " + d.getDate();
      }

      function nthWeekdayOfMonth(year, monthIndex, weekday, nth) {
        var first = new Date(Date.UTC(year, monthIndex, 1));
        var firstWeekday = first.getUTCDay();
        return 1 + ((7 + weekday - firstWeekday) % 7) + (nth - 1) * 7;
      }

      function isEasternDstUtc(utcMillis) {
        var d = new Date(utcMillis);
        var year = d.getUTCFullYear();
        var dstStartDay = nthWeekdayOfMonth(year, 2, 0, 2);
        var dstEndDay = nthWeekdayOfMonth(year, 10, 0, 1);
        var dstStart = Date.UTC(year, 2, dstStartDay, 7, 0, 0);
        var dstEnd = Date.UTC(year, 10, dstEndDay, 6, 0, 0);
        return utcMillis >= dstStart && utcMillis < dstEnd;
      }

      function easternOffsetMinutes(utcMillis) {
        return isEasternDstUtc(utcMillis) ? -240 : -300;
      }

      function updateClock() {
        if (!clockTimeEl || !clockDateEl || !clockDayEl) return;
        var nowUtcMs = Date.now ? Date.now() : new Date().getTime();
        var offsetMinutes = easternOffsetMinutes(nowUtcMs);
        var local = new Date(nowUtcMs + offsetMinutes * 60000);
        var h = local.getUTCHours();
        var m = local.getUTCMinutes();
        var dayIndex = local.getUTCDay();
        var monthIndex = local.getUTCMonth();
        var dayNum = local.getUTCDate();
        var year = local.getUTCFullYear();
        clockTimeEl.textContent = formatTimeParts(h, m);
        clockDayEl.textContent = DAY_NAMES[dayIndex];
        clockDateEl.textContent = MONTH_NAMES[monthIndex] + " " + dayNum + ", " + year;
        var dayKey = year + "-" + pad2(monthIndex + 1) + "-" + pad2(dayNum);
        if (dayKey !== lastClockDayKey) {
          renderMonthCalendar(year, monthIndex, dayNum, dayIndex);
          updateWeather(year, monthIndex + 1, dayNum);
          lastClockDayKey = dayKey;
        }
      }

      function renderMonthCalendar(year, monthIndex, dayNum, dayIndex) {
        if (!monthCalendarEl) return;
        var firstOfMonthUtc = new Date(Date.UTC(year, monthIndex, 1));
        var firstWeekday = firstOfMonthUtc.getUTCDay();
        var daysInMonth = new Date(Date.UTC(year, monthIndex + 1, 0)).getUTCDate();
        var weekdays = ["S","M","T","W","T","F","S"];
        var html = '<div class="month-title">' + MONTH_NAMES[monthIndex] + " " + year + "</div>";
        html += '<div class="month-grid">';
        for (var w = 0; w < weekdays.length; w++) {
          html += '<div class="month-weekday">' + weekdays[w] + "</div>";
        }
        for (var b = 0; b < firstWeekday; b++) {
          html += '<div class="month-day"></div>';
        }
        for (var d = 1; d <= daysInMonth; d++) {
          var isToday = d === dayNum;
          html += '<div class="month-day' + (isToday ? " is-today" : "") + '">' + d + "</div>";
        }
        html += "</div>";
        monthCalendarEl.innerHTML = html;
      }

      function describeWeather(code) {
        if (code === 0) return { label: "Clear", icon: "sun" };
        if (code === 1 || code === 2) return { label: "Partly cloudy", icon: "partly" };
        if (code === 3) return { label: "Cloudy", icon: "cloud" };
        if (code === 45 || code === 48) return { label: "Fog", icon: "fog" };
        if (code === 51 || code === 53 || code === 55 || code === 56 || code === 57) return { label: "Drizzle", icon: "drizzle" };
        if (code === 61 || code === 63 || code === 65 || code === 80 || code === 81 || code === 82 || code === 66 || code === 67) return { label: "Rain", icon: "rain" };
        if (code === 71 || code === 73 || code === 75 || code === 77 || code === 85 || code === 86) return { label: "Snow", icon: "snow" };
        if (code === 95 || code === 96 || code === 99) return { label: "Thunderstorms", icon: "thunder" };
        return { label: "", icon: "" };
      }

      function weatherIconSvg(key) {
        var stroke = ' stroke="#111" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"';
        function wrap(inner) {
          return '<svg viewBox="0 0 125 75" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' + inner + "</svg>";
        }
        var cloud = '<rect x="26" y="38" width="78" height="22" rx="11"' + stroke + "/>" +
          '<circle cx="46" cy="38" r="14"' + stroke + "/>" +
          '<circle cx="68" cy="30" r="18"' + stroke + "/>" +
          '<circle cx="92" cy="38" r="12"' + stroke + "/>";
        if (key === "sun") {
          return wrap(
            '<circle cx="62.5" cy="37.5" r="16"' + stroke + "/>" +
            '<line x1="62.5" y1="6" x2="62.5" y2="18"' + stroke + "/>" +
            '<line x1="62.5" y1="57" x2="62.5" y2="69"' + stroke + "/>" +
            '<line x1="31" y1="37.5" x2="43" y2="37.5"' + stroke + "/>" +
            '<line x1="82" y1="37.5" x2="94" y2="37.5"' + stroke + "/>" +
            '<line x1="42" y1="17" x2="50" y2="25"' + stroke + "/>" +
            '<line x1="74" y1="50" x2="82" y2="58"' + stroke + "/>" +
            '<line x1="74" y1="25" x2="82" y2="17"' + stroke + "/>" +
            '<line x1="42" y1="58" x2="50" y2="50"' + stroke + "/>"
          );
        }
        if (key === "partly") {
          return wrap(
            '<circle cx="36" cy="24" r="12"' + stroke + "/>" +
            '<line x1="36" y1="4" x2="36" y2="12"' + stroke + "/>" +
            '<line x1="18" y1="24" x2="26" y2="24"' + stroke + "/>" +
            '<line x1="46" y1="24" x2="54" y2="24"' + stroke + "/>" +
            '<line x1="24" y1="12" x2="30" y2="18"' + stroke + "/>" +
            '<line x1="42" y1="12" x2="48" y2="18"' + stroke + "/>" +
            cloud
          );
        }
        if (key === "cloud") {
          return wrap(cloud);
        }
        if (key === "fog") {
          return wrap(
            cloud +
            '<line x1="38" y1="60" x2="92" y2="60"' + stroke + "/>" +
            '<line x1="34" y1="66" x2="88" y2="66"' + stroke + "/>" +
            '<line x1="40" y1="72" x2="94" y2="72"' + stroke + "/>"
          );
        }
        if (key === "drizzle") {
          return wrap(
            cloud +
            '<line x1="52" y1="60" x2="48" y2="66"' + stroke + "/>" +
            '<line x1="70" y1="60" x2="66" y2="66"' + stroke + "/>"
          );
        }
        if (key === "rain") {
          return wrap(
            cloud +
            '<line x1="50" y1="60" x2="46" y2="70"' + stroke + "/>" +
            '<line x1="66" y1="60" x2="62" y2="70"' + stroke + "/>" +
            '<line x1="82" y1="60" x2="78" y2="70"' + stroke + "/>"
          );
        }
        if (key === "snow") {
          return wrap(
            cloud +
            '<line x1="52" y1="60" x2="46" y2="66"' + stroke + "/>" +
            '<line x1="46" y1="60" x2="52" y2="66"' + stroke + "/>" +
            '<line x1="78" y1="60" x2="72" y2="66"' + stroke + "/>" +
            '<line x1="72" y1="60" x2="78" y2="66"' + stroke + "/>"
          );
        }
        if (key === "thunder") {
          return wrap(
            cloud +
            '<polygon points="62,52 50,72 66,72 56,74 78,56 64,56" fill="#111" />'
          );
        }
        return "";
      }

      function setWeatherSummary(label, iconKey) {
        if (weatherSummaryEl) weatherSummaryEl.textContent = label || "";
        if (!weatherIconEl) return;
        var svg = "";
        if (typeof iconKey === "string" && iconKey.indexOf("<svg") === 0) {
          svg = iconKey;
        } else if (iconKey) {
          svg = weatherIconSvg(iconKey);
        }
        if (svg) {
          weatherIconEl.innerHTML = svg;
        } else {
          weatherIconEl.textContent = iconKey || "";
        }
      }

      function updateWeather(year, month, dayNum) {
        if (!weatherHighEl || !weatherLowEl || !weatherStatusEl) return;
        var key = year + "-" + pad2(month) + "-" + pad2(dayNum);
        weatherStatusEl.textContent = "Loading weather…";
        getJson("/kc/weather.json").then(function (data) {
          if (!applyLocalWeather(data, key)) throw new Error("No local weather");
        }).catch(function () {
          return fetchWeatherFromApi(key);
        }).catch(function () {
          weatherStatusEl.textContent = "Weather unavailable.";
        });
      }

      function applyLocalWeather(data, key) {
        if (!data || data.high == null || data.low == null) return false;
        weatherHighEl.textContent = Math.round(data.high) + "°";
        weatherLowEl.textContent = Math.round(data.low) + "°";
        if (data.icon && weatherIconSvg(data.icon)) {
          setWeatherSummary(data.condition || "", data.icon || "");
        } else if (data.weathercode != null) {
          var meta = describeWeather(Number(data.weathercode));
          setWeatherSummary(meta.label, meta.icon);
        } else {
          setWeatherSummary(data.condition || "", "");
        }
        if (data.date && data.date !== key) {
          weatherStatusEl.textContent = "As of " + data.date;
        } else {
          weatherStatusEl.textContent = "";
        }
        return true;
      }

      function fetchWeatherFromApi(key) {
        var lat = window.WEATHER_LAT;
        var lon = window.WEATHER_LON;
        if (!lat || !lon) throw new Error("Missing coords");
        var url = "https://api.open-meteo.com/v1/forecast?latitude=" + encodeURIComponent(lat) +
          "&longitude=" + encodeURIComponent(lon) +
          "&daily=temperature_2m_max,temperature_2m_min,weathercode" +
          "&temperature_unit=fahrenheit" +
          "&timezone=America%2FNew_York";
        return getJson(url).then(function (data) {
          var daily = data && data.daily;
          var times = daily && daily.time;
          var highs = daily && daily.temperature_2m_max;
          var lows = daily && daily.temperature_2m_min;
          var codes = daily && daily.weathercode;
          if (!times || !highs || !lows) throw new Error("Missing daily data");
          var idx = -1;
          for (var i = 0; i < times.length; i++) {
            if (times[i] === key) { idx = i; break; }
          }
          if (idx === -1) throw new Error("No weather for today");
          weatherHighEl.textContent = Math.round(highs[idx]) + "°";
          weatherLowEl.textContent = Math.round(lows[idx]) + "°";
          var code = codes && idx < codes.length ? Number(codes[idx]) : null;
          if (code != null) {
            var meta = describeWeather(code);
            setWeatherSummary(meta.label, meta.icon);
          } else {
            setWeatherSummary("", "");
          }
          weatherStatusEl.textContent = "";
        });
      }

      function formatMultiline(text) {
        return escapeHtml(text).replace(/\n/g, "<br>");
      }

      function escapeHtml(s) {
        return String(s || "")
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#039;");
      }

      function groupByDay(events) {
        var map = new Map();
        for (var i = 0; i < events.length; i++) {
          var e = events[i];
          var key = ymd(e.start);
          if (!map.has(key)) map.set(key, []);
          map.get(key).push(e);
        }
        return map;
      }

      function render(events, rangeStart, rangeEnd) {
        events.sort(function (a, b) { return a.start - b.start; });

        var filtered = events.filter(function (e) {
          return e.end > rangeStart && e.start < rangeEnd;
        });

        if (!filtered.length) {
          agendaEl.innerHTML = '<div class="notice">No events in this range.</div>';
          return;
        }

        var byDay = groupByDay(filtered);
        var keys = Array.from(byDay.keys()).sort();

        var html = "";
        for (var k = 0; k < keys.length; k++) {
          var dayKey = keys[k];
          var dayEvents = byDay.get(dayKey);
          dayEvents.sort(function (a, b) { return a.start - b.start; });

          var dParts = dayKey.split("-");
          var dayDate = new Date(Number(dParts[0]), Number(dParts[1]) - 1, Number(dParts[2]), 0, 0, 0, 0);

          html += '<div class="day">';
          html += "<h2>" + escapeHtml(niceDay(dayDate)) + "</h2>";
          html += "<ul>";

          for (var j = 0; j < dayEvents.length; j++) {
            var e = dayEvents[j];
            var timeText = e.allDay ? "All day" : (formatTime(e.start) + " – " + formatTime(e.end));
            html += "<li>";
            html += '<div class="row">';
            html += '<div class="time">' + escapeHtml(timeText) + "</div>";
            html += '<div>';
            html += '<p class="title"><span class="tag">' + escapeHtml(e.calendarLabel) + "</span>" + escapeHtml(e.title || "(No title)") + "</p>";
            if (e.location) html += '<p class="sub"><span class="muted">Location:</span> ' + escapeHtml(e.location) + "</p>";
            if (e.description) html += '<p class="sub">' + formatMultiline(e.description) + "</p>";
            html += "</div>";
            html += "</div>";
            html += "</li>";
          }

          html += "</ul>";
          html += "</div>";
        }

        agendaEl.innerHTML = html;
      }

      function getJson(urls) {
        var list = Array.isArray(urls) ? urls : [urls];
        return new Promise(function (resolve, reject) {
          var idx = 0;

          function tryNext() {
            var url = list[idx];
            var xhr = new XMLHttpRequest();
            var bust = (url.indexOf("?") === -1 ? "?" : "&") + "t=" + Date.now();
            xhr.open("GET", url + bust, true);
            xhr.timeout = 15000;
            try {
              xhr.setRequestHeader("Cache-Control", "no-cache");
            } catch (err) {
              // Some older clients disallow setting request headers.
            }
            xhr.onreadystatechange = function () {
              if (xhr.readyState !== 4) return;
              if ((xhr.status >= 200 && xhr.status < 300) || (xhr.status === 0 && xhr.responseText)) {
                try {
                  resolve(JSON.parse(xhr.responseText));
                } catch (err) {
                  reject(err);
                }
                return;
              }
              fail();
            };
            xhr.onerror = fail;
            xhr.ontimeout = fail;
            xhr.send();

            function fail() {
              if (idx < list.length - 1) {
                idx += 1;
                tryNext();
                return;
              }
              reject(new Error("HTTP " + xhr.status));
            }
          }

          tryNext();
        });
      }

      async function fetchAgendaJson() {
        status.textContent = "Loading…";
        status.className = "meta";

        try {
          var data = await getJson(["/kc/agenda.json", "agenda.json"]);

          var events = (data.events || []).map(function (e) {
            return {
              title: e.title || "",
              location: e.location || "",
              description: e.description || "",
              calendarLabel: e.calendarLabel || "",
              allDay: !!e.allDay,
              start: new Date(e.start),
              end: new Date(e.end)
            };
          });

          var now = new Date();
          if (metaUpdated) {
            metaUpdated.textContent = "Updated: " + (data.generatedAt || "");
          }

          function setRange(days) {
            var s = startOfDay(now);
            var end = addDays(s, days);
            render(events, s, end);
          }

          document.getElementById("btnToday").onclick = function () {
            var s = startOfDay(new Date());
            var end = addDays(s, 1);
            render(events, s, end);
          };

          document.getElementById("btnTomorrow").onclick = function () {
            var s = startOfDay(addDays(new Date(), 1));
            var end = addDays(s, 1);
            render(events, s, end);
          };

          document.getElementById("btnWeek").onclick = function () { setRange(7); };

          document.getElementById("btnRefresh").onclick = function () { fetchAgendaJson(); };

          status.textContent = "Loaded " + events.length + " events.";
          setRange(7);

        } catch (err) {
          status.textContent = "Error loading agenda.json: " + err.message;
          status.className = "meta error";
          agendaEl.innerHTML = '<div class="notice">If this keeps happening, confirm that /kc/agenda.json exists in the built site.</div>';
        }
      }

      fetchAgendaJson();
      updateClock();
      setInterval(updateClock, 60000);
    })();
  </script>
</body>
</html>
<script>
(function () {
  function upd() {
    var w = window.innerWidth, h = window.innerHeight, d = window.devicePixelRatio || 1;
    var el = document.getElementById('viewportDims');
    if (!el) {
      el = document.createElement('div');
      el.id = 'viewportDims';
      el.style.fontSize = '12px';
      el.style.color = '#333';
      el.style.marginLeft = '8px';
      el.style.display = 'inline-block';
      var target = document.querySelector('header .meta') || document.querySelector('header') || document.body;
      target.appendChild(el);
    }
    el.textContent = w + '×' + h + ' px • dpr ' + d;
  }
  window.addEventListener('resize', upd);
  window.addEventListener('orientationchange', upd);
  document.addEventListener('DOMContentLoaded', upd);
  upd();
})();
</script>
