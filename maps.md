---
layout: page
title: Maps
permalink: /maps/
---

<link rel="stylesheet" href="/leaflet/leaflet.css">
<link href="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.css" rel="stylesheet">
<link rel="stylesheet" href="/leaflet/extramarkers/css/leaflet.extra-markers.min.css">
<link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/all.min.css" rel="stylesheet">
<link rel="stylesheet" href="/leaflet/zoomhome/leaflet.zoomhome.css">
<link rel="stylesheet" href="/leaflet/fullscreen/Control.FullScreen.css">

<style>
  .maps-page {
    display: grid;
    height: calc(100vh - 56px);
    height: calc(100dvh - 56px);
    min-height: 0;
  }

  body {
    overflow: hidden;
  }

  .page-content {
    padding: 0;
  }

  .page-content .wrapper {
    max-width: none;
    padding-left: 0;
    padding-right: 0;
  }

  .post {
    margin-bottom: 0;
  }

  .post-content {
    margin-bottom: 0;
  }

  .post-header,
  .site-footer {
    display: none;
  }

  .maps-intro {
    display: none;
  }

  .maps-shell {
    height: calc(100vh - 56px);
    height: calc(100dvh - 56px);
    min-height: 0;
    position: relative;
  }

  #ray-map {
    height: calc(100vh - 56px);
    height: calc(100dvh - 56px);
    min-height: 0;
    width: 100%;
  }

  .maps-panel {
    background: #f6f8fa;
    border: 1px solid #d8dee4;
    bottom: 1rem;
    box-shadow: 0 12px 28px rgba(27, 31, 36, 0.18);
    display: flex;
    flex-direction: column;
    max-height: min(26rem, calc(100vh - 8rem));
    min-width: 0;
    position: absolute;
    right: 1rem;
    top: auto;
    width: min(18rem, calc(100vw - 2rem));
    z-index: 500;
  }

  .maps-panel__header,
  .maps-panel__empty,
  .maps-place {
    padding: 1rem;
  }

  .maps-panel__header {
    border-bottom: 1px solid #d8dee4;
  }

  .maps-panel__heading {
    align-items: center;
    display: flex;
    gap: 0.75rem;
    justify-content: space-between;
  }

  .maps-marker-toggle {
    background: #fff;
    border: 1px solid #d0d7de;
    cursor: pointer;
    font: inherit;
    font-size: 0.85rem;
    padding: 0.35rem 0.5rem;
  }

  .maps-count {
    color: #57606a;
    display: block;
    font-size: 0.9rem;
    margin-top: 0.25rem;
  }

  .maps-filter {
    border: 1px solid #d0d7de;
    box-sizing: border-box;
    font: inherit;
    margin-top: 0.75rem;
    padding: 0.55rem 0.65rem;
    width: 100%;
  }

  .maps-list {
    list-style: none;
    margin: 0;
    overflow: auto;
    padding: 0;
  }

  .maps-place {
    border-bottom: 1px solid #d8dee4;
    cursor: pointer;
  }

  .maps-place:hover,
  .maps-place:focus {
    background: #fff;
    outline: none;
  }

  .maps-place strong,
  .maps-place span {
    display: block;
  }

  .maps-place span {
    color: #57606a;
    font-size: 0.9rem;
    margin-top: 0.25rem;
  }

  .maps-panel__empty {
    color: #57606a;
  }

  @media (max-width: 760px) {
    .maps-page,
    .maps-shell {
      height: calc(100vh - 48px);
      height: calc(100dvh - 48px);
      min-height: 0;
    }

    #ray-map {
      height: calc(100vh - 48px);
      height: calc(100dvh - 48px);
      min-height: 0;
    }

    .maps-panel {
      bottom: 0.75rem;
      max-height: 40vh;
      right: 0.75rem;
      top: auto;
      width: calc(100vw - 1.5rem);
    }
  }
</style>

<section class="maps-page">
  <div class="maps-shell">
    <div id="ray-map" aria-label="Interactive map"></div>

    <aside class="maps-panel" aria-label="Map locations">
      <div class="maps-panel__header">
        <div class="maps-panel__heading">
          <strong>Map Locations</strong>
          <button class="maps-marker-toggle" type="button" data-map-marker-toggle aria-pressed="false">Tiny dots</button>
        </div>
        <span class="maps-count" data-map-count>0 mapped</span>
        <label class="screen-reader-text" for="maps-filter">Filter map locations</label>
        <input class="maps-filter" id="maps-filter" type="search" placeholder="Filter locations" autocomplete="off">
      </div>
      <ul class="maps-list" data-map-list></ul>
      <p class="maps-panel__empty" data-map-empty>No locations added yet.</p>
    </aside>
  </div>
</section>

<script src="/leaflet/leaflet.js"></script>
<script src="https://unpkg.com/maplibre-gl@5/dist/maplibre-gl.js"></script>
<script src="https://unpkg.com/@maplibre/maplibre-gl-leaflet@0.1.4/dist/leaflet-maplibre-gl.js"></script>
<script src="/leaflet/extramarkers/js/leaflet.extra-markers.min.js"></script>
<script src="/leaflet/zoomhome/leaflet.zoomhome.min.js"></script>
<script src="/leaflet/fullscreen/Control.FullScreen.js"></script>
<script>
  window.rayMapsPlaces = window.rayMapsPlaces || [];

  (function () {
    const places = window.rayMapsPlaces;
    const map = L.map("ray-map", {
      minZoom: 4,
      maxZoom: 20,
      maxBounds: [[-85.051129, -Infinity], [85.051129, Infinity]],
      maxBoundsViscosity: 1,
      zoomControl: false,
      scrollWheelZoom: true,
      fullscreenControl: true,
      fullscreenControlOptions: {
        position: "topleft"
      }
    }).setView([30.3322, -81.6557], 11);

    L.Control.zoomHome().addTo(map);

    const openFreeMapStyles = {
      light: "https://tiles.openfreemap.org/styles/positron",
      dark: "https://tiles.openfreemap.org/styles/dark"
    };
    let openFreeMapLayer;
    let activeOpenFreeMapStyle;

    function isDarkModeEnabled() {
      const storedDarkMode = localStorage.getItem("darkMode");
      return storedDarkMode === "enabled" ||
        (window.matchMedia &&
          window.matchMedia("(prefers-color-scheme: dark)").matches &&
          storedDarkMode !== "disabled");
    }

    function setOpenFreeMapStyle() {
      const nextStyle = isDarkModeEnabled() ? openFreeMapStyles.dark : openFreeMapStyles.light;
      if (activeOpenFreeMapStyle === nextStyle) return;
      if (!window.maplibregl || /HeadlessChrome/.test(window.navigator.userAgent) || (maplibregl.supported && !maplibregl.supported({ failIfMajorPerformanceCaveat: true }))) {
        return;
      }
      if (openFreeMapLayer) {
        map.removeLayer(openFreeMapLayer);
      }
      openFreeMapLayer = L.maplibreGL({
        style: nextStyle
      }).addTo(map);
      activeOpenFreeMapStyle = nextStyle;
    }

    map.attributionControl.addAttribution(
      '<a href="https://openfreemap.org/" target="_blank" rel="noopener">OpenFreeMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>'
    );

    const markerIcon = window.L.ExtraMarkers ? L.ExtraMarkers.icon({
      icon: "fa-map-marker-alt",
      markerColor: "black",
      shape: "circle",
      prefix: "fas"
    }) : undefined;
    const activePlaceLayer = L.layerGroup().addTo(map);
    const archivedPlaceLayer = L.layerGroup();
    let markerMode = "markers";

    L.control.layers(null, {
      "Active places": activePlaceLayer,
      "Archived places": archivedPlaceLayer
    }, {
      collapsed: false
    }).addTo(map);

    const list = document.querySelector("[data-map-list]");
    const count = document.querySelector("[data-map-count]");
    const empty = document.querySelector("[data-map-empty]");
    const filter = document.getElementById("maps-filter");
    const markerToggle = document.querySelector("[data-map-marker-toggle]");

    function placeMatchesFilter(place, query) {
      if (!query) return true;
      return [place.name, place.title, place.address, place.description, place.status]
        .filter(Boolean)
        .join(" ")
        .toLowerCase()
        .includes(query);
    }

    function normalizePlace(place) {
      return {
        address: place.address || "",
        description: place.description || "",
        lat: Number.parseFloat(place.lat),
        lng: Number.parseFloat(place.lng),
        name: place.name || place.title || "Map location",
        seating: place.seating || place.seats || place.capacity || "",
        status: place.status || "Active",
        url: place.url || "",
        zoom: place.zoom
      };
    }

    function createPlacePopup(place) {
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      title.textContent = place.name;
      popup.appendChild(title);

      if (place.status) {
        const status = document.createElement("span");
        status.textContent = place.status;
        popup.appendChild(status);
      }

      if (place.seating) {
        const seats = document.createElement("span");
        const seatCount = Number.parseInt(place.seating, 10);
        seats.textContent = Number.isFinite(seatCount) ? `${seatCount.toLocaleString()} seats` : `${place.seating} seats`;
        popup.appendChild(seats);
      }

      if (place.address) {
        const address = document.createElement("address");
        String(place.address).split(/\n/).forEach((line, index) => {
          if (index) address.appendChild(document.createElement("br"));
          address.appendChild(document.createTextNode(line));
        });
        popup.appendChild(address);
      }

      if (place.url) {
        const link = document.createElement("a");
        link.href = place.url;
        link.textContent = "View location";
        popup.appendChild(link);
      }

      return popup;
    }

    function addPlaceMarker(place) {
      const targetLayer = place.status === "Archive" ? archivedPlaceLayer : activePlaceLayer;
      const marker = markerMode === "dots"
        ? L.circleMarker([place.lat, place.lng], {
            radius: 2,
            color: "#171717",
            fillColor: "#171717",
            fillOpacity: 0.95,
            opacity: 1,
            stroke: false,
            weight: 0
          })
        : L.marker([place.lat, place.lng], Object.assign({
            title: place.name
          }, markerIcon ? { icon: markerIcon } : {}));

      marker.bindPopup(createPlacePopup(place)).addTo(targetLayer);
      return marker;
    }

    function renderPlaces() {
      const query = filter.value.trim().toLowerCase();
      const visiblePlaces = places
        .filter((place) => placeMatchesFilter(place, query))
        .map(normalizePlace)
        .filter((place) => Number.isFinite(place.lat) && Number.isFinite(place.lng));
      const bounds = L.latLngBounds([]);

      activePlaceLayer.clearLayers();
      archivedPlaceLayer.clearLayers();
      list.innerHTML = "";
      count.textContent = `${visiblePlaces.length} mapped`;
      empty.hidden = visiblePlaces.length > 0;

      visiblePlaces.forEach((place) => {
        const marker = addPlaceMarker(place);
        const item = document.createElement("li");
        const itemName = document.createElement("strong");

        item.className = "maps-place";
        item.tabIndex = 0;
        itemName.textContent = place.name;
        item.appendChild(itemName);

        if (place.address) {
          const itemAddress = document.createElement("span");
          itemAddress.textContent = place.address;
          item.appendChild(itemAddress);
        }

        item.addEventListener("click", () => {
          map.setView([place.lat, place.lng], place.zoom || 15);
          marker.openPopup();
        });
        item.addEventListener("keydown", (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            item.click();
          }
        });
        list.appendChild(item);

        bounds.extend([place.lat, place.lng]);
      });

      if (visiblePlaces.length > 1) {
        map.fitBounds(bounds, { padding: [24, 24] });
      } else if (visiblePlaces.length === 1) {
        map.setView([visiblePlaces[0].lat, visiblePlaces[0].lng], visiblePlaces[0].zoom || 14);
      }
    }

    if (markerToggle) {
      markerToggle.addEventListener("click", function () {
        markerMode = markerMode === "markers" ? "dots" : "markers";
        markerToggle.setAttribute("aria-pressed", String(markerMode === "dots"));
        markerToggle.textContent = markerMode === "dots" ? "Big markers" : "Tiny dots";
        renderPlaces();
      });
    }

    filter.addEventListener("input", renderPlaces);
    renderPlaces();

    setOpenFreeMapStyle();

    new MutationObserver(setOpenFreeMapStyle).observe(document.body, {
      attributes: true,
      attributeFilter: ["class"]
    });

    if (window.matchMedia) {
      const darkModeQuery = window.matchMedia("(prefers-color-scheme: dark)");
      if (darkModeQuery.addEventListener) {
        darkModeQuery.addEventListener("change", setOpenFreeMapStyle);
      } else if (darkModeQuery.addListener) {
        darkModeQuery.addListener(setOpenFreeMapStyle);
      }
    }
  })();
</script>
