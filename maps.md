---
layout: page
title: Maps
permalink: /maps/
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.9.0/dist/maplibre-gl.css">

<style>
  .maps-page {
    display: grid;
    gap: 1.5rem;
  }

  .maps-intro {
    max-width: 44rem;
  }

  .maps-intro p {
    font-size: 1.05rem;
    line-height: 1.55;
  }

  .maps-shell {
    border: 1px solid #d8dee4;
    display: grid;
    grid-template-columns: minmax(0, 1fr) 18rem;
    min-height: 34rem;
  }

  #ray-map {
    min-height: 34rem;
    width: 100%;
  }

  .maps-panel {
    background: #f6f8fa;
    border-left: 1px solid #d8dee4;
    display: flex;
    flex-direction: column;
    min-width: 0;
  }

  .maps-panel__header,
  .maps-panel__empty,
  .maps-place {
    padding: 1rem;
  }

  .maps-panel__header {
    border-bottom: 1px solid #d8dee4;
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
    .maps-shell {
      grid-template-columns: 1fr;
    }

    #ray-map {
      min-height: 28rem;
    }

    .maps-panel {
      border-left: 0;
      border-top: 1px solid #d8dee4;
    }
  }
</style>

<section class="maps-page">
  <div class="maps-intro">
    <p>Places, routes, and notes will live here.</p>
  </div>

  <div class="maps-shell">
    <div id="ray-map" aria-label="Interactive map"></div>

    <aside class="maps-panel" aria-label="Map locations">
      <div class="maps-panel__header">
        <strong>Map Locations</strong>
        <span class="maps-count" data-map-count>0 mapped</span>
        <label class="screen-reader-text" for="maps-filter">Filter map locations</label>
        <input class="maps-filter" id="maps-filter" type="search" placeholder="Filter locations" autocomplete="off">
      </div>
      <ul class="maps-list" data-map-list></ul>
      <p class="maps-panel__empty" data-map-empty>No locations added yet.</p>
    </aside>
  </div>
</section>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/maplibre-gl@5.9.0/dist/maplibre-gl.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@maplibre/maplibre-gl-leaflet@0.1.4/leaflet-maplibre-gl.js"></script>
<script>
  window.rayMapsPlaces = window.rayMapsPlaces || [];

  (function () {
    const places = window.rayMapsPlaces;
    const map = L.map("ray-map", {
      scrollWheelZoom: false
    }).setView([30.3322, -81.6557], 11);

    L.maplibreGL({
      style: "https://tiles.openfreemap.org/styles/liberty"
    }).addTo(map);

    map.attributionControl.addAttribution(
      '<a href="https://openfreemap.org/" target="_blank" rel="noopener">OpenFreeMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>'
    );

    const markers = L.layerGroup().addTo(map);
    const list = document.querySelector("[data-map-list]");
    const count = document.querySelector("[data-map-count]");
    const empty = document.querySelector("[data-map-empty]");
    const filter = document.getElementById("maps-filter");

    function placeMatchesFilter(place, query) {
      if (!query) return true;
      return [place.name, place.address, place.description]
        .filter(Boolean)
        .join(" ")
        .toLowerCase()
        .includes(query);
    }

    function renderPlaces() {
      const query = filter.value.trim().toLowerCase();
      const visiblePlaces = places.filter((place) => placeMatchesFilter(place, query));
      const bounds = L.latLngBounds([]);

      markers.clearLayers();
      list.innerHTML = "";
      count.textContent = `${visiblePlaces.length} mapped`;
      empty.hidden = visiblePlaces.length > 0;

      visiblePlaces.forEach((place) => {
        const popup = document.createElement("div");
        const popupName = document.createElement("strong");
        popupName.textContent = place.name;
        popup.appendChild(popupName);

        if (place.address) {
          popup.appendChild(document.createElement("br"));
          popup.appendChild(document.createTextNode(place.address));
        }

        const marker = L.marker([place.lat, place.lng])
          .bindPopup(popup)
          .addTo(markers);

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

    filter.addEventListener("input", renderPlaces);
    renderPlaces();
  })();
</script>
