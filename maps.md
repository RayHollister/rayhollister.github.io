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
    border: 1px solid #d0d7de;
    box-shadow: 0 2px 8px rgba(27, 31, 36, 0.15);
    overflow: hidden;
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

    .maps-control-panel__body {
      max-height: min(45vh, 22rem);
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
      fullscreenControl: true,
      fullscreenControlOptions: {
        position: "topleft"
      }
    }).setView([30.3322, -81.6557], 11);

    L.Control.zoomHome().addTo(map);

    const openFreeMapStyles = {
      positron: "https://tiles.openfreemap.org/styles/positron"
    };
    const openMapTilesSource = "https://tiles.openfreemap.org/planet";
    const openFreeMapGlyphs = "https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf";
    const baseMapStyles = {
      positron: {
        label: "Positron",
        getStyle: () => openFreeMapStyles.positron
      },
      osmBright: {
        label: "OSM Bright",
        getStyle: () => "https://raw.githubusercontent.com/openmaptiles/osm-bright-gl-style/master/style.json",
        useOpenFreeMapSource: true
      },
      darkMatter: {
        label: "Dark Matter",
        getStyle: () => "https://raw.githubusercontent.com/openmaptiles/dark-matter-gl-style/master/style.json",
        useOpenFreeMapSource: true
      },
      basic: {
        label: "Basic",
        getStyle: () => "https://raw.githubusercontent.com/openmaptiles/maptiler-basic-gl-style/master/style.json",
        useOpenFreeMapSource: true
      }
    };
    let activeBaseMapKey = "positron";
    let baseMapControlElement;
    let baseMapLayer;
    let baseMapRequestId = 0;

    async function getBaseMapStyle(config) {
      const style = config.getStyle();
      if (!config.useOpenFreeMapSource) {
        return style;
      }

      const response = await fetch(style);
      if (!response.ok) {
        throw new Error(`Could not load ${config.label} style.`);
      }
      const styleJson = await response.json();
      styleJson.sources = styleJson.sources || {};
      styleJson.sources.openmaptiles = {
        type: "vector",
        url: openMapTilesSource
      };
      styleJson.glyphs = openFreeMapGlyphs;
      return styleJson;
    }

    async function setBaseMap(baseMapKey, options) {
      const config = baseMapStyles[baseMapKey];
      const settings = options || {};
      const requestId = ++baseMapRequestId;
      if (!config) return false;
      if (!window.maplibregl || /HeadlessChrome/.test(window.navigator.userAgent) || (maplibregl.supported && !maplibregl.supported({ failIfMajorPerformanceCaveat: true }))) {
        return false;
      }
      let nextStyle;
      try {
        nextStyle = await getBaseMapStyle(config);
      } catch (error) {
        if (!settings.quiet) {
          window.alert(error.message || `Could not load ${config.label} basemap.`);
        }
        return false;
      }
      if (requestId !== baseMapRequestId) {
        return false;
      }
      if (baseMapLayer) {
        map.removeLayer(baseMapLayer);
      }
      baseMapLayer = L.maplibreGL({
        style: nextStyle
      }).addTo(map);
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

    function setupCollapsibleMapControl(container, label, body) {
      const toggle = document.createElement("button");
      const isMobile = window.matchMedia && window.matchMedia("(max-width: 760px)").matches;

      container.classList.add("maps-control-panel");
      body.classList.add("maps-control-panel__body");
      toggle.type = "button";
      toggle.className = "maps-control-panel__toggle";
      toggle.textContent = label;
      toggle.setAttribute("aria-label", `${label} control`);
      container.insertBefore(toggle, body);

      function setOpen(open) {
        container.classList.toggle("is-open", open);
        toggle.setAttribute("aria-expanded", String(open));
      }

      toggle.addEventListener("click", function () {
        setOpen(!container.classList.contains("is-open"));
      });
      setOpen(!isMobile);
    }

    function addBaseMapControl() {
      const BaseMapControl = L.Control.extend({
        options: {
          position: "topright"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "maps-basemap-control leaflet-control");
          const body = document.createElement("div");
          container.appendChild(body);
          Object.entries(baseMapStyles).forEach(([key, config]) => {
            const button = document.createElement("button");
            button.type = "button";
            button.dataset.baseMap = key;
            button.textContent = config.label;
            button.title = `Use ${config.label} basemap`;
            button.addEventListener("click", () => {
              setBaseMap(key);
            });
            body.appendChild(button);
          });
          setupCollapsibleMapControl(container, "Basemap", body);
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
    const busRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addBusRouteInteractivity(feature, layer)
    });
    const busStopsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getBusStopStyle()),
      onEachFeature: (feature, layer) => addBusStopInteractivity(feature, layer)
    });
    const boundaryLayerControls = [];

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
        neighborhoodBorderLayer
      ].forEach((layer) => moveLayerGroup(layer, "bringToBack"));

      moveLayerGroup(busRoutesLayer, "bringToFront");
      moveLayerGroup(busStopsLayer, "bringToFront");
    }

    function syncDistrictLayerInputs() {
      boundaryLayerControls.forEach((control) => {
        if (control.input) {
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
      const row = document.createElement("span");
      const input = document.createElement("input");
      const text = document.createElement("span");
      const settings = options || {};
      const control = { input, layer, group: settings.group || "" };
      let allowMultipleOnNextChange = false;

      input.type = "checkbox";
      input.className = "leaflet-control-layers-selector";
      input.addEventListener("click", function (event) {
        allowMultipleOnNextChange = event.shiftKey;
      });
      input.addEventListener("change", function (event) {
        setBoundaryLayer(control, input.checked, allowMultipleOnNextChange);
        allowMultipleOnNextChange = false;
      });

      text.textContent = ` ${label}`;
      row.appendChild(input);
      row.appendChild(text);
      labelElement.appendChild(row);
      boundaryLayerControls.push(control);
      return { input, labelElement };
    }

    function addDistrictLayerControl() {
      const DistrictLayerControl = L.Control.extend({
        options: {
          position: "topright"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "leaflet-control-layers leaflet-control-layers-expanded leaflet-control maps-layers-control");
          const list = L.DomUtil.create("section", "leaflet-control-layers-list", container);
          const overlays = L.DomUtil.create("div", "leaflet-control-layers-overlays", list);
          [
            createBoundaryLayerInput("City Council District Overlays", councilDistrictFillLayer, { group: "boundaries" }),
            createBoundaryLayerInput("City Council District Borders", councilDistrictBorderLayer, { group: "boundaries" }),
            createBoundaryLayerInput("City Council District At Large Overlays", councilAtLargeFillLayer, { group: "boundaries" }),
            createBoundaryLayerInput("City Council District At Large Borders", councilAtLargeBorderLayer, { group: "boundaries" }),
            createBoundaryLayerInput("Cities Overlays", cityFillLayer, { group: "boundaries" }),
            createBoundaryLayerInput("Cities Borders", cityBorderLayer, { group: "boundaries" }),
            createBoundaryLayerInput("Neighborhood Overlays", neighborhoodFillLayer, { group: "boundaries" }),
            createBoundaryLayerInput("Neighborhood Borders", neighborhoodBorderLayer, { group: "boundaries" }),
            createBoundaryLayerInput("JTA Bus Routes", busRoutesLayer),
            createBoundaryLayerInput("JTA Bus Stops", busStopsLayer)
          ].forEach((control) => {
            overlays.appendChild(control.labelElement);
          });
          setupCollapsibleMapControl(container, "Layers", list);
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
        return getStringColorNumber(properties.NAME || properties.NUM_NAME || "Neighborhood");
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
        return properties.NAME || properties.NUM_NAME || "Neighborhood";
      }
      const district = properties.CC || properties.DISTRICT_N || properties.DISTRICT || "";
      return district ? `Council District ${district}` : "Council District";
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
      return properties.MEMBER_NAM || "";
    }

    function createBoundaryPopup(feature, layerType) {
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      const subtitle = getBoundarySubtitle(feature, layerType);

      popup.className = "maps-district-popup";
      title.textContent = getBoundaryTitle(feature, layerType);
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

      const title = document.createElement("strong");
      title.textContent = district ? `Council District ${district}` : "Council District";
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
        layer.bindTooltip(`District ${district}`, {
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
    loadGeoJsonLayer("/data/jta-bus-routes.geojson", busRoutesLayer, "JTA bus routes");
    loadGeoJsonLayer("/data/jta-bus-stops.geojson", busStopsLayer, "JTA bus stops");

    addDistrictLayerControl();
    addBaseMapControl();
    addLocateControl();
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
