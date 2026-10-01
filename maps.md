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
    position: relative;
    z-index: 0;
  }

  body {
    overflow: hidden;
  }

  .site-header {
    z-index: 1200;
  }

  .site-nav {
    z-index: 1201;
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

  .maps-district-popup strong,
  .maps-district-popup span,
  .maps-district-popup a {
    display: block;
  }

  .maps-district-popup span {
    margin-top: 0.25rem;
  }

  .maps-control-panel,
  .maps-basemap-control {
    background: #fff;
    overflow: hidden;
  }

  .maps-control-panel.is-open {
    display: flex;
    flex-direction: column;
  }

  .maps-control-panel__toggle {
    align-items: center;
    background: #fff;
    border: 0;
    border-bottom: 1px solid #d0d7de;
    color: #24292f;
    cursor: pointer;
    display: flex;
    font: inherit;
    font-weight: 600;
    justify-content: space-between;
    line-height: normal;
    min-width: 7rem;
    padding: 0.45rem 0.6rem;
    text-align: left;
    width: 100%;
  }

  .maps-control-panel__toggle::after {
    content: "Hide";
    color: #57606a;
    font-size: 0.78rem;
    font-weight: 400;
    margin-left: 0.75rem;
  }

  .maps-control-panel:not(.is-open) .maps-control-panel__toggle {
    border-bottom: 0;
  }

  .maps-control-panel:not(.is-open) .maps-control-panel__toggle::after {
    content: "Show";
  }

  .maps-control-panel:not(.is-open) .maps-control-panel__body {
    display: none;
  }

  .maps-control-panel__toggle--icon {
    border-bottom: 0;
    border-radius: 0;
    color: #000;
    justify-content: center;
    height: 30px;
    line-height: 30px;
    min-height: 0;
    min-width: 0;
    padding: 0;
    width: 30px;
  }

  .maps-control-panel__toggle--icon::after {
    content: "";
    margin-left: 0;
  }

  .maps-control-panel:not(.is-open) .maps-control-panel__toggle--icon::after {
    content: "";
  }

  .maps-control-panel__toggle--icon svg {
    display: block;
    fill: currentColor;
    height: 16px;
    width: 16px;
  }

  .maps-control-panel.is-open .leaflet-control-layers-list {
    display: block;
  }

  .maps-control-panel__body {
    max-height: calc(100dvh - 2rem);
    min-height: 0;
    overflow: auto;
  }

  .maps-layers-control .maps-control-panel__body {
    max-height: calc(100vh - 10rem);
    max-height: calc(100dvh - 10rem);
    overflow-y: auto;
  }

  .maps-basemap-control .maps-control-panel__body {
    display: flex;
    flex-direction: column;
  }

  .maps-basemap-control button[data-base-map] {
    background: #fff;
    border: 0;
    cursor: pointer;
    font: inherit;
  }

  .maps-basemap-control button[data-base-map] {
    border-bottom: 1px solid #d0d7de;
    min-width: 7rem;
    padding: 0.45rem 0.6rem;
    text-align: left;
  }

  .maps-basemap-control button[data-base-map]:last-child {
    border-bottom: 0;
  }

  .maps-basemap-control button[data-base-map][aria-pressed="true"] {
    background: #0969da;
    color: #fff;
  }

  .maps-basemap-control button[data-base-map]:disabled {
    color: #8c959f;
    cursor: not-allowed;
  }

  .maps-layers-control .leaflet-control-layers-list {
    margin: 0;
  }

  .maps-layers-control .leaflet-control-layers-overlays {
    padding: 0.45rem 0.6rem;
  }

  .maps-layer-heading {
    border-top: 1px solid #d0d7de;
    color: #57606a;
    font-size: 0.78rem;
    font-weight: 700;
    margin-top: 0.45rem;
    padding-top: 0.45rem;
    text-transform: uppercase;
  }

  .leaflet-control-layers-overlays > .maps-layer-heading:first-child {
    margin-top: 0;
  }

  .maps-layer-subheading {
    color: #57606a;
    font-size: 0.78rem;
    font-weight: 700;
    margin-top: 0.35rem;
  }

  .maps-layer-group-row {
    display: grid;
    gap: 0.3rem;
    grid-template-columns: minmax(9rem, 1fr);
    align-items: center;
  }

  .leaflet-control-layers-overlays .maps-layer-group-row__name {
    align-items: center;
    display: flex;
    gap: 0.45rem;
    min-width: 0;
  }

  .leaflet-control-layers-overlays .maps-layer-control-row {
    align-items: center;
    display: flex;
    gap: 0.45rem;
    min-width: 0;
  }

  .maps-layer-group-row__name .leaflet-control-layers-selector,
  .maps-layer-control-row .leaflet-control-layers-selector {
    flex: 0 0 auto;
    margin-right: 0;
  }

  .maps-layer-group-row label {
    white-space: nowrap;
  }

  .maps-layer-mode-switch {
    align-items: center;
    display: inline-flex;
  }

  .maps-layers-control {
    position: relative;
  }

  .maps-layers-control > .maps-layer-mode-switch {
    position: absolute;
    right: 6px;
    top: 0;
    z-index: 1;
  }

  .maps-layers-control:not(.is-open) > .maps-layer-mode-switch {
    display: none;
  }

  .maps-layer-mode-switch__track {
    background: black;
    border: 1px solid black;
    box-sizing: border-box;
    border-radius: 0px;
    display: inline-flex;
    height: 16px;
    margin: 7px 0;
    padding: 2px;
    transition: background 0.15s ease, border-color 0.15s ease;
    width: 32px;
  }

  .maps-layer-mode-switch__knob {
    background: #fff;
    border-radius: 1px;
    display: block;
    height: 10px;
    transform: translateX(0);
    transition: background 0.15s ease, transform 0.15s ease;
    width: 12px;
  }

  .maps-layer-mode-switch input {
    position: absolute;
    opacity: 0;
    pointer-events: none;
  }

  .maps-layer-mode-switch input:checked ~ .maps-layer-mode-switch__track {
    background: transparent;
  }

  .maps-layer-mode-switch input:checked ~ .maps-layer-mode-switch__track .maps-layer-mode-switch__knob {
    background: black;
    transform: translateX(14px);
  }

  .leaflet-control-layers-overlays label:focus,
  .leaflet-control-layers-overlays label:focus-within,
  .leaflet-control-layers-overlays span:focus,
  .leaflet-control-layers-selector:focus {
    box-shadow: none;
    outline: 0;
  }

  .leaflet-interactive:focus {
    outline: 0;
  }

  .leaflet-control-locate a {
    cursor: pointer;
  }

  .leaflet-control-locate a .leaflet-control-locate-location-arrow {
    background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="black" d="M445 4 29 195c-48 23-32 93 19 93h176v176c0 51 70 67 93 19L508 67c16-38-25-79-63-63z"/></svg>');
    display: inline-block;
    height: 16px;
    margin: 7px;
    width: 16px;
  }

  .leaflet-control-locate a .leaflet-control-locate-spinner {
    animation: leaflet-control-locate-spin 2s linear infinite;
    background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="black" d="M304 48a48 48 0 1 1-96 0 48 48 0 0 1 96 0zm-48 368a48 48 0 1 0 0 96 48 48 0 0 0 0-96zm208-208a48 48 0 1 0 0 96 48 48 0 0 0 0-96zM96 256a48 48 0 1 0-96 0 48 48 0 0 0 96 0zm13 99a48 48 0 1 0 0 96 48 48 0 0 0 0-96zm294 0a48 48 0 1 0 0 96 48 48 0 0 0 0-96zM109 61a48 48 0 1 0 0 96 48 48 0 0 0 0-96z"/></svg>');
    display: inline-block;
    height: 16px;
    margin: 7px;
    width: 16px;
  }

  .leaflet-control-locate.active a .leaflet-control-locate-location-arrow {
    background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="rgb(32, 116, 182)" d="M445 4 29 195c-48 23-32 93 19 93h176v176c0 51 70 67 93 19L508 67c16-38-25-79-63-63z"/></svg>');
  }

  .leaflet-control-locate.following a .leaflet-control-locate-location-arrow {
    background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="rgb(252, 132, 40)" d="M445 4 29 195c-48 23-32 93 19 93h176v176c0 51 70 67 93 19L508 67c16-38-25-79-63-63z"/></svg>');
  }

  @keyframes leaflet-control-locate-spin {
    0% {
      transform: rotate(0deg);
    }

    100% {
      transform: rotate(360deg);
    }
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

    .maps-control-panel {
      max-width: min(17rem, calc(100vw - 5rem));
    }

    .leaflet-touch .maps-control-panel__toggle--icon {
      height: 30px;
      line-height: 30px;
      width: 30px;
    }

    .maps-control-panel.is-open {
      max-height: calc(100dvh - 0.75rem);
    }

    .maps-control-panel__body {
      max-height: calc(100dvh - 5rem);
      overflow: auto;
    }
  }
</style>

<section class="maps-page">
  <div class="maps-shell">
    <div id="ray-map" aria-label="Interactive map"></div>
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
      fullscreenControl: false
    }).setView([30.3322, -81.6557], 11);
    let isolatedBoundaryLayer = null;
    let skipNextBoundaryRestoreClick = false;

    const openFreeMapStyles = {
      positron: "https://tiles.openfreemap.org/styles/positron",
      bright: "https://tiles.openfreemap.org/styles/bright",
      threeD: "https://tiles.openfreemap.org/styles/liberty"
    };
    const baseMapStyles = {
      positron: {
        label: "Positron",
        getStyle: () => openFreeMapStyles.positron
      },
      bright: {
        label: "Bright",
        getStyle: () => openFreeMapStyles.bright
      },
      threeD: {
        label: "3D",
        getStyle: () => openFreeMapStyles.threeD
      },
      googleSatellite: {
        label: "Google Satellite",
        type: "tile",
        url: "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
      }
    };
    let activeBaseMapKey = "positron";
    let baseMapControlElement;
    let baseMapLayer;
    let baseMapRequestId = 0;

    async function setBaseMap(baseMapKey, options) {
      const config = baseMapStyles[baseMapKey];
      const settings = options || {};
      const requestId = ++baseMapRequestId;
      if (!config) return false;
      if (config.type !== "tile" && (!window.maplibregl || /HeadlessChrome/.test(window.navigator.userAgent) || (maplibregl.supported && !maplibregl.supported({ failIfMajorPerformanceCaveat: true })))) {
        return false;
      }
      if (requestId !== baseMapRequestId) {
        return false;
      }
      if (baseMapLayer) {
        map.removeLayer(baseMapLayer);
      }
      if (config.type === "tile") {
        baseMapLayer = L.tileLayer(config.url, {
          attribution: "Google Satellite",
          maxZoom: 20
        }).addTo(map);
      } else {
        let nextStyle;
        try {
          nextStyle = config.getStyle();
        } catch (error) {
          if (!settings.quiet) {
            window.alert(error.message || `Could not load ${config.label} basemap.`);
          }
          return false;
        }
        baseMapLayer = L.maplibreGL({
          style: nextStyle
        }).addTo(map);
      }
      activeBaseMapKey = baseMapKey;
      updateBaseMapControl();
      return true;
    }

    function refreshActiveBaseMap() {
      if (activeBaseMapKey === "positron") {
        setBaseMap("positron", { quiet: true });
      }
    }

    function updateBaseMapControl() {
      if (!baseMapControlElement) return;
      baseMapControlElement.querySelectorAll("button[data-base-map]").forEach((button) => {
        const key = button.dataset.baseMap;
        button.setAttribute("aria-pressed", String(key === activeBaseMapKey));
      });
    }

    function setupCollapsibleMapControl(container, label, body, options) {
      const toggle = document.createElement("button");
      const settings = options || {};
      const viewportPadding = 12;

      container.classList.add("maps-control-panel");
      body.classList.add("maps-control-panel__body");
      toggle.type = "button";
      toggle.className = "maps-control-panel__toggle";
      toggle.setAttribute("aria-label", `${label} control`);
      toggle.title = label;
      if (settings.iconPath) {
        const icon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        icon.setAttribute("viewBox", settings.iconViewBox || "0 0 640 640");
        icon.setAttribute("aria-hidden", "true");
        icon.setAttribute("focusable", "false");
        path.setAttribute("d", settings.iconPath);
        icon.appendChild(path);
        toggle.classList.add("maps-control-panel__toggle--icon");
        toggle.appendChild(icon);
      } else {
        toggle.textContent = label;
      }
      container.insertBefore(toggle, body);

      function fitOpenPanelToViewport() {
        if (!container.classList.contains("is-open")) return;
        const containerTop = container.getBoundingClientRect().top;
        const availableHeight = Math.max(160, window.innerHeight - containerTop - viewportPadding);
        const bodyHeight = Math.max(120, availableHeight - toggle.offsetHeight);
        container.style.maxHeight = `${availableHeight}px`;
        body.style.maxHeight = `${bodyHeight}px`;
      }

      function clearPanelViewportFit() {
        container.style.maxHeight = "";
        body.style.maxHeight = "";
      }

      function setOpen(open) {
        container.classList.toggle("is-open", open);
        toggle.setAttribute("aria-expanded", String(open));
        if (open) {
          fitOpenPanelToViewport();
          window.requestAnimationFrame(fitOpenPanelToViewport);
        } else {
          clearPanelViewportFit();
        }
      }

      toggle.addEventListener("click", function () {
        setOpen(!container.classList.contains("is-open"));
      });
      window.addEventListener("resize", fitOpenPanelToViewport);
      window.addEventListener("orientationchange", fitOpenPanelToViewport);
      document.addEventListener("pointerdown", function (event) {
        if (container.classList.contains("is-open") && !container.contains(event.target)) {
          setOpen(false);
        }
      }, true);
      setOpen(false);
      return { setOpen };
    }

    function addBaseMapControl() {
      const BaseMapControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "maps-basemap-control leaflet-bar leaflet-control");
          const body = document.createElement("div");
          let controlApi;
          container.appendChild(body);
          Object.entries(baseMapStyles).forEach(([key, config]) => {
            const button = document.createElement("button");
            button.type = "button";
            button.dataset.baseMap = key;
            button.textContent = config.label;
            button.title = `Use ${config.label} basemap`;
            button.addEventListener("click", () => {
              setBaseMap(key).then((selected) => {
                if (selected && controlApi) {
                  controlApi.setOpen(false);
                }
              });
            });
            body.appendChild(button);
          });
          controlApi = setupCollapsibleMapControl(container, "Basemap", body, {
            iconPath: "M576 112C576 103.7 571.7 96 564.7 91.6C557.7 87.2 548.8 86.8 541.4 90.5L416.5 152.1L244 93.4C230.3 88.7 215.3 89.6 202.1 95.7L77.8 154.3C69.4 158.2 64 166.7 64 176L64 528C64 536.2 68.2 543.9 75.1 548.3C82 552.7 90.7 553.2 98.2 549.7L225.5 489.8L396.2 546.7C409.9 551.3 424.7 550.4 437.8 544.2L562.2 485.7C570.6 481.7 576 473.3 576 464L576 112zM208 146.1L208 445.1L112 490.3L112 191.3L208 146.1zM256 449.4L256 148.3L384 191.8L384 492.1L256 449.4zM432 198L528 150.6L528 448.8L432 494L432 198z"
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          baseMapControlElement = container;
          updateBaseMapControl();
          return container;
        }
      });

      map.addControl(new BaseMapControl());
    }

    let userAccuracyCircle;
    let userLocationMarker;
    let locateControlContainer;
    let locateControlIcon;

    function addLocateControl() {
      const LocateControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "leaflet-control-locate leaflet-bar leaflet-control");
          const link = L.DomUtil.create("a", "leaflet-bar-part leaflet-bar-part-single", container);
          const icon = L.DomUtil.create("span", "leaflet-control-locate-location-arrow", link);
          link.href = "#";
          link.title = "Show me where I am";
          link.setAttribute("role", "button");
          link.setAttribute("aria-label", "Show me where I am");
          link.addEventListener("click", function (event) {
            event.preventDefault();
            L.DomUtil.addClass(container, "requesting");
            L.DomUtil.removeClass(container, "active");
            L.DomUtil.removeClass(container, "following");
            L.DomUtil.removeClass(icon, "leaflet-control-locate-location-arrow");
            L.DomUtil.addClass(icon, "leaflet-control-locate-spinner");
            map.locate({
              enableHighAccuracy: true,
              maxZoom: 16,
              setView: true
            });
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          locateControlContainer = container;
          locateControlIcon = icon;
          return container;
        }
      });

      map.addControl(new LocateControl());
    }

    function setLocateControlState(state) {
      if (!locateControlContainer || !locateControlIcon) return;
      L.DomUtil.removeClass(locateControlContainer, "requesting");
      L.DomUtil.removeClass(locateControlContainer, "active");
      L.DomUtil.removeClass(locateControlContainer, "following");
      L.DomUtil.removeClass(locateControlIcon, "leaflet-control-locate-spinner");
      L.DomUtil.addClass(locateControlIcon, "leaflet-control-locate-location-arrow");
      if (state) {
        L.DomUtil.addClass(locateControlContainer, state);
      }
    }

    map.on("locationfound", function (event) {
      setLocateControlState("following");

      if (userLocationMarker) {
        map.removeLayer(userLocationMarker);
      }
      if (userAccuracyCircle) {
        map.removeLayer(userAccuracyCircle);
      }

      userLocationMarker = L.marker(event.latlng, {
        title: "Your location"
      }).addTo(map).bindPopup("You are here");
      userAccuracyCircle = L.circle(event.latlng, {
        color: "#0969da",
        fillColor: "#0969da",
        fillOpacity: 0.12,
        radius: event.accuracy || 0,
        weight: 1
      }).addTo(map);
    });

    map.on("locationerror", function (error) {
      setLocateControlState();
      window.alert(error.message || "Could not determine your location.");
    });

    map.on("dragstart zoomstart", function () {
      if (locateControlContainer && L.DomUtil.hasClass(locateControlContainer, "following")) {
        setLocateControlState("active");
      }
    });

    map.on("click", function () {
      if (skipNextBoundaryRestoreClick) {
        skipNextBoundaryRestoreClick = false;
        return;
      }
      if (!isolatedBoundaryLayer) return;
      restoreBoundaryLayerFeatures(isolatedBoundaryLayer);
      isolatedBoundaryLayer = null;
      orderMapLayers();
      syncDistrictLayerInputs();
    });

    map.attributionControl.addAttribution(
      '<a href="https://openfreemap.org/" target="_blank" rel="noopener">OpenFreeMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://github.com/RayHollister/JacksonvilleNeighborhoods" target="_blank" rel="noopener">Jacksonville Neighborhoods</a>'
    );

    const markerIcon = window.L.ExtraMarkers ? L.ExtraMarkers.icon({
      icon: "fa-map-marker-alt",
      markerColor: "black",
      shape: "circle",
      prefix: "fas"
    }) : undefined;
    const activePlaceLayer = L.layerGroup().addTo(map);
    const archivedPlaceLayer = L.layerGroup();
    const councilDistrictFillLayer = L.geoJSON(null, {
      style: (feature) => getCouncilDistrictStyle(feature, "fill"),
      onEachFeature: (feature, layer) => addCouncilDistrictInteractivity(feature, layer, "fill")
    }).addTo(map);
    const councilDistrictBorderLayer = L.geoJSON(null, {
      style: (feature) => getCouncilDistrictStyle(feature, "border"),
      onEachFeature: (feature, layer) => addCouncilDistrictInteractivity(feature, layer, "border")
    });
    const councilAtLargeFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "atLarge"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "atLarge")
    });
    const councilAtLargeBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "atLarge"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "atLarge")
    });
    const cityFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "city"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "city")
    });
    const cityBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "city"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "city")
    });
    const neighborhoodFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "neighborhood"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "neighborhood")
    });
    const neighborhoodBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "neighborhood"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "neighborhood")
    });
    const neighborhoodOrganizationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getNeighborhoodOrganizationStyle()),
      onEachFeature: (feature, layer) => addNeighborhoodOrganizationInteractivity(feature, layer)
    });
    const cpacFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "cpac"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "cpac")
    });
    const cpacBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "cpac"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "cpac")
    });
    const floridaHouseFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "floridaHouse"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "floridaHouse")
    });
    const floridaHouseBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "floridaHouse"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "floridaHouse")
    });
    const floridaSenateFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "floridaSenate"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "floridaSenate")
    });
    const floridaSenateBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "floridaSenate"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "floridaSenate")
    });
    const zipCodeFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "zipCode"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "zipCode")
    });
    const zipCodeBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "zipCode"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "zipCode")
    });
    const congressionalDistrictFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "congressional"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "congressional")
    });
    const congressionalDistrictBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "congressional"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "congressional")
    });
    const jsoDistrictFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "jsoDistrict"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "jsoDistrict")
    });
    const jsoDistrictBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "jsoDistrict"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "jsoDistrict")
    });
    const jsoSubsectionFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "jsoSubsector"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "jsoSubsector")
    });
    const jsoSubsectionBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "jsoSubsector"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "jsoSubsector")
    });
    const jsoPoliceStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getPoliceStationStyle()),
      onEachFeature: (feature, layer) => addPoliceStationInteractivity(feature, layer)
    });
    const busRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addBusRouteInteractivity(feature, layer)
    });
    const busStopsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getBusStopStyle()),
      onEachFeature: (feature, layer) => addBusStopInteractivity(feature, layer)
    });
    const elementarySchoolsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle("elementary")),
      onEachFeature: (feature, layer) => addSchoolInteractivity(feature, layer)
    });
    const middleSchoolsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle("middle")),
      onEachFeature: (feature, layer) => addSchoolInteractivity(feature, layer)
    });
    const highSchoolsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle("high")),
      onEachFeature: (feature, layer) => addSchoolInteractivity(feature, layer)
    });
    const dedicatedMagnetSchoolsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle("magnet")),
      onEachFeature: (feature, layer) => addSchoolInteractivity(feature, layer)
    });
    const fldoeTraditionalElementarySchoolsLayer = createFldoeSchoolLayer("elementary");
    const fldoeTraditionalMiddleSchoolsLayer = createFldoeSchoolLayer("middle");
    const fldoeTraditionalHighSchoolsLayer = createFldoeSchoolLayer("high");
    const fldoeTraditionalCombinationSchoolsLayer = createFldoeSchoolLayer("combination");
    const fldoeTraditionalMagnetSchoolsLayer = createFldoeSchoolLayer("magnet");
    const fldoeCharterElementarySchoolsLayer = createFldoeSchoolLayer("elementary");
    const fldoeCharterMiddleSchoolsLayer = createFldoeSchoolLayer("middle");
    const fldoeCharterHighSchoolsLayer = createFldoeSchoolLayer("high");
    const fldoeCharterCombinationSchoolsLayer = createFldoeSchoolLayer("combination");
    const privateElementarySchoolsLayer = createPrivateSchoolLayer("elementary");
    const privateMiddleSchoolsLayer = createPrivateSchoolLayer("middle");
    const privateHighSchoolsLayer = createPrivateSchoolLayer("high");
    const privateCombinationSchoolsLayer = createPrivateSchoolLayer("combination");
    const postSecondarySchoolsLayer = createFldoeSchoolLayer("postSecondary");
    const boundaryLayerControls = [];
    const geographyLayerControls = [];
    let governmentLayerMode = "fill";
    let governmentLayerModeInput;

    function moveLayerGroup(layer, direction) {
      if (!map.hasLayer(layer) || !layer.eachLayer) return;
      layer.eachLayer((childLayer) => {
        if (childLayer[direction]) {
          childLayer[direction]();
        }
      });
    }

    function orderMapLayers() {
      [
        councilDistrictFillLayer,
        councilDistrictBorderLayer,
        councilAtLargeFillLayer,
        councilAtLargeBorderLayer,
        cityFillLayer,
        cityBorderLayer,
        neighborhoodFillLayer,
        neighborhoodBorderLayer,
        cpacFillLayer,
        cpacBorderLayer,
        floridaHouseFillLayer,
        floridaHouseBorderLayer,
        floridaSenateFillLayer,
        floridaSenateBorderLayer,
        zipCodeFillLayer,
        zipCodeBorderLayer,
        congressionalDistrictFillLayer,
        congressionalDistrictBorderLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer
      ].forEach((layer) => moveLayerGroup(layer, "bringToBack"));

      moveLayerGroup(busRoutesLayer, "bringToFront");
      moveLayerGroup(jsoPoliceStationsLayer, "bringToFront");
      moveLayerGroup(neighborhoodOrganizationsLayer, "bringToFront");
      [
        elementarySchoolsLayer,
        middleSchoolsLayer,
        highSchoolsLayer,
        dedicatedMagnetSchoolsLayer,
        fldoeTraditionalElementarySchoolsLayer,
        fldoeTraditionalMiddleSchoolsLayer,
        fldoeTraditionalHighSchoolsLayer,
        fldoeTraditionalCombinationSchoolsLayer,
        fldoeTraditionalMagnetSchoolsLayer,
        fldoeCharterElementarySchoolsLayer,
        fldoeCharterMiddleSchoolsLayer,
        fldoeCharterHighSchoolsLayer,
        fldoeCharterCombinationSchoolsLayer,
        privateElementarySchoolsLayer,
        privateMiddleSchoolsLayer,
        privateHighSchoolsLayer,
        privateCombinationSchoolsLayer,
        postSecondarySchoolsLayer
      ].forEach((layer) => moveLayerGroup(layer, "bringToFront"));
      moveLayerGroup(busStopsLayer, "bringToFront");
    }

    function syncDistrictLayerInputs() {
      boundaryLayerControls.forEach((control) => {
        if (control.syncInput) {
          control.syncInput();
        } else if (control.input) {
          control.input.checked = map.hasLayer(control.layer);
        }
      });
    }

    function getBoundaryFeatureStyle(feature, mode, layerType) {
      return layerType === "district"
        ? getCouncilDistrictStyle(feature, mode)
        : getBoundaryStyle(feature, mode, layerType);
    }

    function restoreBoundaryLayerFeatures(layerGroup) {
      if (!layerGroup.eachLayer) return;
      layerGroup.eachLayer((featureLayer) => {
        const options = featureLayer.options || {};
        if (featureLayer.setStyle && featureLayer.feature && options.boundaryMode && options.boundaryType) {
          featureLayer.setStyle(getBoundaryFeatureStyle(featureLayer.feature, options.boundaryMode, options.boundaryType));
        }
        if (featureLayer._path) {
          featureLayer._path.style.pointerEvents = "";
        }
      });
    }

    function hideBoundaryFeature(featureLayer) {
      if (featureLayer.setStyle) {
        featureLayer.setStyle({
          fillOpacity: 0,
          opacity: 0,
          weight: 0
        });
      }
      if (featureLayer.closeTooltip) featureLayer.closeTooltip();
      if (featureLayer.closePopup) featureLayer.closePopup();
      if (featureLayer._path) {
        featureLayer._path.style.pointerEvents = "none";
      }
    }

    function isolateBoundaryFeature(activeLayer, activeFeatureLayer) {
      hideOtherBoundaryLayers(activeLayer);
      restoreBoundaryLayerFeatures(activeLayer);
      if (activeLayer.eachLayer) {
        activeLayer.eachLayer((featureLayer) => {
          if (featureLayer !== activeFeatureLayer) {
            hideBoundaryFeature(featureLayer);
          }
        });
      }
      if (activeFeatureLayer._path) {
        activeFeatureLayer._path.style.pointerEvents = "";
      }
      orderMapLayers();
      if (activeFeatureLayer.bringToFront) {
        activeFeatureLayer.bringToFront();
      }
    }

    function zoomToBoundaryFeature(featureLayer) {
      if (featureLayer.getBounds) {
        const bounds = featureLayer.getBounds();
        if (bounds.isValid()) {
          map.fitBounds(bounds, {
            animate: true,
            maxZoom: 15,
            padding: [32, 32]
          });
        }
      }
    }

    function handleBoundaryFeatureClick(event, activeLayer, activeFeatureLayer) {
      isolateBoundaryFeature(activeLayer, activeFeatureLayer);
      isolatedBoundaryLayer = activeLayer;
      skipNextBoundaryRestoreClick = true;
      window.setTimeout(() => {
        skipNextBoundaryRestoreClick = false;
      }, 0);
      if (event.originalEvent && event.originalEvent.shiftKey) {
        zoomToBoundaryFeature(activeFeatureLayer);
      }
    }

    function setBoundaryLayer(control, enabled, allowMultiple) {
      if (enabled) {
        if (!map.hasLayer(control.layer)) map.addLayer(control.layer);
        restoreBoundaryLayerFeatures(control.layer);
        if (control.group && !allowMultiple) {
          boundaryLayerControls.forEach((otherControl) => {
            if (otherControl !== control && otherControl.group === control.group && map.hasLayer(otherControl.layer)) {
              map.removeLayer(otherControl.layer);
            }
          });
        }
      } else if (map.hasLayer(control.layer)) {
        map.removeLayer(control.layer);
        if (isolatedBoundaryLayer === control.layer) {
          isolatedBoundaryLayer = null;
        }
      }
      orderMapLayers();
      syncDistrictLayerInputs();
    }

    function hideOtherBoundaryLayers(activeLayer) {
      boundaryLayerControls.forEach((control) => {
        if (control.group === "boundaries" && control.layer !== activeLayer && map.hasLayer(control.layer)) {
          map.removeLayer(control.layer);
        }
      });
      orderMapLayers();
      syncDistrictLayerInputs();
    }

    function createBoundaryLayerInput(label, layer, options) {
      const labelElement = document.createElement("label");
      const input = document.createElement("input");
      const text = document.createElement("span");
      const settings = options || {};
      const control = { input, layer, group: settings.group || "" };
      let allowMultipleOnNextChange = false;

      labelElement.className = "maps-layer-control-row";
      input.type = "checkbox";
      input.className = "leaflet-control-layers-selector";
      input.addEventListener("click", function (event) {
        allowMultipleOnNextChange = event.shiftKey;
      });
      input.addEventListener("change", function (event) {
        setBoundaryLayer(control, input.checked, allowMultipleOnNextChange);
        allowMultipleOnNextChange = false;
      });

      text.textContent = label;
      labelElement.appendChild(input);
      labelElement.appendChild(text);
      boundaryLayerControls.push(control);
      return { input, labelElement, control };
    }

    function createLayerGroupToggle(label, layerControls) {
      const labelElement = document.createElement("label");
      const input = document.createElement("input");
      const text = document.createElement("span");
      const controls = layerControls.map((layerControl) => layerControl.control).filter(Boolean);

      function syncInput() {
        input.checked = controls.length > 0 && controls.every((control) => map.hasLayer(control.layer));
        input.indeterminate = controls.some((control) => map.hasLayer(control.layer)) && !input.checked;
      }

      labelElement.className = "maps-layer-control-row";
      input.type = "checkbox";
      input.className = "leaflet-control-layers-selector";
      input.addEventListener("change", function () {
        const enabled = input.checked;
        controls.forEach((control) => {
          setBoundaryLayer(control, enabled, true);
        });
        syncInput();
      });

      text.textContent = label;
      labelElement.appendChild(input);
      labelElement.appendChild(text);
      boundaryLayerControls.push({ syncInput });
      return { input, labelElement };
    }

    function createLayerHeading(label) {
      const heading = document.createElement("div");
      heading.className = "maps-layer-heading";
      heading.textContent = label;
      return heading;
    }

    function createLayerSubheading(label) {
      const heading = document.createElement("div");
      heading.className = "maps-layer-subheading";
      heading.textContent = label;
      return heading;
    }

    function appendLayerControls(parent, controls) {
      controls.forEach((control) => {
        parent.appendChild(control.labelElement);
      });
    }

    function createLayerModeSwitch(label) {
      const modeLabel = document.createElement("label");
      const modeInput = document.createElement("input");
      const modeTrack = document.createElement("span");
      const modeKnob = document.createElement("span");

      modeLabel.className = "maps-layer-mode-switch";
      modeInput.type = "checkbox";
      modeInput.setAttribute("aria-label", label);
      modeTrack.className = "maps-layer-mode-switch__track";
      modeKnob.className = "maps-layer-mode-switch__knob";
      modeTrack.appendChild(modeKnob);
      modeLabel.appendChild(modeInput);
      modeLabel.appendChild(modeTrack);
      return { labelElement: modeLabel, input: modeInput };
    }

    function addGovernmentLayerModeSwitch(container) {
      const modeSwitch = createLayerModeSwitch("Use borders for government layers");

      governmentLayerModeInput = modeSwitch.input;
      governmentLayerModeInput.addEventListener("change", function () {
        setGovernmentLayerMode(governmentLayerModeInput.checked ? "border" : "fill");
      });
      container.appendChild(modeSwitch.labelElement);
    }

    function getSelectedGeographyControl(geographyControl) {
      return governmentLayerMode === "border" ? geographyControl.borderControl : geographyControl.overlayControl;
    }

    function setGovernmentLayerMode(mode) {
      governmentLayerMode = mode;
      if (governmentLayerModeInput) {
        governmentLayerModeInput.checked = mode === "border";
      }
      geographyLayerControls.forEach((geographyControl) => {
        const nextControl = getSelectedGeographyControl(geographyControl);
        const previousControl = mode === "border" ? geographyControl.overlayControl : geographyControl.borderControl;
        const isActive = map.hasLayer(previousControl.layer) || map.hasLayer(nextControl.layer);
        if (!isActive) return;
        if (map.hasLayer(previousControl.layer)) {
          map.removeLayer(previousControl.layer);
        }
        if (!map.hasLayer(nextControl.layer)) {
          map.addLayer(nextControl.layer);
        }
        restoreBoundaryLayerFeatures(nextControl.layer);
      });
      orderMapLayers();
      syncDistrictLayerInputs();
    }

    function appendGeographyLayerRow(parent, name, overlayLayer, borderLayer) {
      const row = document.createElement("div");
      const layerLabel = document.createElement("label");
      const layerInput = document.createElement("input");
      const nameText = document.createElement("span");
      const overlayControl = { layer: overlayLayer, group: "boundaries" };
      const borderControl = { layer: borderLayer, group: "boundaries" };
      const geographyControl = { overlayControl, borderControl };
      let allowMultipleOnNextChange = false;

      row.className = "maps-layer-group-row";
      layerLabel.className = "maps-layer-group-row__name";
      layerInput.type = "checkbox";
      layerInput.className = "leaflet-control-layers-selector";
      nameText.textContent = name;
      layerLabel.appendChild(layerInput);
      layerLabel.appendChild(nameText);

      function getSelectedControl() {
        return getSelectedGeographyControl(geographyControl);
      }

      function syncRowInputs() {
        const isOverlayActive = map.hasLayer(overlayLayer);
        const isBorderActive = map.hasLayer(borderLayer);
        layerInput.checked = isOverlayActive || isBorderActive;
        row.classList.toggle("is-active", layerInput.checked);
      }

      overlayControl.syncInput = syncRowInputs;
      borderControl.syncInput = syncRowInputs;

      layerInput.addEventListener("click", function (event) {
        allowMultipleOnNextChange = event.shiftKey;
      });
      layerInput.addEventListener("change", function () {
        if (layerInput.checked) {
          setBoundaryLayer(getSelectedControl(), true, allowMultipleOnNextChange);
        } else {
          setBoundaryLayer(overlayControl, false, true);
          setBoundaryLayer(borderControl, false, true);
        }
        allowMultipleOnNextChange = false;
      });

      geographyLayerControls.push(geographyControl);
      boundaryLayerControls.push(overlayControl, borderControl);
      row.appendChild(layerLabel);
      parent.appendChild(row);
    }

    function addDistrictLayerControl() {
      const DistrictLayerControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "leaflet-control-layers leaflet-bar leaflet-control maps-layers-control");
          const list = L.DomUtil.create("section", "leaflet-control-layers-list", container);
          const overlays = L.DomUtil.create("div", "leaflet-control-layers-overlays", list);
          overlays.appendChild(createLayerHeading("Government"));
          appendGeographyLayerRow(overlays, "City Council District", councilDistrictFillLayer, councilDistrictBorderLayer);
          appendGeographyLayerRow(overlays, "City Council District At Large", councilAtLargeFillLayer, councilAtLargeBorderLayer);
          appendGeographyLayerRow(overlays, "Cities", cityFillLayer, cityBorderLayer);
          appendGeographyLayerRow(overlays, "Florida House", floridaHouseFillLayer, floridaHouseBorderLayer);
          appendGeographyLayerRow(overlays, "Florida Senate", floridaSenateFillLayer, floridaSenateBorderLayer);
          appendGeographyLayerRow(overlays, "Zip Codes", zipCodeFillLayer, zipCodeBorderLayer);
          appendGeographyLayerRow(overlays, "Congressional Districts", congressionalDistrictFillLayer, congressionalDistrictBorderLayer);
          overlays.appendChild(createLayerHeading("Neighborhood"));
          appendGeographyLayerRow(overlays, "Neighborhoods", neighborhoodFillLayer, neighborhoodBorderLayer);
          appendLayerControls(overlays, [
            createBoundaryLayerInput("Neighborhood Organizations", neighborhoodOrganizationsLayer)
          ]);
          appendGeographyLayerRow(overlays, "Citizens Planning Advisory Committee (CPACs)", cpacFillLayer, cpacBorderLayer);
          overlays.appendChild(createLayerHeading("Jacksonville Sheriff's Office"));
          appendGeographyLayerRow(overlays, "Districts", jsoDistrictFillLayer, jsoDistrictBorderLayer);
          appendGeographyLayerRow(overlays, "Subsections", jsoSubsectionFillLayer, jsoSubsectionBorderLayer);
          appendLayerControls(overlays, [
            createBoundaryLayerInput("Substations", jsoPoliceStationsLayer)
          ]);
          overlays.appendChild(createLayerHeading("Transportation"));
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JTA Bus Routes", busRoutesLayer),
            createBoundaryLayerInput("JTA Bus Stops", busStopsLayer)
          ]);
          const traditionalPublicSchoolControls = [
            createBoundaryLayerInput("Elementary", fldoeTraditionalElementarySchoolsLayer),
            createBoundaryLayerInput("Middle", fldoeTraditionalMiddleSchoolsLayer),
            createBoundaryLayerInput("High", fldoeTraditionalHighSchoolsLayer),
            createBoundaryLayerInput("Combination", fldoeTraditionalCombinationSchoolsLayer),
            createBoundaryLayerInput("Magnet", fldoeTraditionalMagnetSchoolsLayer)
          ];
          const charterPublicSchoolControls = [
            createBoundaryLayerInput("Elementary", fldoeCharterElementarySchoolsLayer),
            createBoundaryLayerInput("Middle", fldoeCharterMiddleSchoolsLayer),
            createBoundaryLayerInput("High", fldoeCharterHighSchoolsLayer),
            createBoundaryLayerInput("Combination", fldoeCharterCombinationSchoolsLayer)
          ];
          const privateSchoolControls = [
            createBoundaryLayerInput("Elementary", privateElementarySchoolsLayer),
            createBoundaryLayerInput("Middle", privateMiddleSchoolsLayer),
            createBoundaryLayerInput("High", privateHighSchoolsLayer),
            createBoundaryLayerInput("Combination", privateCombinationSchoolsLayer)
          ];
          const postSecondarySchoolControls = [
            createBoundaryLayerInput("Post-Secondary Schools", postSecondarySchoolsLayer)
          ];
          const fldoeSchoolControls = traditionalPublicSchoolControls.concat(charterPublicSchoolControls, privateSchoolControls, postSecondarySchoolControls);

          overlays.appendChild(createLayerHeading("Educational Institutions"));
          appendLayerControls(overlays, [
            createLayerGroupToggle("All Schools", fldoeSchoolControls)
          ]);
          appendLayerControls(overlays, postSecondarySchoolControls);
          overlays.appendChild(createLayerSubheading("Traditional Public"));
          appendLayerControls(overlays, [
            createLayerGroupToggle("Toggle all", traditionalPublicSchoolControls)
          ]);
          appendLayerControls(overlays, traditionalPublicSchoolControls);
          overlays.appendChild(createLayerSubheading("Charter Public"));
          appendLayerControls(overlays, [
            createLayerGroupToggle("Toggle all", charterPublicSchoolControls)
          ]);
          appendLayerControls(overlays, charterPublicSchoolControls);
          overlays.appendChild(createLayerSubheading("Private Schools"));
          appendLayerControls(overlays, [
            createLayerGroupToggle("Toggle all", privateSchoolControls)
          ]);
          appendLayerControls(overlays, privateSchoolControls);
          setupCollapsibleMapControl(container, "Layers", list, {
            iconPath: "M296.5 69.2C311.4 62.3 328.6 62.3 343.5 69.2L562.1 170.2C570.6 174.1 576 182.6 576 192C576 201.4 570.6 209.9 562.1 213.8L343.5 314.8C328.6 321.7 311.4 321.7 296.5 314.8L77.9 213.8C69.4 209.8 64 201.3 64 192C64 182.7 69.4 174.1 77.9 170.2L296.5 69.2zM112.1 282.4L276.4 358.3C304.1 371.1 336 371.1 363.7 358.3L528 282.4L562.1 298.2C570.6 302.1 576 310.6 576 320C576 329.4 570.6 337.9 562.1 341.8L343.5 442.8C328.6 449.7 311.4 449.7 296.5 442.8L77.9 341.8C69.4 337.8 64 329.3 64 320C64 310.7 69.4 302.1 77.9 298.2L112 282.4zM77.9 426.2L112 410.4L276.3 486.3C304 499.1 335.9 499.1 363.6 486.3L527.9 410.4L562 426.2C570.5 430.1 575.9 438.6 575.9 448C575.9 457.4 570.5 465.9 562 469.8L343.4 570.8C328.5 577.7 311.3 577.7 296.4 570.8L77.9 469.8C69.4 465.8 64 457.3 64 448C64 438.7 69.4 430.1 77.9 426.2z"
          });
          addGovernmentLayerModeSwitch(container);
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          syncDistrictLayerInputs();
          return container;
        }
      });

      map.addControl(new DistrictLayerControl());
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

    function getDistrictNumber(feature) {
      const properties = feature.properties || {};
      return Number.parseInt(properties.DISTRICT_N || properties.CC || properties.DISTRICT, 10);
    }

    function getBoundaryNumber(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "atLarge") {
        return Number.parseInt(properties.CCAL, 10);
      }
      if (layerType === "city") {
        return Number.parseInt(properties.city_code || properties.FPLACE90, 10);
      }
      if (layerType === "neighborhood") {
        return getStringColorNumber(properties.NAME || properties.NUM_NAME || "Neighborhoods");
      }
      if (layerType === "cpac") {
        return Number.parseInt(properties.cpac_district || properties.DIST || properties.planning_district || properties.PD_ID, 10);
      }
      if (layerType === "floridaHouse") {
        return Number.parseInt(properties.HSE, 10);
      }
      if (layerType === "floridaSenate") {
        return Number.parseInt(properties.SEN, 10);
      }
      if (layerType === "zipCode") {
        return Number.parseInt(properties.ZIPCODE, 10);
      }
      if (layerType === "congressional") {
        return Number.parseInt(properties.BASENAME || properties.GEOID, 10);
      }
      if (layerType === "jsoDistrict") {
        return Number.parseInt(properties.DISTRICT, 10);
      }
      if (layerType === "jsoSubsector") {
        return getStringColorNumber(properties.SUBSECTOR || properties.SECTOR || "Subsection");
      }
      return getDistrictNumber(feature);
    }

    function getStringColorNumber(value) {
      const text = String(value || "");
      let hash = 0;
      for (let index = 0; index < text.length; index += 1) {
        hash = ((hash << 5) - hash) + text.charCodeAt(index);
        hash |= 0;
      }
      return Math.abs(hash) + 1;
    }

    function getBoundaryColor(feature, layerType) {
      const colors = [
        "#2563eb", "#dc2626", "#16a34a", "#9333ea", "#ea580c",
        "#0891b2", "#be123c", "#4f46e5", "#65a30d", "#c026d3",
        "#0f766e", "#b45309", "#0284c7", "#7c3aed"
      ];
      const boundaryNumber = getBoundaryNumber(feature, layerType);
      return colors[((Number.isFinite(boundaryNumber) ? boundaryNumber : 1) - 1) % colors.length];
    }

    function getBoundaryStyle(feature, mode, layerType) {
      const color = getBoundaryColor(feature, layerType);

      return {
        color,
        fillColor: mode === "border" ? "transparent" : color,
        fillOpacity: mode === "border" ? 0 : 0.16,
        opacity: 0.95,
        weight: mode === "border" ? 1.25 : 0.75
      };
    }

    function getCouncilDistrictStyle(feature, mode) {
      return getBoundaryStyle(feature, mode, "district");
    }

    function getBoundaryLayer(layerType, mode) {
      if (layerType === "atLarge") {
        return mode === "border" ? councilAtLargeBorderLayer : councilAtLargeFillLayer;
      }
      if (layerType === "city") {
        return mode === "border" ? cityBorderLayer : cityFillLayer;
      }
      if (layerType === "neighborhood") {
        return mode === "border" ? neighborhoodBorderLayer : neighborhoodFillLayer;
      }
      if (layerType === "cpac") {
        return mode === "border" ? cpacBorderLayer : cpacFillLayer;
      }
      if (layerType === "floridaHouse") {
        return mode === "border" ? floridaHouseBorderLayer : floridaHouseFillLayer;
      }
      if (layerType === "floridaSenate") {
        return mode === "border" ? floridaSenateBorderLayer : floridaSenateFillLayer;
      }
      if (layerType === "zipCode") {
        return mode === "border" ? zipCodeBorderLayer : zipCodeFillLayer;
      }
      if (layerType === "congressional") {
        return mode === "border" ? congressionalDistrictBorderLayer : congressionalDistrictFillLayer;
      }
      if (layerType === "jsoDistrict") {
        return mode === "border" ? jsoDistrictBorderLayer : jsoDistrictFillLayer;
      }
      if (layerType === "jsoSubsector") {
        return mode === "border" ? jsoSubsectionBorderLayer : jsoSubsectionFillLayer;
      }
      return mode === "border" ? councilDistrictBorderLayer : councilDistrictFillLayer;
    }

    function getBoundaryTitle(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "atLarge") {
        return properties.CCAL ? `Council District At Large ${properties.CCAL}` : "Council District At Large";
      }
      if (layerType === "city") {
        return properties.Name || "City";
      }
      if (layerType === "neighborhood") {
        return properties.NAME || properties.NUM_NAME || "Neighborhoods";
      }
      if (layerType === "cpac") {
        return properties.cpac_label || properties.CPAC || properties.NAME || "CPAC / Planning District";
      }
      if (layerType === "floridaHouse") {
        return properties.HSE ? `Florida House District ${properties.HSE}` : "Florida House District";
      }
      if (layerType === "floridaSenate") {
        return properties.SEN ? `Florida Senate District ${properties.SEN}` : "Florida Senate District";
      }
      if (layerType === "zipCode") {
        return properties.ZIPCODE ? `ZIP Code ${properties.ZIPCODE}` : "ZIP Code";
      }
      if (layerType === "congressional") {
        return properties.BASENAME ? `Florida's ${properties.BASENAME}th Congressional District` : "Florida Congressional District";
      }
      if (layerType === "jsoDistrict") {
        return properties.DISTRICT ? `JSO District ${properties.DISTRICT}` : "JSO District";
      }
      if (layerType === "jsoSubsector") {
        return properties.SUBSECTOR ? `JSO Subsection ${properties.SUBSECTOR}` : "JSO Subsection";
      }
      const district = properties.CC || properties.DISTRICT_N || properties.DISTRICT || "";
      return district ? `City Council District ${district}` : "City Council District";
    }

    function getBoundarySubtitle(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "atLarge") {
        return properties.C_NAME || "";
      }
      if (layerType === "city") {
        return properties.ESN ? `ESN ${properties.ESN}` : "";
      }
      if (layerType === "neighborhood") {
        return properties.NUM_NAME && properties.NUM_NAME !== properties.NAME ? properties.NUM_NAME : "";
      }
      if (layerType === "cpac") {
        return properties.cpac_district ? `Planning District ${properties.planning_district || properties.PD_ID || properties.cpac_district}` : "Planning District";
      }
      if (layerType === "floridaHouse") {
        return properties.HSE_NAME || properties.DELEGATES || "";
      }
      if (layerType === "floridaSenate") {
        return properties.SEN_NAME || "";
      }
      if (layerType === "zipCode") {
        return [properties.USPS_CITY, properties.USPS_STATE].filter(Boolean).join(", ");
      }
      if (layerType === "congressional") {
        return properties.CDSESSN ? `${properties.CDSESSN}th Congress` : "";
      }
      if (layerType === "jsoDistrict") {
        return "Jacksonville Sheriff's Office";
      }
      if (layerType === "jsoSubsector") {
        return [properties.SECTOR ? `Sector ${properties.SECTOR}` : "", properties.DISTRICT ? `District ${properties.DISTRICT}` : ""].filter(Boolean).join(" / ");
      }
      return properties.MEMBER_NAM || "";
    }

    function getCityCouncilMemberUrl(properties) {
      const districtUrls = {
        1: "https://www.jacksonville.gov/city-council/city-council-members/d01",
        2: "https://www.jacksonville.gov/city-council/city-council-members/d02",
        3: "https://www.jacksonville.gov/city-council/city-council-members/d03",
        4: "https://www.jacksonville.gov/city-council/city-council-members/d04",
        5: "https://www.jacksonville.gov/city-council/city-council-members/d05",
        6: "https://www.jacksonville.gov/city-council/city-council-members/d06",
        7: "https://www.jacksonville.gov/city-council/city-council-members/d07",
        8: "https://www.jacksonville.gov/city-council/city-council-members/d08",
        9: "https://www.jacksonville.gov/city-council/city-council-members/d09",
        10: "https://www.jacksonville.gov/city-council/city-council-members/d10",
        11: "https://www.jacksonville.gov/city-council/city-council-members/d11",
        12: "https://www.jacksonville.gov/city-council/city-council-members/d12",
        13: "https://www.jacksonville.gov/city-council/city-council-members/d13",
        14: "https://www.jacksonville.gov/city-council/city-council-members/d14"
      };
      const atLargeUrls = {
        1: "https://www.jacksonville.gov/city-council/city-council-members/al1",
        2: "https://www.jacksonville.gov/city-council/city-council-members/al2",
        3: "https://www.jacksonville.gov/city-council/city-council-members/al3",
        4: "https://www.jacksonville.gov/city-council/city-council-members/al4",
        5: "https://www.jacksonville.gov/city-council/city-council-members/al5"
      };
      const district = Number.parseInt(properties.CC || properties.DISTRICT_N || properties.DISTRICT, 10);
      const atLarge = Number.parseInt(properties.CCAL, 10);

      return atLargeUrls[atLarge] || districtUrls[district] || "";
    }

    function getBoundaryTitleUrl(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "atLarge") {
        return getCityCouncilMemberUrl(properties);
      }
      if (layerType === "congressional") {
        return properties.ballotpedia_url || "";
      }
      if (layerType === "cpac") {
        return properties.cpac_url || "";
      }
      return "";
    }

    function createBoundaryPopup(feature, layerType) {
      const popup = document.createElement("div");
      const titleUrl = getBoundaryTitleUrl(feature, layerType);
      const title = titleUrl ? document.createElement("a") : document.createElement("strong");
      const subtitle = getBoundarySubtitle(feature, layerType);

      popup.className = "maps-district-popup";
      title.textContent = getBoundaryTitle(feature, layerType);
      if (titleUrl) {
        title.href = titleUrl;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      if (subtitle) {
        const line = document.createElement("span");
        line.textContent = subtitle;
        popup.appendChild(line);
      }

      return popup;
    }

    function createCouncilDistrictPopup(feature) {
      const properties = feature.properties || {};
      const district = properties.CC || properties.DISTRICT_N || properties.DISTRICT || "";
      const member = properties.MEMBER_NAM || "";
      const email = properties.E_MAIL || "";
      const phone = properties.PHONE || "";
      const popup = document.createElement("div");
      popup.className = "maps-district-popup";

      const memberUrl = getCityCouncilMemberUrl(properties);
      const title = memberUrl ? document.createElement("a") : document.createElement("strong");
      title.textContent = district ? `City Council District ${district}` : "City Council District";
      if (memberUrl) {
        title.href = memberUrl;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      if (member) {
        const memberLine = document.createElement("span");
        memberLine.textContent = member;
        popup.appendChild(memberLine);
      }

      if (phone) {
        const phoneLine = document.createElement("span");
        phoneLine.textContent = phone;
        popup.appendChild(phoneLine);
      }

      if (email) {
        const emailLink = document.createElement("a");
        emailLink.href = `mailto:${email}`;
        emailLink.textContent = email;
        popup.appendChild(emailLink);
      }

      return popup;
    }

    function addCouncilDistrictInteractivity(feature, layer, mode) {
      const district = (feature.properties || {}).CC || getDistrictNumber(feature);
      layer.options.boundaryMode = mode;
      layer.options.boundaryType = "district";
      layer.bindPopup(createCouncilDistrictPopup(feature));
      if (district) {
        layer.bindTooltip(`City Council District ${district}`, {
          sticky: true
        });
      }
      layer.on({
        mouseover: function () {
          layer.setStyle({
            fillOpacity: mode === "border" ? 0 : 0.28,
            weight: mode === "border" ? 1.75 : 1.25
          });
        },
        mouseout: function () {
          layer.setStyle(getCouncilDistrictStyle(feature, mode));
        },
        click: function (event) {
          handleBoundaryFeatureClick(event, getBoundaryLayer("district", mode), layer);
        }
      });
    }

    function addBoundaryInteractivity(feature, layer, mode, layerType) {
      layer.options.boundaryMode = mode;
      layer.options.boundaryType = layerType;
      layer.bindPopup(createBoundaryPopup(feature, layerType));
      layer.bindTooltip(getBoundaryTitle(feature, layerType), {
        sticky: true
      });
      layer.on({
        mouseover: function () {
          layer.setStyle({
            fillOpacity: mode === "border" ? 0 : 0.28,
            weight: mode === "border" ? 1.75 : 1.25
          });
        },
        mouseout: function () {
          layer.setStyle(getBoundaryStyle(feature, mode, layerType));
        },
        click: function (event) {
          handleBoundaryFeatureClick(event, getBoundaryLayer(layerType, mode), layer);
        }
      });
    }

    function normalizeHexColor(value, fallback) {
      const color = String(value || "").replace("#", "").trim();
      return /^[0-9a-fA-F]{6}$/.test(color) ? `#${color}` : fallback;
    }

    function getBusRouteStyle(feature) {
      const color = normalizeHexColor((feature.properties || {}).route_color, "#0f766e");
      return {
        color,
        opacity: 0.88,
        weight: 3
      };
    }

    function getBusStopStyle() {
      return {
        color: "#ffffff",
        fillColor: "#111827",
        fillOpacity: 0.9,
        opacity: 1,
        radius: 3,
        weight: 1
      };
    }

    function getPoliceStationStyle() {
      return {
        color: "#ffffff",
        fillColor: "#1d4ed8",
        fillOpacity: 0.95,
        opacity: 1,
        radius: 6,
        weight: 1.5
      };
    }

    function getNeighborhoodOrganizationStyle() {
      return {
        color: "#ffffff",
        fillColor: "#be123c",
        fillOpacity: 0.95,
        opacity: 1,
        radius: 5,
        weight: 1.5
      };
    }

    function createBusRoutePopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      const name = [properties.route_short_name, properties.route_long_name].filter(Boolean).join(" - ");

      popup.className = "maps-district-popup";
      title.textContent = name || `Route ${properties.route_id || ""}`.trim() || "JTA Bus Route";
      popup.appendChild(title);

      if (properties.shape_id) {
        const shapeLine = document.createElement("span");
        shapeLine.textContent = `Shape ${properties.shape_id}`;
        popup.appendChild(shapeLine);
      }

      return popup;
    }

    function createBusStopPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = properties.stop_name || "JTA Bus Stop";
      popup.appendChild(title);

      if (properties.stop_code) {
        const codeLine = document.createElement("span");
        codeLine.textContent = `Stop ${properties.stop_code}`;
        popup.appendChild(codeLine);
      }

      return popup;
    }

    function createPoliceStationPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      const directionsUrl = properties.directions_url || "";

      popup.className = "maps-district-popup";
      title.textContent = properties.name || "JSO Substation";
      popup.appendChild(title);

      [
        properties.neighborhoods,
        properties.commander ? `District Commander ${properties.commander}` : "",
        properties.address,
        properties.located && properties.located_label ? `${properties.located_label}: ${properties.located}` : properties.located,
        properties.hours ? `Hours: ${properties.hours}` : "",
        properties.phone ? `Phone: ${properties.phone}` : "",
        properties.fax ? `Fax: ${properties.fax}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      if (properties.email) {
        const emailLink = document.createElement("a");
        emailLink.href = `mailto:${properties.email}`;
        emailLink.textContent = properties.email;
        popup.appendChild(emailLink);
      }

      if (directionsUrl) {
        const directionsLink = document.createElement("a");
        directionsLink.href = directionsUrl;
        directionsLink.target = "_blank";
        directionsLink.rel = "noopener";
        directionsLink.textContent = "Directions";
        popup.appendChild(directionsLink);
      }

      return popup;
    }

    function createNeighborhoodOrganizationPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = properties.name || "Neighborhood Organization";
      popup.appendChild(title);

      [
        properties.type,
        properties.address,
        properties.cpac ? `CPAC: ${properties.cpac}` : "",
        properties.planning_district ? `Planning District ${properties.planning_district}` : "",
        properties.council_district ? `City Council District ${properties.council_district}` : "",
        properties.date_registered ? `Registered ${properties.date_registered}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      return popup;
    }

    function addBusRouteInteractivity(feature, layer) {
      const properties = feature.properties || {};
      const name = [properties.route_short_name, properties.route_long_name].filter(Boolean).join(" - ");
      layer.bindPopup(createBusRoutePopup(feature));
      if (name) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
      layer.on({
        mouseover: function () {
          layer.setStyle({
            opacity: 1,
            weight: 5
          });
        },
        mouseout: function () {
          layer.setStyle(getBusRouteStyle(feature));
        }
      });
    }

    function addBusStopInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createBusStopPopup(feature));
      if (properties.stop_name) {
        layer.bindTooltip(properties.stop_name, {
          sticky: true
        });
      }
    }

    function addPoliceStationInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createPoliceStationPopup(feature));
      layer.bindTooltip(properties.name || "JSO Substation", {
        sticky: true
      });
    }

    function addNeighborhoodOrganizationInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createNeighborhoodOrganizationPopup(feature));
      layer.bindTooltip(properties.name || "Neighborhood Organization", {
        sticky: true
      });
    }

    function getSchoolStyle(type) {
      const colors = {
        elementary: "#0891b2",
        middle: "#dc2626",
        high: "#16a34a",
        combination: "#ca8a04",
        magnet: "#9333ea",
        private: "#be123c",
        postSecondary: "#0f766e"
      };
      const fillColor = colors[type] || "#111827";
      return {
        color: "#ffffff",
        fillColor,
        fillOpacity: 0.95,
        opacity: 1,
        radius: 5,
        weight: 1.5
      };
    }

    function createFldoeSchoolLayer(type) {
      return L.geoJSON(null, {
        pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle(type)),
        onEachFeature: (feature, layer) => addFldoeSchoolInteractivity(feature, layer)
      });
    }

    function createFilteredFldoeSchoolLayer(type, filter) {
      return L.geoJSON(null, {
        filter,
        pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSchoolStyle(type)),
        onEachFeature: (feature, layer) => addFldoeSchoolInteractivity(feature, layer)
      });
    }

    function getPrivateSchoolGrades(feature) {
      const properties = feature.properties || {};
      const gradeLevels = properties.grade_levels || "";
      const gradeOrder = {
        PK: -1,
        K: 0,
        KG: 0
      };
      const tokens = gradeLevels.match(/PK|KG|K|\d{1,2}/g) || [];
      const grades = tokens
        .map((token) => Object.prototype.hasOwnProperty.call(gradeOrder, token) ? gradeOrder[token] : Number.parseInt(token, 10))
        .filter((grade) => Number.isFinite(grade));

      if (grades.length >= 2 && grades[0] <= grades[grades.length - 1]) {
        const range = [];
        for (let grade = grades[0]; grade <= grades[grades.length - 1]; grade += 1) {
          range.push(grade);
        }
        return range;
      }

      return grades;
    }

    function getPrivateSchoolCategory(feature) {
      const grades = getPrivateSchoolGrades(feature);
      const bands = new Set();

      if (grades.some((grade) => grade <= 5)) bands.add("elementary");
      if (grades.some((grade) => grade >= 6 && grade <= 8)) bands.add("middle");
      if (grades.some((grade) => grade >= 9)) bands.add("high");

      return bands.size === 1 ? Array.from(bands)[0] : "combination";
    }

    function createPrivateSchoolLayer(category) {
      return createFilteredFldoeSchoolLayer(category, (feature) => getPrivateSchoolCategory(feature) === category);
    }

    function getSchoolName(feature) {
      const properties = feature.properties || {};
      return properties.USER_Full_Name
        || properties.USER_Name
        || properties.Sch_Label
        || properties.USER_Short_Name
        || "School";
    }

    function appendSchoolPopupLine(popup, value) {
      if (!value) return;
      const line = document.createElement("span");
      line.textContent = value;
      popup.appendChild(line);
    }

    function createSchoolPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      const gradeLevel = properties.USER_School_Grade_Level || properties.USER_Grade_Level || "";
      const address = properties.USER_School_Address || properties.IN_SingleLine || properties.Match_addr || "";
      const phone = properties.USER_School_Phone_Number || "";

      popup.className = "maps-district-popup";
      title.textContent = getSchoolName(feature);
      popup.appendChild(title);

      appendSchoolPopupLine(popup, gradeLevel);
      appendSchoolPopupLine(popup, address);
      appendSchoolPopupLine(popup, phone);

      if (properties.USER_URL) {
        const link = document.createElement("a");
        link.href = properties.USER_URL;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "View school";
        popup.appendChild(link);
      }

      return popup;
    }

    function addSchoolInteractivity(feature, layer) {
      const name = getSchoolName(feature);
      layer.bindPopup(createSchoolPopup(feature));
      if (name) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
    }

    function getFldoeSchoolName(feature) {
      const properties = feature.properties || {};
      return properties.school_name || properties.school_name_short || "School";
    }

    function formatFldoeAddress(properties) {
      if (properties.address) return properties.address;
      if (properties.formatted_address) return properties.formatted_address;
      return [
        properties.physical_address,
        [properties.physical_city, properties.physical_state, properties.physical_zip].filter(Boolean).join(" ")
      ].filter(Boolean).join(", ");
    }

    function appendFldoePopupLine(popup, label, value) {
      if (value === undefined || value === null || value === "") return;
      const line = document.createElement("span");
      line.textContent = label ? `${label}: ${value}` : value;
      popup.appendChild(line);
    }

    function createFldoeSchoolPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = properties.report_card_url ? document.createElement("a") : document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = getFldoeSchoolName(feature);
      if (properties.report_card_url) {
        title.href = properties.report_card_url;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      appendFldoePopupLine(popup, "", properties.public_school_type || properties.category);
      appendFldoePopupLine(popup, "School type", properties.school_type);
      appendFldoePopupLine(popup, "Address", formatFldoeAddress(properties));
      appendFldoePopupLine(popup, "Phone", properties.phone_number);
      appendFldoePopupLine(popup, "Grade levels", properties.grade_levels);
      appendFldoePopupLine(popup, "Students", properties.total_students || properties.enrollment);
      appendFldoePopupLine(popup, "Teachers", properties.teacher_count);
      appendFldoePopupLine(popup, "Community Eligibility Provision", properties.cep_percentage ? `${properties.cep_percentage}%` : "");
      appendFldoePopupLine(popup, "Title I", properties.title1);
      appendFldoePopupLine(popup, "Magnet status", properties.magnet_status_label);
      appendFldoePopupLine(popup, "Magnet specialty", properties.magnet_specialty_label);
      appendFldoePopupLine(popup, "Alternative/ESE/DJJ", properties.alt_school_label);
      appendFldoePopupLine(popup, "Operating", properties.operating);
      appendFldoePopupLine(popup, "Operator class", properties.operator_class);
      appendFldoePopupLine(popup, "Owner", properties.owner);
      appendFldoePopupLine(popup, "Programs", properties.programs);
      appendFldoePopupLine(popup, "Director", properties.director);
      appendFldoePopupLine(popup, "Director email", properties.director_email);
      appendFldoePopupLine(popup, "Contact", properties.contact);
      appendFldoePopupLine(popup, "Contact email", properties.contact_email);
      appendFldoePopupLine(popup, "Religious", properties.religious);
      appendFldoePopupLine(popup, "Denomination", properties.denomination);
      appendFldoePopupLine(popup, "Non-profit", properties.non_profit);
      appendFldoePopupLine(popup, "Accreditation", properties.accreditation);
      appendFldoePopupLine(popup, "FES Educational Options", properties.fes_educational_options);
      appendFldoePopupLine(popup, "FTC", properties.ftc);
      appendFldoePopupLine(popup, "FES Unique Abilities", properties.fes_unique_abilities);
      appendFldoePopupLine(popup, "PEP", properties.pep);
      appendFldoePopupLine(popup, "Notes", properties.notes);
      appendFldoePopupLine(popup, "School number", properties.school_number);
      appendFldoePopupLine(popup, "Federal ID", properties.federal_id);

      if (properties.school_website) {
        const link = document.createElement("a");
        link.href = properties.school_website;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "View school website";
        popup.appendChild(link);
      }

      if (properties.google_map_url) {
        const link = document.createElement("a");
        link.href = properties.google_map_url;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "View on Google Maps";
        popup.appendChild(link);
      }

      return popup;
    }

    function addFldoeSchoolInteractivity(feature, layer) {
      const name = getFldoeSchoolName(feature);
      layer.bindPopup(createFldoeSchoolPopup(feature));
      if (name) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
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
      const marker = L.marker([place.lat, place.lng], Object.assign({
        title: place.name
      }, markerIcon ? { icon: markerIcon } : {}));

      marker.bindPopup(createPlacePopup(place)).addTo(targetLayer);
      return marker;
    }

    function renderPlaces() {
      const visiblePlaces = places
        .map(normalizePlace)
        .filter((place) => Number.isFinite(place.lat) && Number.isFinite(place.lng));
      const bounds = L.latLngBounds([]);

      activePlaceLayer.clearLayers();
      archivedPlaceLayer.clearLayers();

      visiblePlaces.forEach((place) => {
        addPlaceMarker(place);
        bounds.extend([place.lat, place.lng]);
      });

      if (visiblePlaces.length > 1) {
        map.fitBounds(bounds, { padding: [24, 24] });
      } else if (visiblePlaces.length === 1) {
        map.setView([visiblePlaces[0].lat, visiblePlaces[0].lng], visiblePlaces[0].zoom || 14);
      }
    }

    function loadCouncilDistricts() {
      fetch("/data/city-council-districts.geojson")
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Could not load council districts: ${response.status}`);
          }
          return response.json();
        })
        .then((districts) => {
          councilDistrictFillLayer.addData(districts);
          councilDistrictBorderLayer.addData(districts);
          orderMapLayers();
          if (!places.length && councilDistrictFillLayer.getLayers().length) {
            map.fitBounds(councilDistrictFillLayer.getBounds(), {
              padding: [24, 24]
            });
          }
        })
        .catch((error) => {
          console.warn(error);
        });
    }

    function loadBoundaryLayers(url, fillLayer, borderLayer, label) {
      fetch(url)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Could not load ${label}: ${response.status}`);
          }
          return response.json();
        })
        .then((geojson) => {
          fillLayer.addData(geojson);
          borderLayer.addData(geojson);
          orderMapLayers();
        })
        .catch((error) => {
          console.warn(error);
        });
    }

    function loadGeoJsonLayer(url, layer, label) {
      fetch(url)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Could not load ${label}: ${response.status}`);
          }
          return response.json();
        })
        .then((geojson) => {
          layer.addData(geojson);
          orderMapLayers();
        })
        .catch((error) => {
          console.warn(error);
        });
    }

    renderPlaces();
    loadCouncilDistricts();
    loadBoundaryLayers(
      "/data/city-council-at-large-districts.geojson",
      councilAtLargeFillLayer,
      councilAtLargeBorderLayer,
      "city council at-large districts"
    );
    loadBoundaryLayers(
      "/data/city-boundaries.geojson",
      cityFillLayer,
      cityBorderLayer,
      "city boundaries"
    );
    loadBoundaryLayers(
      "https://raw.githubusercontent.com/RayHollister/JacksonvilleNeighborhoods/main/neighborhoods.geojson",
      neighborhoodFillLayer,
      neighborhoodBorderLayer,
      "neighborhood boundaries"
    );
    loadGeoJsonLayer("/data/neighborhood-organizations.geojson", neighborhoodOrganizationsLayer, "neighborhood organizations");
    loadBoundaryLayers(
      "/data/cpac-planning-districts.geojson",
      cpacFillLayer,
      cpacBorderLayer,
      "CPAC planning districts"
    );
    loadBoundaryLayers(
      "/data/florida-house-districts.geojson",
      floridaHouseFillLayer,
      floridaHouseBorderLayer,
      "Florida House districts"
    );
    loadBoundaryLayers(
      "/data/florida-senate-districts.geojson",
      floridaSenateFillLayer,
      floridaSenateBorderLayer,
      "Florida Senate districts"
    );
    loadBoundaryLayers(
      "/data/zip-codes.geojson",
      zipCodeFillLayer,
      zipCodeBorderLayer,
      "ZIP Codes"
    );
    loadBoundaryLayers(
      "/data/congressional-districts.geojson",
      congressionalDistrictFillLayer,
      congressionalDistrictBorderLayer,
      "Congressional districts"
    );
    loadGeoJsonLayer("/data/jta-bus-routes.geojson", busRoutesLayer, "JTA bus routes");
    loadGeoJsonLayer("/data/jta-bus-stops.geojson", busStopsLayer, "JTA bus stops");
    loadBoundaryLayers(
      "/data/jso-districts.geojson",
      jsoDistrictFillLayer,
      jsoDistrictBorderLayer,
      "JSO districts"
    );
    loadBoundaryLayers(
      "/data/jso-subsectors.geojson",
      jsoSubsectionFillLayer,
      jsoSubsectionBorderLayer,
      "JSO subsections"
    );
    loadGeoJsonLayer("/data/jso-police-stations.geojson", jsoPoliceStationsLayer, "JSO police stations");
    loadGeoJsonLayer("/data/elementary-schools.geojson", elementarySchoolsLayer, "elementary schools");
    loadGeoJsonLayer("/data/middle-schools.geojson", middleSchoolsLayer, "middle schools");
    loadGeoJsonLayer("/data/high-schools.geojson", highSchoolsLayer, "high schools");
    loadGeoJsonLayer("/data/dedicated-magnet-schools.geojson", dedicatedMagnetSchoolsLayer, "dedicated magnet schools");
    loadGeoJsonLayer("/data/fldoe-duval-traditional-public-elementary-schools.geojson", fldoeTraditionalElementarySchoolsLayer, "FLDOE traditional public elementary schools");
    loadGeoJsonLayer("/data/fldoe-duval-traditional-public-middle-schools.geojson", fldoeTraditionalMiddleSchoolsLayer, "FLDOE traditional public middle schools");
    loadGeoJsonLayer("/data/fldoe-duval-traditional-public-high-schools.geojson", fldoeTraditionalHighSchoolsLayer, "FLDOE traditional public high schools");
    loadGeoJsonLayer("/data/fldoe-duval-traditional-public-combination-schools.geojson", fldoeTraditionalCombinationSchoolsLayer, "FLDOE traditional public combination schools");
    loadGeoJsonLayer("/data/fldoe-duval-traditional-public-magnet-schools.geojson", fldoeTraditionalMagnetSchoolsLayer, "FLDOE traditional public magnet schools");
    loadGeoJsonLayer("/data/fldoe-duval-charter-public-elementary-schools.geojson", fldoeCharterElementarySchoolsLayer, "FLDOE charter public elementary schools");
    loadGeoJsonLayer("/data/fldoe-duval-charter-public-middle-schools.geojson", fldoeCharterMiddleSchoolsLayer, "FLDOE charter public middle schools");
    loadGeoJsonLayer("/data/fldoe-duval-charter-public-high-schools.geojson", fldoeCharterHighSchoolsLayer, "FLDOE charter public high schools");
    loadGeoJsonLayer("/data/fldoe-duval-charter-public-combination-schools.geojson", fldoeCharterCombinationSchoolsLayer, "FLDOE charter public combination schools");
    loadGeoJsonLayer("/data/duval-private-schools.geojson", privateElementarySchoolsLayer, "Duval private elementary schools");
    loadGeoJsonLayer("/data/duval-private-schools.geojson", privateMiddleSchoolsLayer, "Duval private middle schools");
    loadGeoJsonLayer("/data/duval-private-schools.geojson", privateHighSchoolsLayer, "Duval private high schools");
    loadGeoJsonLayer("/data/duval-private-schools.geojson", privateCombinationSchoolsLayer, "Duval private combination schools");
    loadGeoJsonLayer("/data/duval-post-secondary-schools.geojson", postSecondarySchoolsLayer, "Duval post-secondary schools");

    addLocateControl();
    L.control.fullscreen({
      position: "topleft"
    }).addTo(map);
    L.Control.zoomHome().addTo(map);
    addDistrictLayerControl();
    addBaseMapControl();
    
    setBaseMap("positron", { quiet: true });

    new MutationObserver(refreshActiveBaseMap).observe(document.body, {
      attributes: true,
      attributeFilter: ["class"]
    });

    if (window.matchMedia) {
      const darkModeQuery = window.matchMedia("(prefers-color-scheme: dark)");
      if (darkModeQuery.addEventListener) {
        darkModeQuery.addEventListener("change", refreshActiveBaseMap);
      } else if (darkModeQuery.addListener) {
        darkModeQuery.addListener(refreshActiveBaseMap);
      }
    }
  })();
</script>
