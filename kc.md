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
    body { margin: 0; font-family: Georgia, serif; background: #fff; color: #111; }
    .wrap { padding: 12px 14px; max-width: 900px; margin: 0 auto; }
    header { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; border-bottom: 1px solid #ddd; padding-bottom: 8px; margin-bottom: 10px; }
    h1 { font-size: 20px; margin: 0; font-weight: 700; }
    .meta { font-size: 13px; color: #333; }
    .notice { font-size: 14px; padding: 10px; border: 1px solid #ddd; background: #fafafa; border-radius: 6px; }
    .controls { display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0 12px; }
    button { font: inherit; padding: 8px 10px; border: 1px solid #bbb; background: #fff; border-radius: 6px; }
    button:active { background: #f0f0f0; }
    .day { margin: 14px 0; }
    .day h2 { font-size: 16px; margin: 0 0 8px; padding-top: 10px; border-top: 1px solid #eee; }
    ul { list-style: none; padding: 0; margin: 0; }
    li { padding: 10px 0; border-bottom: 1px solid #eee; }
    .row { display: grid; grid-template-columns: 90px 1fr; gap: 10px; align-items: start; }
    .time { font-size: 14px; color: #111; font-weight: 700; }
    .title { font-size: 15px; font-weight: 700; margin: 0 0 3px; }
    .sub { font-size: 13px; color: #333; margin: 0; line-height: 1.25; }
    .tag { display: inline-block; font-size: 12px; padding: 1px 6px; border: 1px solid #ccc; border-radius: 999px; margin-left: 6px; color: #333; }
    .muted { color: #555; font-weight: 400; }
    .error { color: #a00; }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>Agenda</h1>
      <div class="meta" id="meta"></div>
    </header>

    <div id="kindleGate" class="notice" style="display:none"></div>

    <div class="controls">
      <button id="btnToday" type="button">Today</button>
      <button id="btnTomorrow" type="button">Tomorrow</button>
      <button id="btnWeek" type="button">Next 7 Days</button>
      <button id="btnRefresh" type="button">Refresh</button>
    </div>

    <div id="status" class="meta"></div>
    <div id="agenda"></div>
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
      var status = document.getElementById("status");
      var agendaEl = document.getElementById("agenda");

      function pad2(n) { return (n < 10 ? "0" : "") + n; }

      function formatTime(d) {
        var h = d.getHours();
        var m = d.getMinutes();
        var am = h >= 12 ? "PM" : "AM";
        var hh = h % 12; if (hh === 0) hh = 12;
        return hh + ":" + pad2(m) + " " + am;
      }

      function startOfDay(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate(), 0, 0, 0, 0); }
      function addDays(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }

      function ymd(d) {
        return d.getFullYear() + "-" + pad2(d.getMonth() + 1) + "-" + pad2(d.getDate());
      }

      function niceDay(d) {
        var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
        var months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
        return days[d.getDay()] + ", " + months[d.getMonth()] + " " + d.getDate();
      }

      function escapeHtml(s) {
        return String(s || "")
          .replaceAll("&", "&amp;")
          .replaceAll("<", "&lt;")
          .replaceAll(">", "&gt;")
          .replaceAll('"', "&quot;")
          .replaceAll("'", "&#039;");
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
            html += '<p class="title">' + escapeHtml(e.title || "(No title)") + '<span class="tag">' + escapeHtml(e.calendarLabel) + "</span></p>";
            if (e.location) html += '<p class="sub"><span class="muted">Location:</span> ' + escapeHtml(e.location) + "</p>";
            if (e.description) html += '<p class="sub">' + escapeHtml(e.description) + "</p>";
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
          meta.textContent = "Updated: " + (data.generatedAt || "");

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
    })();
  </script>
</body>
</html>
