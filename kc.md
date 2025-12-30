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
    body { margin: 0; font-family: "Bookerly", Georgia, serif; background: #fff; color: #111; }
    .wrap { padding: 12px 14px; max-width: 618px; margin: 0 auto; min-height: calc(100vh - 25px); display: flex; flex-direction: column; }
    header { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; border-bottom: 1px solid #ddd; padding-bottom: 8px; margin-bottom: 10px; }
    h1 { font-size: 20px; margin: 0; font-weight: 700; }
    .clock { text-align: center; padding: 6px 0 10px; }
    .clock-time { font-size: 48px; font-weight: 700; line-height: 1; }
    .clock-date { font-size: 20px; color: #333; }
    .month-calendar { margin-top: 20px; max-width: 280px; margin-left: auto; margin-right: auto; }
    .month-title { font-size: 16px; font-weight: 700; margin-bottom: 6px; }
    .month-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; }
    .month-weekday { font-size: 12px; text-align: center; color: #555; font-weight: 700; }
    .month-day { font-size: 13px; text-align: center; padding: 4px 0; border: 1px solid #666; border-radius: 4px; }
    .month-day.is-today { background: #111; color: #fff; border-color: #111; }
    .meta { font-size: 13px; color: #333; }
    .notice { font-size: 14px; padding: 10px; border: 1px solid #ddd; background: #fafafa; border-radius: 6px; }
    .controls { display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0 12px; }
    button { font: inherit; padding: 8px 10px; border: 1px solid #bbb; background: #fff; border-radius: 6px; }
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
  </style>
</head>
<body>
  <div class="wrap">
    <div class="clock">
      <div class="clock-time" id="clockTime"></div>
      <div class="clock-date" id="clockDate"></div>
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
      var clockDateEl = document.getElementById("clockDate");
      var monthCalendarEl = document.getElementById("monthCalendar");
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

      function niceDayParts(dayIndex, monthIndex, dayNum) {
        return DAY_NAMES[dayIndex] + ", " + MONTH_NAMES[monthIndex] + " " + dayNum;
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
        if (!clockTimeEl || !clockDateEl) return;
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
        clockDateEl.textContent = niceDayParts(dayIndex, monthIndex, dayNum) + " " + year;
        var dayKey = year + "-" + pad2(monthIndex + 1) + "-" + pad2(dayNum);
        if (dayKey !== lastClockDayKey) {
          renderMonthCalendar(year, monthIndex, dayNum, dayIndex);
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

      async function fetchAgendaJson() {
        status.textContent = "Loading…";
        status.className = "meta";

        try {
          var res = await fetch("/kc/agenda.json", { cache: "no-store" });
          if (!res.ok) throw new Error("HTTP " + res.status);
          var data = await res.json();

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
