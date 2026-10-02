---
layout: page
title: Maps
permalink: /maps/
description: "Explore Jacksonville, Florida neighborhood organizations, CPAC districts, schools, transit, public safety, council districts, and local boundaries on an interactive map."
image: /media/2026/09/maps-featured.png
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

  .maps-district-popup .maps-route-pdf-link {
    margin-top: 0.25rem;
  }

  .maps-district-popup strong {
    margin-top: 0.5rem;
  }

  .maps-district-popup strong:first-child {
    margin-top: 0;
  }

  .maps-district-popup img {
    border-radius: 4px;
    display: block;
    height: 72px;
    margin-bottom: 0.4rem;
    object-fit: cover;
    width: 72px;
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

  .maps-control-panel__header {
    align-items: center;
    display: flex;
    justify-content: space-between;
  }

  .maps-layers-control.is-open .maps-control-panel__header {
    border-bottom: 1px solid #d0d7de;
    gap: 0.35rem;
    justify-content: flex-start;
    padding-right: 0.45rem;
  }

  .maps-layers-control:not(.is-open) .maps-control-panel__header {
    display: block;
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
    background: #424242;
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
    border-top: 0;
    margin-top: 0;
    padding-top: 0;
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

  .maps-layer-geometry-icon {
    align-items: center;
    color: #57606a;
    display: inline-flex;
    flex: 0 0 auto;
    height: 14px;
    justify-content: center;
    width: 14px;
  }

  .maps-layer-geometry-icon svg {
    display: block;
    fill: currentColor;
    height: 14px;
    width: 14px;
  }

  .maps-layer-group-row label {
    white-space: nowrap;
  }

  .maps-route-filter {
    border: 1px solid #d0d7de;
    border-radius: 4px;
    margin-top: 0.35rem;
  }

  .maps-route-filter summary {
    align-items: center;
    cursor: pointer;
    display: flex;
    font-weight: 700;
    gap: 0.35rem;
    justify-content: space-between;
    padding: 0.35rem 0.45rem;
  }

  .maps-route-filter__toggle {
    background: #424242;
    border: 0;
    color: #ffffff;
    cursor: pointer;
    font-size: 0.68rem;
    font-weight: 700;
    height: 1.25rem;
    line-height: 1;
    padding: 0 0.35rem;
  }

  .maps-route-filter__toggle:disabled {
    cursor: default;
    opacity: 0.55;
  }

  .maps-route-filter__list {
    border-top: 1px solid #d0d7de;
    display: grid;
    gap: 0.2rem;
    max-height: 14rem;
    overflow: auto;
    padding: 0.35rem 0.45rem;
  }

  .maps-route-filter__list:empty {
    display: none;
  }

  .maps-route-filter__row {
    align-items: center;
    display: flex;
    gap: 0.35rem;
    min-width: 0;
  }

  .maps-route-filter__swatch {
    border: 1px solid rgba(0, 0, 0, 0.28);
    display: inline-block;
    flex: 0 0 auto;
    height: 0.65rem;
    width: 0.65rem;
    margin: 0 0.25rem; 
  }

  .maps-layers-control {
    position: relative;
  }

  .maps-layers-control .maps-layer-opacity-control {
    align-items: center;
    display: flex;
    flex: 1 1 7rem;
    height: 30px;
    justify-content: center;
    min-width: 5rem;
    position: relative;
  }

  .maps-layers-control .maps-layer-opacity-control::after {
    border: 1px solid #424242;
    box-sizing: border-box;
    content: "";
    height: 18px;
    left: 0;
    pointer-events: none;
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
  }

  .maps-layers-control:not(.is-open) .maps-layer-header-actions {
    display: none;
  }

  .maps-layer-header-actions {
    align-items: center;
    display: flex;
    flex: 1 1 auto;
    gap: 0.25rem;
  }

  .maps-layer-header-actions button {
    align-items: center;
    background: #fff;
    border: 1px solid #424242;
    box-sizing: border-box;
    color: #424242;
    cursor: pointer;
    display: inline-flex;
    flex: 0 0 auto;
    font-size: 11px;
    height: 18px;
    line-height: 1;
    padding: 0 0.45rem;
  }

  .maps-layer-header-actions button[aria-pressed="true"] {
    background: #424242;
    border-color: #424242;
    color: #fff;
  }

  .maps-pinned-card-panel button {
    background: #fff;
    border: 1px solid #d0d7de;
    border-radius: 4px;
    color: #24292f;
    cursor: pointer;
    font: inherit;
    padding: 0.25rem 0.45rem;
  }

  .maps-pinned-card-panel button:disabled {
    color: #8c959f;
    cursor: not-allowed;
  }

  .maps-pinned-card-panel {
    background: #fff;
    border: 1px solid #d0d7de;
    box-shadow: 0 2px 8px rgb(27 31 36 / 12%);
    display: none;
    max-height: calc(100vh - 7rem);
    max-height: calc(100dvh - 7rem);
    overflow: hidden;
    width: min(22rem, calc(100vw - 5rem));
  }

  .maps-pinned-card-panel.is-open {
    display: flex;
    flex-direction: column;
  }

  .maps-pinned-card-panel__header {
    align-items: center;
    border-bottom: 1px solid #d0d7de;
    display: flex;
    gap: 0.5rem;
    justify-content: space-between;
    padding: 0.45rem 0.6rem;
  }

  .maps-pinned-card-panel__title {
    font-weight: 700;
  }

  .maps-pinned-card-panel__body {
    display: grid;
    gap: 0.5rem;
    overflow: auto;
    padding: 0.6rem;
  }

  .maps-pinned-card {
    border: 1px solid #d0d7de;
    border-radius: 6px;
    display: grid;
    gap: 0.35rem;
    padding: 0.55rem;
  }

  .maps-pinned-card__header {
    align-items: start;
    display: flex;
    gap: 0.5rem;
    justify-content: space-between;
  }

  .maps-pinned-card__header strong {
    margin-top: 0;
  }

  .maps-pinned-card__close {
    flex: 0 0 auto;
    line-height: 1;
    padding: 0.15rem 0.35rem;
  }

  .maps-layer-opacity-control input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    --maps-layer-opacity-alpha: 0.25;
    --maps-layer-opacity-fill-color: rgb(208 208 208);
    --maps-layer-opacity-percent: 25%;
    --maps-layer-thumb-border-color: rgb(64 64 64);
    background: linear-gradient(
      to right,
      var(--maps-layer-opacity-fill-color) 0 var(--maps-layer-opacity-percent),
      #fff var(--maps-layer-opacity-percent) 100%
    );
    border: 0;
    box-sizing: border-box;
    cursor: pointer;
    display: block;
    height: 18px;
    margin: 0;
    position: relative;
    width: 100%;
    z-index: 1;
  }

  .maps-layer-opacity-control input[type="range"]::-webkit-slider-runnable-track {
    background: transparent;
    border: 0;
    border-radius: 0;
    box-sizing: border-box;
    height: 18px;
    width: 100%;
  }

  .maps-layer-opacity-control input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    background: var(--maps-layer-opacity-fill-color);
    border: 1px solid var(--maps-layer-thumb-border-color);
    border-radius: 0;
    box-sizing: border-box;
    height: 18px;
    margin-top: 0;
    width: 18px;
  }

  .maps-layer-opacity-control input[type="range"]::-moz-range-track {
    background: transparent;
    border: 0;
    border-radius: 0;
    box-sizing: border-box;
    height: 18px;
    width: 100%;
  }

  .maps-layer-opacity-control input[type="range"]::-moz-range-progress {
    background: var(--maps-layer-opacity-fill-color);
    border: 0;
    height: 18px;
  }

  .maps-layer-opacity-control input[type="range"]::-moz-range-thumb {
    background: var(--maps-layer-opacity-fill-color);
    border: 1px solid var(--maps-layer-thumb-border-color);
    border-radius: 0;
    box-sizing: border-box;
    height: 18px;
    width: 18px;
  }

  .maps-layer-opacity-control input[type="range"]:focus-visible {
    outline: 2px solid #0969da;
    outline-offset: 2px;
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

  #ray-map,
  #ray-map * {
    -webkit-tap-highlight-color: transparent;
  }

  .maps-context-menu {
    background: #fff;
    border: 1px solid #424242;
    box-shadow: 0 2px 8px rgb(27 31 36 / 18%);
    display: none;
    min-width: 11rem;
    padding: 0;
    position: absolute;
    z-index: 1200;
  }

  .maps-context-menu.is-open {
    display: block;
  }

  .maps-context-menu button {
    background: #fff;
    border: 0;
    border-bottom: 1px solid #d0d7de;
    box-sizing: border-box;
    color: #24292f;
    cursor: pointer;
    display: block;
    font: inherit;
    font-size: 12px;
    line-height: 1.2;
    padding: 0.45rem 0.55rem;
    text-align: left;
    width: 100%;
  }

  .maps-context-menu button:last-child {
    border-bottom: 0;
  }

  .maps-context-menu button:hover,
  .maps-context-menu button:focus-visible {
    background: #f6f8fa;
    outline: 0;
  }

  #ray-map .maplibregl-map,
  #ray-map .maplibregl-canvas-container,
  #ray-map .maplibregl-canvas,
  #ray-map .maplibregl-control-container {
    pointer-events: none;
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

    .maps-pinned-card-panel {
      display: none !important;
    }
  }
</style>

<section class="maps-page">
  <div class="maps-shell">
    <div id="ray-map" aria-label="Interactive map"></div>
  </div>
</section>

<script src="/leaflet/leaflet.js"></script>
<script src="/leaflet/smoothwheelzoom/SmoothWheelZoom.js"></script>
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
      scrollWheelZoom: false,
      smoothWheelZoom: true,
      smoothSensitivity: 1,
      zoomSnap: 0,
      fullscreenControl: false
    }).setView([30.3322, -81.6557], 11);

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
    let zoomHomeControl;
    const supportsPointerHover = window.matchMedia
      ? window.matchMedia("(hover: hover) and (pointer: fine)").matches
      : true;

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
      const headerAction = settings.headerAction || null;
      let header = null;
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
      if (headerAction) {
        header = document.createElement("div");
        header.className = "maps-control-panel__header";
        header.appendChild(toggle);
        header.appendChild(headerAction);
        container.insertBefore(header, body);
      } else {
        container.insertBefore(toggle, body);
      }

      function fitOpenPanelToViewport() {
        if (!container.classList.contains("is-open")) return;
        const containerTop = container.getBoundingClientRect().top;
        const availableHeight = Math.max(160, window.innerHeight - containerTop - viewportPadding);
        const headerHeight = header ? header.offsetHeight : toggle.offsetHeight;
        const bodyHeight = Math.max(120, availableHeight - headerHeight);
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
      document.addEventListener("click", function (event) {
        if (container.classList.contains("is-open") && !container.contains(event.target)) {
          setOpen(false);
        }
      });
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

    map.attributionControl.addAttribution(
      '<a href="https://openfreemap.org/" target="_blank" rel="noopener">OpenFreeMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="https://github.com/RayHollister/JacksonvilleNeighborhoods" target="_blank" rel="noopener">Jacksonville Neighborhoods</a>'
    );
    map.attributionControl.addAttribution(
      '<a href="/maps/references/">Disclaimer and Data Sources</a>'
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
    const schoolBoardDistrictFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "schoolBoard"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "schoolBoard")
    });
    const schoolBoardDistrictBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "schoolBoard"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "schoolBoard")
    });
    const cityFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "city"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "city")
    });
    const cityBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "city"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "city")
    });
    const countyFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "county"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "county")
    });
    const countyBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "county"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "county")
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
    const healthZoneFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "healthZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "healthZone")
    });
    const healthZoneBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "healthZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "healthZone")
    });
    const healthZoneByZipCodeLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "healthZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "healthZone")
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
    const countablePointLayers = [];
    const queryLayerControls = new Map();
    const queryLayerSlugsByLayer = new Map();
    const explicitQueryLayerSlugs = new Set();
    const defaultGovernmentOverlayOpacity = 0.25;
    let governmentLayerMode = "fill";
    let governmentOverlayOpacity = defaultGovernmentOverlayOpacity;
    let governmentLayerOpacityInput;
    let governmentLayerOpacityLabel;
    const busRouteBoundaryToleranceMeters = 100;
    let mapInteractionMode = "browse";
    let focusToggleButton;
    let focusedBoundary;
    const focusLayerStates = new Map();
    let compareModeEnabled = false;
    let compareToggleButton;
    let pinnedCardPanel;
    let pinnedCardBody;
    let mapContextMenuElement;
    const pinnedBoundaryCards = [];
    let pendingMapDataLoads = 0;
    let initialVisibleLayerFitComplete = false;
    let initialVisibleLayerFitTimeout;
    const busRouteLayersByRouteId = new Map();
    const busRouteMetadataByRouteId = new Map();
    const selectedBusRouteIds = new Set();
    const busRouteFilterInputs = new Map();
    let focusedBusRouteSelectionSnapshot;
    let busRouteFilterElement;
    let busRouteFilterListElement;
    let busRouteFilterSummaryElement;
    let busRouteSelectionToggleButton;

    function moveLayerGroup(layer, direction) {
      if (!map.hasLayer(layer) || !layer.eachLayer) return;
      layer.eachLayer((childLayer) => {
        if (childLayer[direction]) {
          childLayer[direction]();
        }
      });
    }

    function orderMapLayers() {
      const polygonLayers = [
        councilDistrictFillLayer,
        councilDistrictBorderLayer,
        councilAtLargeFillLayer,
        councilAtLargeBorderLayer,
        schoolBoardDistrictFillLayer,
        schoolBoardDistrictBorderLayer,
        cityFillLayer,
        cityBorderLayer,
        countyFillLayer,
        countyBorderLayer,
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
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer
      ];
      const lineLayers = [
        busRoutesLayer
      ];
      const pointLayers = [
        activePlaceLayer,
        archivedPlaceLayer,
        jsoPoliceStationsLayer,
        neighborhoodOrganizationsLayer,
        busStopsLayer,
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
      ];

      polygonLayers.forEach((layer) => moveLayerGroup(layer, "bringToBack"));
      lineLayers.forEach((layer) => moveLayerGroup(layer, "bringToFront"));
      pointLayers.forEach((layer) => moveLayerGroup(layer, "bringToFront"));
      moveLayerGroup(busStopsLayer, "bringToFront");
    }

    function getVisibleOverlayLayers() {
      return [
        councilDistrictFillLayer,
        councilDistrictBorderLayer,
        councilAtLargeFillLayer,
        councilAtLargeBorderLayer,
        schoolBoardDistrictFillLayer,
        schoolBoardDistrictBorderLayer,
        cityFillLayer,
        cityBorderLayer,
        countyFillLayer,
        countyBorderLayer,
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
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer,
        neighborhoodOrganizationsLayer,
        jsoPoliceStationsLayer,
        busRoutesLayer,
        busStopsLayer,
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
        postSecondarySchoolsLayer,
        activePlaceLayer,
        archivedPlaceLayer
      ].filter((layer) => map.hasLayer(layer));
    }

    function extendBoundsWithLayer(bounds, layer) {
      if (!layer) return;
      if (layer.getBounds) {
        try {
          const layerBounds = layer.getBounds();
          if (layerBounds && layerBounds.isValid && layerBounds.isValid()) {
            bounds.extend(layerBounds);
            return;
          }
        } catch (error) {
          // Empty layer groups can throw while data is still loading.
        }
      }
      if (layer.getLatLng) {
        bounds.extend(layer.getLatLng());
      }
    }

    function fitVisibleMapLayersOnLoad() {
      if (initialVisibleLayerFitComplete || pendingMapDataLoads > 0) return;
      const bounds = L.latLngBounds([]);
      getVisibleOverlayLayers().forEach((layer) => extendBoundsWithLayer(bounds, layer));
      if (!bounds.isValid()) return;
      initialVisibleLayerFitComplete = true;
      map.fitBounds(bounds, { padding: [24, 24] });
    }

    function updateZoomHomeDefaultBounds() {
      if (!zoomHomeControl) return;
      const bounds = L.latLngBounds([]);
      extendBoundsWithLayer(bounds, councilDistrictFillLayer);
      if (activePlaceLayer.getLayers && activePlaceLayer.getLayers().length) {
        extendBoundsWithLayer(bounds, activePlaceLayer);
      }
      if (!bounds.isValid()) return;
      zoomHomeControl.setHomeCoordinates(bounds.getCenter());
      zoomHomeControl.setHomeZoom(map.getBoundsZoom(bounds, false, [24, 24]));
    }

    function scheduleInitialVisibleLayerFit() {
      if (initialVisibleLayerFitComplete) return;
      window.clearTimeout(initialVisibleLayerFitTimeout);
      initialVisibleLayerFitTimeout = window.setTimeout(fitVisibleMapLayersOnLoad, 100);
    }

    function beginMapDataLoad() {
      pendingMapDataLoads += 1;
    }

    function finishMapDataLoad() {
      pendingMapDataLoads = Math.max(0, pendingMapDataLoads - 1);
      scheduleInitialVisibleLayerFit();
    }

    function syncDistrictLayerInputs() {
      boundaryLayerControls.forEach((control) => {
        if (control.syncInput) {
          control.syncInput();
        } else if (control.input) {
          control.input.checked = map.hasLayer(control.layer);
        }
      });
      updateBusRouteFilterVisibility();
    }

    function getBoundaryFeatureStyle(feature, mode, layerType) {
      return layerType === "district"
        ? getCouncilDistrictStyle(feature, mode)
        : getBoundaryStyle(feature, mode, layerType);
    }

    function getOverlayFillOpacity(multiplier) {
      return Math.max(0, Math.min(1, governmentOverlayOpacity * (multiplier || 1)));
    }

    function restoreBoundaryLayerFeatures(layerGroup) {
      if (!layerGroup.eachLayer) return;
      layerGroup.eachLayer((featureLayer) => {
        const style = getLayerBoundaryStyle(featureLayer);
        if (featureLayer.setStyle && style) {
          featureLayer.setStyle(style);
        }
        if (featureLayer._path) {
          featureLayer._path.style.pointerEvents = "";
        }
      });
    }

    function getLayerBoundaryStyle(layer) {
      const options = layer && layer.options ? layer.options : {};
      if (!layer || !layer.feature || !options.boundaryMode || !options.boundaryType) return undefined;
      return getBoundaryFeatureStyle(layer.feature, options.boundaryMode, options.boundaryType);
    }

    function rememberFocusLayerState(layer) {
      if (!layer || focusLayerStates.has(layer._leaflet_id)) return;
      focusLayerStates.set(layer._leaflet_id, {
        layer,
        opacity: layer.options && layer.options.opacity,
        fillOpacity: layer.options && layer.options.fillOpacity,
        interactive: layer.options && layer.options.interactive,
        pointerEvents: layer._path ? layer._path.style.pointerEvents : "",
        parent: getLayerParent(layer)
      });
    }

    function getLayerParent(targetLayer) {
      let parent;
      [
        councilDistrictFillLayer,
        councilDistrictBorderLayer,
        councilAtLargeFillLayer,
        councilAtLargeBorderLayer,
        schoolBoardDistrictFillLayer,
        schoolBoardDistrictBorderLayer,
        cityFillLayer,
        cityBorderLayer,
        countyFillLayer,
        countyBorderLayer,
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
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer,
        neighborhoodOrganizationsLayer,
        jsoPoliceStationsLayer,
        busStopsLayer,
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
      ].some((layerGroup) => {
        if (!layerGroup.hasLayer || !layerGroup.hasLayer(targetLayer)) return false;
        parent = layerGroup;
        return true;
      });
      return parent;
    }

    function restoreAllBoundaryFillLayerStyles() {
      [
        councilDistrictFillLayer,
        councilAtLargeFillLayer,
        schoolBoardDistrictFillLayer,
        cityFillLayer,
        countyFillLayer,
        neighborhoodFillLayer,
        cpacFillLayer,
        floridaHouseFillLayer,
        floridaSenateFillLayer,
        zipCodeFillLayer,
        congressionalDistrictFillLayer,
        healthZoneFillLayer,
        healthZoneByZipCodeLayer,
        jsoDistrictFillLayer,
        jsoSubsectionFillLayer
      ].forEach(restoreBoundaryLayerFeatures);
    }

    function restoreFocusLayerStates() {
      focusLayerStates.forEach((state) => {
        const layer = state.layer;
        if (!layer) return;
        const boundaryStyle = getLayerBoundaryStyle(layer);
        if (layer.setStyle && boundaryStyle) {
          layer.setStyle(boundaryStyle);
        } else if (state.parent && state.parent.resetStyle && layer.feature) {
          state.parent.resetStyle(layer);
        } else if (layer.setStyle) {
          layer.setStyle({
            opacity: state.opacity === undefined ? 1 : state.opacity,
            fillOpacity: state.fillOpacity === undefined ? 0.9 : state.fillOpacity
          });
        } else if (layer.setOpacity) {
          layer.setOpacity(state.opacity === undefined ? 1 : state.opacity);
        }
        if (layer.options) {
          layer.options.interactive = state.interactive;
        }
        if (layer._path) {
          layer._path.style.pointerEvents = state.pointerEvents || "";
        }
      });
      focusLayerStates.clear();
    }

    function setLayerFocusVisibility(layer, visible) {
      rememberFocusLayerState(layer);
      if (layer.setStyle) {
        const boundaryStyle = getLayerBoundaryStyle(layer);
        if (visible && boundaryStyle) {
          layer.setStyle(boundaryStyle);
        } else {
          layer.setStyle({
            opacity: visible ? (layer.options.opacity === undefined ? 1 : layer.options.opacity) : 0,
            fillOpacity: visible ? (layer.options.fillOpacity === undefined ? 0.9 : layer.options.fillOpacity) : 0
          });
        }
      } else if (layer.setOpacity) {
        layer.setOpacity(visible ? 1 : 0);
      }
      if (layer.options) {
        layer.options.interactive = visible;
      }
      if (layer._path) {
        layer._path.style.pointerEvents = visible ? "" : "none";
      }
    }

    function setFocusedBoundaryStyle(layer) {
      if (!layer || !layer.setStyle) return;
      layer.setStyle({
        fillOpacity: layer.options.boundaryMode === "border" ? 0 : getOverlayFillOpacity(1.25),
        opacity: 1,
        weight: layer.options.boundaryMode === "border" ? 2.25 : 1.8
      });
    }

    function getFocusGeometryFeature(feature, layerType) {
      return getPointCountFeature(feature, layerType);
    }

    function doesFeatureMatchFocus(feature, focus) {
      const properties = feature.properties || {};
      const focusProperties = (focus.feature.properties || {});
      if (focus.layerType === "healthZone") {
        return properties.health_zone === focusProperties.health_zone;
      }
      return feature === focus.feature;
    }

    function getFocusSourceLayer(layerType, mode) {
      if (layerType === "healthZone") {
        return getActiveHealthZoneLayer() || getBoundaryLayer(layerType, mode);
      }
      return getBoundaryLayer(layerType, mode);
    }

    function applyFocusToBoundaryLayer(sourceLayer, focus) {
      if (!sourceLayer || !sourceLayer.eachLayer) return;
      sourceLayer.eachLayer((layer) => {
        if (!layer.feature || !layer.setStyle) return;
        const isFocused = doesFeatureMatchFocus(layer.feature, focus);
        setLayerFocusVisibility(layer, isFocused);
        if (isFocused) {
          setFocusedBoundaryStyle(layer);
        }
      });
    }

    function applyFocusToPointLayers(focusFeature) {
      const geometry = focusFeature.geometry || {};
      countablePointLayers.forEach((pointLayer) => {
        if (!map.hasLayer(pointLayer.layer) || !pointLayer.layer.eachLayer || !geometry.coordinates) return;
        pointLayer.layer.eachLayer((layer) => {
          if (!layer.getLatLng) return;
          const latLng = layer.getLatLng();
          const isInside = isPointInFeatureGeometry([latLng.lng, latLng.lat], geometry);
          setLayerFocusVisibility(layer, isInside);
        });
      });
    }

    function restoreFocusedBusRouteSelection() {
      if (!focusedBusRouteSelectionSnapshot) return;
      selectedBusRouteIds.clear();
      focusedBusRouteSelectionSnapshot.forEach((routeId) => selectedBusRouteIds.add(routeId));
      focusedBusRouteSelectionSnapshot = undefined;
      applyBusRouteFilters();
    }

    function applyFocusToBusRoutes(focusFeature) {
      if (!map.hasLayer(busRoutesLayer)) return;
      if (!focusedBusRouteSelectionSnapshot) {
        focusedBusRouteSelectionSnapshot = new Set(selectedBusRouteIds);
      }
      const focusedRouteIds = getLayerRouteIdsInFeature(busStopsLayer, focusFeature, { selectedOnly: false });
      selectedBusRouteIds.clear();
      focusedRouteIds.forEach((routeId) => selectedBusRouteIds.add(routeId));
      applyBusRouteFilters();
    }

    function refreshFocusedPopup(feature, layer, layerType) {
      if (!layer || !layer.getPopup) return;
      const popup = layer.getPopup();
      if (!popup) return;
      const content = layerType === "district"
        ? createCouncilDistrictPopup(feature)
        : createBoundaryPopup(feature, layerType);
      popup.setContent(content);
      if (!layer.isPopupOpen || !layer.isPopupOpen()) {
        layer.openPopup();
      }
    }

    function updateFocusControl() {
      if (focusToggleButton) {
        focusToggleButton.setAttribute("aria-pressed", mapInteractionMode === "focus" ? "true" : "false");
        let title;
        if (focusedBoundary) {
          title = `Focused on ${focusedBoundary.title}.`;
        } else if (mapInteractionMode === "focus") {
          title = "Click a polygon to focus the map.";
        } else {
          title = "Use Focus to isolate one polygon and its data points.";
        }
        focusToggleButton.title = title;
        focusToggleButton.setAttribute("aria-label", title);
      }
    }

    function clearMapFocus(options) {
      const settings = options || {};
      restoreFocusLayerStates();
      restoreFocusedBusRouteSelection();
      focusedBoundary = undefined;
      if (settings.resetMode) {
        mapInteractionMode = "browse";
      }
      updateFocusControl();
    }

    function focusBoundaryFeature(feature, layer, mode, layerType, options) {
      const settings = options || {};
      const sourceLayer = getFocusSourceLayer(layerType, mode);
      const focusFeature = getFocusGeometryFeature(feature, layerType);
      const title = layerType === "district"
        ? getBoundaryTitle(feature, "district")
        : getBoundaryTitle(feature, layerType);

      if (!settings.force && focusedBoundary && doesFeatureMatchFocus(feature, focusedBoundary)) {
        clearMapFocus();
        refreshFocusedPopup(feature, layer, layerType);
        return;
      }

      restoreFocusLayerStates();
      focusedBoundary = {
        feature,
        focusFeature,
        layer,
        layerType,
        mode,
        sourceLayer,
        title
      };
      applyFocusToBoundaryLayer(sourceLayer, focusedBoundary);
      applyFocusToPointLayers(focusFeature);
      applyFocusToBusRoutes(focusFeature);
      refreshFocusedPopup(feature, layer, layerType);
      orderMapLayers();
      updateFocusControl();
    }

    function formatContextMenuCoordinates(latLng) {
      return `${latLng.lat.toFixed(6)}, ${latLng.lng.toFixed(6)}`;
    }

    function copyTextToClipboard(text) {
      if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text);
      }

      return new Promise((resolve, reject) => {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        textArea.setAttribute("readonly", "");
        textArea.style.left = "-9999px";
        textArea.style.position = "fixed";
        document.body.appendChild(textArea);
        textArea.select();

        try {
          if (document.execCommand("copy")) {
            resolve();
          } else {
            reject(new Error("Copy command was not available."));
          }
        } catch (error) {
          reject(error);
        } finally {
          document.body.removeChild(textArea);
        }
      });
    }

    function hideMapContextMenu() {
      if (!mapContextMenuElement) return;
      mapContextMenuElement.classList.remove("is-open");
    }

    function createContextMenuButton(label, title, onClick) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = label;
      button.title = title || label;
      button.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        onClick(button);
      });
      return button;
    }

    function getComparablePointLayerDefinitions() {
      return [
        { layer: activePlaceLayer, layerType: "place" },
        { layer: archivedPlaceLayer, layerType: "place" },
        { layer: neighborhoodOrganizationsLayer, layerType: "neighborhoodOrganization" },
        { layer: jsoPoliceStationsLayer, layerType: "policeStation" },
        { layer: busStopsLayer, layerType: "busStop" },
        { layer: elementarySchoolsLayer, layerType: "school" },
        { layer: middleSchoolsLayer, layerType: "school" },
        { layer: highSchoolsLayer, layerType: "school" },
        { layer: dedicatedMagnetSchoolsLayer, layerType: "school" },
        { layer: fldoeTraditionalElementarySchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeTraditionalMiddleSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeTraditionalHighSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeTraditionalCombinationSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeTraditionalMagnetSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeCharterElementarySchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeCharterMiddleSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeCharterHighSchoolsLayer, layerType: "fldoeSchool" },
        { layer: fldoeCharterCombinationSchoolsLayer, layerType: "fldoeSchool" },
        { layer: privateElementarySchoolsLayer, layerType: "fldoeSchool" },
        { layer: privateMiddleSchoolsLayer, layerType: "fldoeSchool" },
        { layer: privateHighSchoolsLayer, layerType: "fldoeSchool" },
        { layer: privateCombinationSchoolsLayer, layerType: "fldoeSchool" },
        { layer: postSecondarySchoolsLayer, layerType: "fldoeSchool" }
      ];
    }

    function isFeatureLayerVisible(layer) {
      if (!layer) return false;
      if (layer.options && layer.options.interactive === false) return false;
      if (layer._path) {
        const pathOpacity = Number.parseFloat(layer._path.style.opacity || layer._path.getAttribute("opacity") || "1");
        if (layer._path.style.pointerEvents === "none" || pathOpacity === 0) return false;
      }
      return true;
    }

    function pinRouteCardsInFeature(polygonFeature) {
      if (!map.hasLayer(busRoutesLayer)) return 0;
      let pinnedCount = 0;
      const routeIds = getLayerRouteIdsInFeature(busStopsLayer, polygonFeature, { selectedOnly: true });
      routeIds.forEach((routeId) => {
        const routeLayers = busRouteLayersByRouteId.get(routeId) || [];
        const routeLayer = routeLayers.find((layer) => busRoutesLayer.hasLayer(layer)) || routeLayers[0];
        if (!routeLayer || !routeLayer.feature) return;
        pinComparableFeature(routeLayer.feature, "busRoute");
        pinnedCount += 1;
      });
      return pinnedCount;
    }

    function pinPointCardsInFeature(polygonFeature) {
      const geometry = polygonFeature.geometry || {};
      if (!geometry.coordinates) return 0;
      let pinnedCount = 0;
      getComparablePointLayerDefinitions().forEach((definition) => {
        if (!map.hasLayer(definition.layer) || !definition.layer.eachLayer) return;
        definition.layer.eachLayer((layer) => {
          if (!layer.getLatLng || !layer.feature || !isFeatureLayerVisible(layer)) return;
          const latLng = layer.getLatLng();
          if (!isPointInFeatureGeometry([latLng.lng, latLng.lat], geometry)) return;
          pinComparableFeature(layer.feature, definition.layerType);
          pinnedCount += 1;
        });
      });
      return pinnedCount;
    }

    function compareAllCardsInBoundary(feature, layerType) {
      const comparisonFeature = getPointCountFeature(feature, layerType);
      pinComparableFeature(feature, layerType);
      const routeCount = pinRouteCardsInFeature(comparisonFeature);
      const pointCount = pinPointCardsInFeature(comparisonFeature);
      renderPinnedCards();
      return routeCount + pointCount + 1;
    }

    function showMapContextMenu(event, featureContext) {
      if (!event || !event.latlng) return;
      const originalEvent = event.originalEvent;
      if (originalEvent) {
        originalEvent._mapsContextMenuHandled = true;
        L.DomEvent.preventDefault(originalEvent);
        L.DomEvent.stopPropagation(originalEvent);
      }

      if (!mapContextMenuElement) {
        mapContextMenuElement = document.createElement("div");
        mapContextMenuElement.className = "maps-context-menu";
        map.getContainer().appendChild(mapContextMenuElement);
        L.DomEvent.disableClickPropagation(mapContextMenuElement);
        L.DomEvent.disableScrollPropagation(mapContextMenuElement);
      }

      const coordinates = formatContextMenuCoordinates(event.latlng);
      mapContextMenuElement.replaceChildren();
      mapContextMenuElement.appendChild(createContextMenuButton(
        coordinates,
        "Copy coordinates",
        (button) => {
          copyTextToClipboard(coordinates)
            .then(() => {
              button.textContent = "Copied";
              window.setTimeout(hideMapContextMenu, 450);
            })
            .catch(() => {
              button.textContent = "Copy failed";
            });
        }
      ));

      if (featureContext && featureContext.feature && featureContext.layer) {
        const contextTitle = getComparableFeatureTitle(featureContext.feature, featureContext.layerType);
        const isPolygonContext = featureContext.feature.geometry &&
          (featureContext.feature.geometry.type === "Polygon" || featureContext.feature.geometry.type === "MultiPolygon");
        if (isPolygonContext && featureContext.layerType !== "busRoute") {
          mapContextMenuElement.appendChild(createContextMenuButton(
            "Focus",
            `Focus on ${contextTitle}`,
            () => {
              mapInteractionMode = "focus";
              focusBoundaryFeature(
                featureContext.feature,
                featureContext.layer,
                featureContext.mode,
                featureContext.layerType,
                { force: true }
              );
              hideMapContextMenu();
            }
          ));
        }
        mapContextMenuElement.appendChild(createContextMenuButton(
          "Compare",
          `Compare ${contextTitle}`,
          () => {
            compareModeEnabled = true;
            pinComparableFeature(featureContext.feature, featureContext.layerType);
            updateCompareControl();
            hideMapContextMenu();
          }
        ));
        if (isPolygonContext && featureContext.layerType !== "busRoute") {
          mapContextMenuElement.appendChild(createContextMenuButton(
            "Compare All",
            `Compare all visible cards in ${contextTitle}`,
            () => {
              compareModeEnabled = true;
              compareAllCardsInBoundary(featureContext.feature, featureContext.layerType);
              updateCompareControl();
              hideMapContextMenu();
            }
          ));
        }
      }

      const container = map.getContainer();
      const point = event.containerPoint || map.latLngToContainerPoint(event.latlng);
      mapContextMenuElement.style.visibility = "hidden";
      mapContextMenuElement.classList.add("is-open");
      const menuWidth = mapContextMenuElement.offsetWidth;
      const menuHeight = mapContextMenuElement.offsetHeight;
      const left = Math.max(0, Math.min(point.x, container.clientWidth - menuWidth - 4));
      const top = Math.max(0, Math.min(point.y, container.clientHeight - menuHeight - 4));
      mapContextMenuElement.style.left = `${left}px`;
      mapContextMenuElement.style.top = `${top}px`;
      mapContextMenuElement.style.visibility = "";
    }

    function setBoundaryLayer(control, enabled, allowMultiple) {
      clearMapFocus();
      if (enabled) {
        if (!map.hasLayer(control.layer)) map.addLayer(control.layer);
        restoreBoundaryLayerFeatures(control.layer);
        if (control.group && !allowMultiple) {
          boundaryLayerControls.forEach((otherControl) => {
            if (otherControl !== control && otherControl.group === control.group && map.hasLayer(otherControl.layer)) {
              map.removeLayer(otherControl.layer);
              setExplicitQueryLayerState(otherControl, false);
            }
          });
        }
        setExplicitQueryLayerState(control, true);
      } else if (map.hasLayer(control.layer)) {
        map.removeLayer(control.layer);
        setExplicitQueryLayerState(control, false);
      } else if (!enabled) {
        setExplicitQueryLayerState(control, false);
      }
      orderMapLayers();
      syncDistrictLayerInputs();
      updateLayerQueryUrl();
    }

    function normalizeLayerQueryToken(value) {
      return String(value || "").toLowerCase().replace(/[^a-z0-9]/g, "");
    }

    function registerQueryLayer(aliases, layer, options) {
      const settings = options || {};
      const querySlug = String(settings.slug || normalizeLayerQueryToken(aliases[0]));
      queryLayerSlugsByLayer.set(layer, querySlug);
      (settings.alternateLayers || []).forEach((alternateLayer) => {
        queryLayerSlugsByLayer.set(alternateLayer, querySlug);
      });
      aliases.forEach((alias) => {
        queryLayerControls.set(normalizeLayerQueryToken(alias), {
          layer,
          group: settings.group || "",
          querySlug
        });
      });
    }

    function setExplicitQueryLayerState(control, enabled) {
      const querySlug = control.querySlug || queryLayerSlugsByLayer.get(control.layer);
      if (!querySlug) return;
      if (enabled) {
        explicitQueryLayerSlugs.add(querySlug);
      } else {
        explicitQueryLayerSlugs.delete(querySlug);
      }
    }

    function updateLayerQueryUrl() {
      const url = new URL(window.location.href);
      const layerSlugs = Array.from(explicitQueryLayerSlugs);

      url.searchParams.delete("layer");
      url.searchParams.delete("layers");
      const searchParts = [
        url.searchParams.toString(),
        layerSlugs.length ? `layer=${layerSlugs.join(",")}` : ""
      ].filter(Boolean);
      const nextSearch = searchParts.length ? `?${searchParts.join("&")}` : "";

      window.history.replaceState(window.history.state, "", `${url.pathname}${nextSearch}${url.hash}`);
    }

    function getQueryLayerTokens() {
      const params = new URLSearchParams(window.location.search);
      return params.getAll("layer")
        .concat(params.getAll("layers"))
        .flatMap((value) => String(value).split(","))
        .map(normalizeLayerQueryToken)
        .filter(Boolean);
    }

    function activateOpacityQuery() {
      const params = new URLSearchParams(window.location.search);
      if (!params.has("opacity")) return;
      const opacity = Number(params.get("opacity"));
      if (!Number.isFinite(opacity)) return;
      setGovernmentOverlayOpacity(opacity / 100);
    }

    function hasBoundaryLayerQuery(tokens) {
      return tokens.some((token) => {
        const control = queryLayerControls.get(token);
        return control && control.group === "boundaries";
      });
    }

    function activateQueryLayers() {
      const tokens = getQueryLayerTokens();
      if (!tokens.length) return;

      const includesBoundaryLayer = hasBoundaryLayerQuery(tokens);
      const includesDefaultCouncilDistrict = tokens.some((token) => {
        const control = queryLayerControls.get(token);
        return control && control.layer === councilDistrictFillLayer;
      });
      if (includesBoundaryLayer && !includesDefaultCouncilDistrict && map.hasLayer(councilDistrictFillLayer)) {
        map.removeLayer(councilDistrictFillLayer);
        orderMapLayers();
        syncDistrictLayerInputs();
      }

      tokens.forEach((token) => {
        const control = queryLayerControls.get(token);
        if (control) {
          setBoundaryLayer(control, true, true);
        } else {
          console.warn(`Unknown map layer query: ${token}`);
        }
      });
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

    function createLayerGeometryIcon(type) {
      const icon = document.createElement("span");
      const geometryType = type || "point";
      const paths = {
        point: '<circle cx="8" cy="8" r="4"></circle>',
        line: '<path d="M2 11.5L6.2 6.8L9.6 9.1L14 3.8L14 6.2L10 11L6.6 8.7L2 14Z"></path>',
        polygon: '<path d="M2.2 5.4L7.1 1.9L13.8 4.2L12.5 12.3L5.1 14.1L2.2 5.4ZM4.1 6L6.4 12L10.9 10.9L11.8 5.5L7.4 4L4.1 6Z"></path>'
      };

      icon.className = `maps-layer-geometry-icon maps-layer-geometry-icon--${geometryType}`;
      icon.setAttribute("aria-hidden", "true");
      icon.innerHTML = `<svg viewBox="0 0 16 16" focusable="false">${paths[geometryType] || paths.point}</svg>`;
      return icon;
    }

    function appendLayerLabelContents(labelElement, input, label, geometryType) {
      const text = document.createElement("span");
      text.textContent = label;
      labelElement.appendChild(input);
      labelElement.appendChild(createLayerGeometryIcon(geometryType));
      labelElement.appendChild(text);
      return text;
    }

    function registerCountablePointLayer(label, layer, options) {
      const settings = options || {};
      if (settings.geometryType === "line" || settings.geometryType === "polygon" || settings.countable === false) return;
      countablePointLayers.push({ label: settings.countLabel || label, layer });
    }

    function createBoundaryLayerInput(label, layer, options) {
      const labelElement = document.createElement("label");
      const input = document.createElement("input");
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

      appendLayerLabelContents(labelElement, input, label, settings.geometryType || "point");
      registerCountablePointLayer(label, layer, settings);
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

    function sortBusRouteIds(routeIds) {
      return routeIds.sort((first, second) => {
        const firstNumber = Number.parseInt(first, 10);
        const secondNumber = Number.parseInt(second, 10);
        if (Number.isFinite(firstNumber) && Number.isFinite(secondNumber) && firstNumber !== secondNumber) {
          return firstNumber - secondNumber;
        }
        return String(first).localeCompare(String(second), undefined, { numeric: true });
      });
    }

    function updateBusRouteFilterSummary() {
      if (!busRouteFilterSummaryElement) return;
      const selectedCount = Array.from(busRouteMetadataByRouteId.keys()).filter((routeId) => selectedBusRouteIds.has(routeId)).length;
      const totalCount = busRouteMetadataByRouteId.size;
      busRouteFilterSummaryElement.textContent = totalCount
        ? `${selectedCount.toLocaleString()} of ${totalCount.toLocaleString()}`
        : "Loading";
      if (busRouteSelectionToggleButton) {
        busRouteSelectionToggleButton.disabled = totalCount === 0;
        busRouteSelectionToggleButton.textContent = totalCount > 0 && selectedCount === totalCount
          ? "Deselect All Routes"
          : "Select All Routes";
      }
    }

    function updateBusRouteFilterVisibility() {
      if (!busRouteFilterElement) return;
      busRouteFilterElement.hidden = !map.hasLayer(busRoutesLayer);
    }

    function syncBusRouteFilterInputs() {
      busRouteFilterInputs.forEach((input, routeId) => {
        input.checked = selectedBusRouteIds.has(routeId);
      });
      updateBusRouteFilterSummary();
    }

    function applyBusRouteFilters() {
      busRouteLayersByRouteId.forEach((layers, routeId) => {
        layers.forEach((layer) => {
          const isSelected = selectedBusRouteIds.has(routeId);
          if (isSelected && !busRoutesLayer.hasLayer(layer)) {
            busRoutesLayer.addLayer(layer);
          } else if (!isSelected && busRoutesLayer.hasLayer(layer)) {
            busRoutesLayer.removeLayer(layer);
          }
        });
      });
      orderMapLayers();
      syncBusRouteFilterInputs();
    }

    function toggleAllBusRoutes() {
      const routeIds = Array.from(busRouteMetadataByRouteId.keys());
      const shouldSelectAll = routeIds.some((routeId) => !selectedBusRouteIds.has(routeId));
      if (shouldSelectAll) {
        routeIds.forEach((routeId) => selectedBusRouteIds.add(routeId));
      } else {
        selectedBusRouteIds.clear();
      }
      applyBusRouteFilters();
    }

    function populateBusRouteFilterControls() {
      if (!busRouteFilterListElement || !busRouteMetadataByRouteId.size) return;
      busRouteFilterListElement.textContent = "";
      busRouteFilterInputs.clear();

      sortBusRouteIds(Array.from(busRouteMetadataByRouteId.keys())).forEach((routeId) => {
        const metadata = busRouteMetadataByRouteId.get(routeId);
        const label = document.createElement("label");
        const input = document.createElement("input");
        const swatch = document.createElement("span");
        const text = document.createElement("span");

        label.className = "maps-route-filter__row";
        input.type = "checkbox";
        input.className = "leaflet-control-layers-selector";
        input.checked = selectedBusRouteIds.has(routeId);
        input.addEventListener("change", function () {
          if (input.checked) {
            selectedBusRouteIds.add(routeId);
          } else {
            selectedBusRouteIds.delete(routeId);
          }
          applyBusRouteFilters();
        });

        swatch.className = "maps-route-filter__swatch";
        swatch.style.background = metadata.color;
        text.textContent = metadata.title;

        label.appendChild(input);
        label.appendChild(swatch);
        label.appendChild(text);
        busRouteFilterInputs.set(routeId, input);
        busRouteFilterListElement.appendChild(label);
      });

      updateBusRouteFilterSummary();
    }

    function createBusRouteFilterSection() {
      const details = document.createElement("details");
      const summary = document.createElement("summary");
      const title = document.createElement("span");
      const count = document.createElement("span");
      const toggleButton = document.createElement("button");
      const list = document.createElement("div");

      details.className = "maps-route-filter";
      title.textContent = "Routes";
      count.textContent = "Loading";
      toggleButton.type = "button";
      toggleButton.className = "maps-route-filter__toggle";
      toggleButton.textContent = "Select All Routes";
      toggleButton.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        toggleAllBusRoutes();
      });
      list.className = "maps-route-filter__list";
      busRouteFilterElement = details;
      busRouteFilterSummaryElement = count;
      busRouteSelectionToggleButton = toggleButton;
      busRouteFilterListElement = list;

      summary.appendChild(title);
      summary.appendChild(toggleButton);
      summary.appendChild(count);
      details.appendChild(summary);
      details.appendChild(list);
      populateBusRouteFilterControls();
      updateBusRouteFilterVisibility();

      return details;
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

    function createGovernmentLayerOpacityControl() {
      const opacityLabel = document.createElement("label");
      const opacityInput = document.createElement("input");

      opacityLabel.className = "maps-layer-opacity-control";
      opacityInput.type = "range";
      opacityInput.min = "0";
      opacityInput.max = "100";
      opacityInput.step = "1";
      opacityInput.setAttribute("aria-label", "Government layer overlay opacity");
      opacityInput.addEventListener("input", function () {
        setGovernmentOverlayOpacity(Number(opacityInput.value) / 100, { updateUrl: true });
      });
      opacityLabel.appendChild(opacityInput);
      governmentLayerOpacityInput = opacityInput;
      governmentLayerOpacityLabel = opacityLabel;
      updateGovernmentLayerOpacityControl();
      return opacityLabel;
    }

    function createLayerHeaderActions() {
      const wrapper = document.createElement("div");
      wrapper.className = "maps-layer-header-actions";
      if (supportsPointerHover) {
        wrapper.appendChild(createFocusModeControl());
        wrapper.appendChild(createCompareModeControl());
      }
      wrapper.appendChild(createGovernmentLayerOpacityControl());
      return wrapper;
    }

    function createFocusModeControl() {
      focusToggleButton = document.createElement("button");
      focusToggleButton.type = "button";
      focusToggleButton.textContent = "Focus";
      focusToggleButton.setAttribute("aria-pressed", "false");
      focusToggleButton.addEventListener("click", function () {
        if (mapInteractionMode === "focus") {
          clearMapFocus({ resetMode: true });
        } else {
          mapInteractionMode = "focus";
          updateFocusControl();
        }
      });

      updateFocusControl();
      return focusToggleButton;
    }

    function updateCompareControl() {
      if (compareToggleButton) {
        compareToggleButton.setAttribute("aria-pressed", compareModeEnabled ? "true" : "false");
        let title;
        if (compareModeEnabled) {
          title = "Click polygons to pin their cards.";
        } else if (pinnedBoundaryCards.length) {
          title = `${pinnedBoundaryCards.length.toLocaleString()} pinned card${pinnedBoundaryCards.length === 1 ? "" : "s"}.`;
        } else {
          title = "Use Compare to keep polygon cards open.";
        }
        compareToggleButton.title = title;
        compareToggleButton.setAttribute("aria-label", title);
      }
    }

    function getPinnedCardKey(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "busRoute") {
        return [
          layerType,
          properties.route_id,
          getBusRouteTitle(feature)
        ].filter(Boolean).join("|");
      }
      if (layerType === "busStop") {
        return [
          layerType,
          properties.stop_id,
          properties.stop_code,
          properties.stop_name
        ].filter(Boolean).join("|");
      }
      if (layerType === "policeStation") {
        return [
          layerType,
          properties.id,
          properties.name,
          properties.address
        ].filter(Boolean).join("|");
      }
      if (layerType === "neighborhoodOrganization") {
        return [
          layerType,
          properties.id,
          properties.name,
          properties.address
        ].filter(Boolean).join("|");
      }
      if (layerType === "school") {
        return [
          layerType,
          properties.USER_School_Number,
          properties.SchoolNumber,
          properties.OBJECTID,
          getSchoolName(feature),
          properties.IN_SingleLine || properties.Match_addr
        ].filter(Boolean).join("|");
      }
      if (layerType === "fldoeSchool") {
        return [
          layerType,
          properties.school_number,
          properties.federal_id,
          properties.school_name,
          properties.address || properties.formatted_address
        ].filter(Boolean).join("|");
      }
      if (layerType === "place") {
        return [
          layerType,
          properties.name,
          properties.address,
          properties.lat,
          properties.lng
        ].filter(Boolean).join("|");
      }
      return [
        layerType,
        properties.GEOID,
        properties.geoid,
        properties.CC,
        properties.CCAL,
        properties.school_board_district,
        properties.Name,
        properties.NAME,
        properties.label,
        properties.health_zone,
        properties.ZIPCODE,
        properties.DISTRICT,
        properties.SUBSECTOR,
        getBoundaryTitle(feature, layerType)
      ].filter(Boolean).join("|");
    }

    function getComparableFeatureTitle(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "busRoute") return getBusRouteTitle(feature);
      if (layerType === "busStop") return properties.stop_name || "JTA Bus Stop";
      if (layerType === "policeStation") return properties.name || "JSO Substation";
      if (layerType === "neighborhoodOrganization") return properties.name || "Neighborhood Organization";
      if (layerType === "school") return getSchoolName(feature);
      if (layerType === "fldoeSchool") return getFldoeSchoolName(feature);
      if (layerType === "place") return properties.name || "Map location";
      return getBoundaryTitle(feature, layerType);
    }

    function createPinnedCardContent(card) {
      if (card.layerType === "busRoute") {
        return createBusRoutePopup(card.feature);
      }
      if (card.layerType === "busStop") {
        return createBusStopPopup(card.feature);
      }
      if (card.layerType === "policeStation") {
        return createPoliceStationPopup(card.feature);
      }
      if (card.layerType === "neighborhoodOrganization") {
        return createNeighborhoodOrganizationPopup(card.feature);
      }
      if (card.layerType === "school") {
        return createSchoolPopup(card.feature);
      }
      if (card.layerType === "fldoeSchool") {
        return createFldoeSchoolPopup(card.feature);
      }
      if (card.layerType === "place") {
        return createPlacePopup(card.feature.properties || {});
      }
      if (card.layerType === "district") {
        return createCouncilDistrictPopup(card.feature);
      }
      return createBoundaryPopup(card.feature, card.layerType);
    }

    function renderPinnedCards() {
      if (!pinnedCardPanel || !pinnedCardBody) return;
      pinnedCardBody.textContent = "";
      pinnedCardPanel.classList.toggle("is-open", pinnedBoundaryCards.length > 0);

      pinnedBoundaryCards.forEach((card) => {
        const wrapper = document.createElement("article");
        const header = document.createElement("div");
        const title = document.createElement("strong");
        const closeButton = document.createElement("button");
        const content = createPinnedCardContent(card);

        wrapper.className = "maps-pinned-card";
        header.className = "maps-pinned-card__header";
        title.textContent = card.title;
        closeButton.type = "button";
        closeButton.className = "maps-pinned-card__close";
        closeButton.setAttribute("aria-label", `Remove ${card.title}`);
        closeButton.textContent = "x";
        closeButton.addEventListener("click", function () {
          const index = pinnedBoundaryCards.indexOf(card);
          if (index >= 0) {
            pinnedBoundaryCards.splice(index, 1);
            renderPinnedCards();
          }
        });

        const duplicateTitle = Array.from(content.children).find((element) => {
          return (element.tagName === "STRONG" || element.tagName === "A") && element.textContent === card.title;
        });
        if (duplicateTitle) {
          content.removeChild(duplicateTitle);
        }
        header.appendChild(title);
        header.appendChild(closeButton);
        wrapper.appendChild(header);
        wrapper.appendChild(content);
        pinnedCardBody.appendChild(wrapper);
      });

      updateCompareControl();
    }

    function clearPinnedCards() {
      pinnedBoundaryCards.splice(0, pinnedBoundaryCards.length);
      renderPinnedCards();
    }

    function pinComparableFeature(feature, layerType) {
      const key = getPinnedCardKey(feature, layerType);
      const existingCard = pinnedBoundaryCards.find((card) => card.key === key);
      const title = getComparableFeatureTitle(feature, layerType);

      if (existingCard) {
        existingCard.feature = feature;
        renderPinnedCards();
        return;
      }

      pinnedBoundaryCards.push({
        feature,
        key,
        layerType,
        title
      });
      renderPinnedCards();
    }

    function pinBoundaryFeature(feature, layerType) {
      pinComparableFeature(feature, layerType);
    }

    function createCompareModeControl() {
      compareToggleButton = document.createElement("button");
      compareToggleButton.type = "button";
      compareToggleButton.textContent = "Compare";
      compareToggleButton.setAttribute("aria-pressed", "false");
      compareToggleButton.addEventListener("click", function () {
        compareModeEnabled = !compareModeEnabled;
        updateCompareControl();
      });

      updateCompareControl();
      return compareToggleButton;
    }

    function addPinnedCardPanel() {
      if (!supportsPointerHover) return;

      const PinnedCardControl = L.Control.extend({
        options: {
          position: "topright"
        },
        onAdd: function () {
          pinnedCardPanel = L.DomUtil.create("aside", "maps-pinned-card-panel");
          const header = L.DomUtil.create("div", "maps-pinned-card-panel__header", pinnedCardPanel);
          const title = L.DomUtil.create("span", "maps-pinned-card-panel__title", header);
          const clearButton = L.DomUtil.create("button", "", header);

          title.textContent = "Pinned cards";
          clearButton.type = "button";
          clearButton.textContent = "Clear all";
          clearButton.addEventListener("click", clearPinnedCards);
          pinnedCardBody = L.DomUtil.create("div", "maps-pinned-card-panel__body", pinnedCardPanel);

          L.DomEvent.disableClickPropagation(pinnedCardPanel);
          L.DomEvent.disableScrollPropagation(pinnedCardPanel);
          return pinnedCardPanel;
        }
      });

      map.addControl(new PinnedCardControl());
    }

    function addCompareKeyboardShortcut() {
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && (compareModeEnabled || pinnedBoundaryCards.length)) {
          compareModeEnabled = false;
          clearPinnedCards();
          updateCompareControl();
        }
      });
    }

    function getSelectedGeographyControl(geographyControl) {
      return geographyControl.overlayControl;
    }

    function updateGovernmentLayerOpacityControl() {
      const opacityPercent = Math.round(governmentOverlayOpacity * 100);
      if (governmentLayerOpacityInput) {
        const thumbBorderChannel = Math.round(governmentOverlayOpacity * 255);
        const opacityFillChannel = Math.round(255 - ((255 - 66) * governmentOverlayOpacity));
        governmentLayerOpacityInput.value = String(opacityPercent);
        governmentLayerOpacityInput.title = `Overlay opacity: ${opacityPercent}%`;
        governmentLayerOpacityInput.style.setProperty("--maps-layer-opacity-alpha", String(governmentOverlayOpacity));
        governmentLayerOpacityInput.style.setProperty("--maps-layer-opacity-fill-color", `rgb(${opacityFillChannel} ${opacityFillChannel} ${opacityFillChannel})`);
        governmentLayerOpacityInput.style.setProperty("--maps-layer-opacity-percent", `${opacityPercent}%`);
        governmentLayerOpacityInput.style.setProperty("--maps-layer-thumb-border-color", `rgb(${thumbBorderChannel} ${thumbBorderChannel} ${thumbBorderChannel})`);
      }
      if (governmentLayerOpacityLabel) {
        governmentLayerOpacityLabel.title = `Overlay opacity: ${opacityPercent}%`;
      }
    }

    function updateOpacityQueryUrl() {
      const url = new URL(window.location.href);
      const opacityPercent = Math.round(governmentOverlayOpacity * 100);
      url.searchParams.set("opacity", String(opacityPercent));
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function setGovernmentOverlayOpacity(value, options) {
      const settings = options || {};
      const nextOpacity = Math.max(0, Math.min(1, Number.isFinite(value) ? value : 1));
      governmentOverlayOpacity = nextOpacity;
      governmentLayerMode = "fill";
      updateGovernmentLayerOpacityControl();
      geographyLayerControls.forEach((geographyControl) => {
        const nextControl = geographyControl.overlayControl;
        const previousControl = geographyControl.borderControl;
        const isActive = map.hasLayer(previousControl.layer) || map.hasLayer(nextControl.layer);
        if (!isActive) return;
        if (map.hasLayer(previousControl.layer)) {
          map.removeLayer(previousControl.layer);
        }
        if (!map.hasLayer(nextControl.layer)) {
          map.addLayer(nextControl.layer);
        }
      });
      restoreAllBoundaryFillLayerStyles();
      if (focusedBoundary) {
        focusedBoundary.mode = "fill";
        focusedBoundary.sourceLayer = getFocusSourceLayer(focusedBoundary.layerType, focusedBoundary.mode);
        applyFocusToBoundaryLayer(focusedBoundary.sourceLayer, focusedBoundary);
        applyFocusToPointLayers(focusedBoundary.focusFeature);
        updateFocusControl();
      }
      orderMapLayers();
      syncDistrictLayerInputs();
      if (settings.updateUrl) {
        updateOpacityQueryUrl();
      }
    }

    function appendGeographyLayerRow(parent, name, overlayLayer, borderLayer) {
      const row = document.createElement("div");
      const layerLabel = document.createElement("label");
      const layerInput = document.createElement("input");
      const overlayControl = { layer: overlayLayer, group: "boundaries" };
      const borderControl = { layer: borderLayer, group: "boundaries" };
      const geographyControl = { overlayControl, borderControl };
      let allowMultipleOnNextChange = false;

      row.className = "maps-layer-group-row";
      layerLabel.className = "maps-layer-group-row__name";
      layerInput.type = "checkbox";
      layerInput.className = "leaflet-control-layers-selector";
      appendLayerLabelContents(layerLabel, layerInput, name, "polygon");

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
          appendGeographyLayerRow(overlays, "School Board Districts", schoolBoardDistrictFillLayer, schoolBoardDistrictBorderLayer);
          appendGeographyLayerRow(overlays, "Cities", cityFillLayer, cityBorderLayer);
          appendGeographyLayerRow(overlays, "Counties", countyFillLayer, countyBorderLayer);
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
          appendGeographyLayerRow(overlays, "JSO Districts", jsoDistrictFillLayer, jsoDistrictBorderLayer);
          appendGeographyLayerRow(overlays, "JSO Subsections", jsoSubsectionFillLayer, jsoSubsectionBorderLayer);
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JSO Substations", jsoPoliceStationsLayer)
          ]);
          overlays.appendChild(createLayerHeading("Health"));
          appendGeographyLayerRow(overlays, "Health Zones", healthZoneFillLayer, healthZoneBorderLayer);
          overlays.appendChild(createLayerHeading("Transportation"));
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JTA Bus Routes", busRoutesLayer, { geometryType: "line" })
          ]);
          overlays.appendChild(createBusRouteFilterSection());
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JTA Bus Stops", busStopsLayer, { countLabel: "JTA Bus Stops" })
          ]);
          const traditionalPublicSchoolControls = [
            createBoundaryLayerInput("Elementary", fldoeTraditionalElementarySchoolsLayer, { countLabel: "Traditional Public Elementary" }),
            createBoundaryLayerInput("Middle", fldoeTraditionalMiddleSchoolsLayer, { countLabel: "Traditional Public Middle" }),
            createBoundaryLayerInput("High", fldoeTraditionalHighSchoolsLayer, { countLabel: "Traditional Public High" }),
            createBoundaryLayerInput("Combination", fldoeTraditionalCombinationSchoolsLayer, { countLabel: "Traditional Public Combination" }),
            createBoundaryLayerInput("Magnet", fldoeTraditionalMagnetSchoolsLayer, { countLabel: "Traditional Public Magnet" })
          ];
          const charterPublicSchoolControls = [
            createBoundaryLayerInput("Elementary", fldoeCharterElementarySchoolsLayer, { countLabel: "Charter Public Elementary" }),
            createBoundaryLayerInput("Middle", fldoeCharterMiddleSchoolsLayer, { countLabel: "Charter Public Middle" }),
            createBoundaryLayerInput("High", fldoeCharterHighSchoolsLayer, { countLabel: "Charter Public High" }),
            createBoundaryLayerInput("Combination", fldoeCharterCombinationSchoolsLayer, { countLabel: "Charter Public Combination" })
          ];
          const privateSchoolControls = [
            createBoundaryLayerInput("Elementary", privateElementarySchoolsLayer, { countLabel: "Private Elementary" }),
            createBoundaryLayerInput("Middle", privateMiddleSchoolsLayer, { countLabel: "Private Middle" }),
            createBoundaryLayerInput("High", privateHighSchoolsLayer, { countLabel: "Private High" }),
            createBoundaryLayerInput("Combination", privateCombinationSchoolsLayer, { countLabel: "Private Combination" })
          ];
          const postSecondarySchoolControls = [
            createBoundaryLayerInput("Post-Secondary Schools", postSecondarySchoolsLayer)
          ];
          const fldoeSchoolControls = traditionalPublicSchoolControls.concat(charterPublicSchoolControls, privateSchoolControls, postSecondarySchoolControls);

          overlays.appendChild(createLayerHeading("Education"));
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
          const layerHeaderActions = createLayerHeaderActions();
          setupCollapsibleMapControl(container, "Layers", list, {
            iconPath: "M296.5 69.2C311.4 62.3 328.6 62.3 343.5 69.2L562.1 170.2C570.6 174.1 576 182.6 576 192C576 201.4 570.6 209.9 562.1 213.8L343.5 314.8C328.6 321.7 311.4 321.7 296.5 314.8L77.9 213.8C69.4 209.8 64 201.3 64 192C64 182.7 69.4 174.1 77.9 170.2L296.5 69.2zM112.1 282.4L276.4 358.3C304.1 371.1 336 371.1 363.7 358.3L528 282.4L562.1 298.2C570.6 302.1 576 310.6 576 320C576 329.4 570.6 337.9 562.1 341.8L343.5 442.8C328.6 449.7 311.4 449.7 296.5 442.8L77.9 341.8C69.4 337.8 64 329.3 64 320C64 310.7 69.4 302.1 77.9 298.2L112 282.4zM77.9 426.2L112 410.4L276.3 486.3C304 499.1 335.9 499.1 363.6 486.3L527.9 410.4L562 426.2C570.5 430.1 575.9 438.6 575.9 448C575.9 457.4 570.5 465.9 562 469.8L343.4 570.8C328.5 577.7 311.3 577.7 296.4 570.8L77.9 469.8C69.4 465.8 64 457.3 64 448C64 438.7 69.4 430.1 77.9 426.2z",
            headerAction: layerHeaderActions
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          syncDistrictLayerInputs();
          return container;
        }
      });

      map.addControl(new DistrictLayerControl());
    }

    function addFocusKeyboardShortcut() {
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && (focusedBoundary || mapInteractionMode === "focus")) {
          clearMapFocus({ resetMode: true });
        }
      });
    }

    function addMapContextMenuHandlers() {
      map.on("contextmenu", function (event) {
        if (event.originalEvent && event.originalEvent._mapsContextMenuHandled) return;
        showMapContextMenu(event);
      });
      map.on("click movestart zoomstart popupopen", hideMapContextMenu);
      document.addEventListener("click", function (event) {
        if (!mapContextMenuElement || !mapContextMenuElement.classList.contains("is-open")) return;
        if (mapContextMenuElement.contains(event.target)) return;
        hideMapContextMenu();
      });
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
          hideMapContextMenu();
        }
      });
    }

    function registerMapQueryLayers() {
      registerQueryLayer(["councildistrict", "councildistricts", "citycouncildistrict", "citycouncildistricts"], councilDistrictFillLayer, { group: "boundaries", slug: "citycouncildistrict", alternateLayers: [councilDistrictBorderLayer] });
      registerQueryLayer(["councilatlarge", "councildistrictatlarge", "citycouncilatlarge", "citycouncildistrictatlarge"], councilAtLargeFillLayer, { group: "boundaries", slug: "citycouncilatlarge", alternateLayers: [councilAtLargeBorderLayer] });
      registerQueryLayer(["schoolboard", "schoolboarddistrict", "schoolboarddistricts"], schoolBoardDistrictFillLayer, { group: "boundaries", slug: "schoolboarddistricts", alternateLayers: [schoolBoardDistrictBorderLayer] });
      registerQueryLayer(["cities", "cityboundaries"], cityFillLayer, { group: "boundaries", slug: "cities", alternateLayers: [cityBorderLayer] });
      registerQueryLayer(["county", "counties", "countyboundaries", "duvalcounty", "duvalcountyboundary", "countyboundary"], countyFillLayer, { group: "boundaries", slug: "counties", alternateLayers: [countyBorderLayer] });
      registerQueryLayer(["floridahouse", "house", "statehouse"], floridaHouseFillLayer, { group: "boundaries", slug: "floridahouse", alternateLayers: [floridaHouseBorderLayer] });
      registerQueryLayer(["floridasenate", "senate", "statesenate"], floridaSenateFillLayer, { group: "boundaries", slug: "floridasenate", alternateLayers: [floridaSenateBorderLayer] });
      registerQueryLayer(["zip", "zips", "zipcode", "zipcodes", "zcta", "zctas"], zipCodeFillLayer, { group: "boundaries", slug: "zipcodes", alternateLayers: [zipCodeBorderLayer] });
      registerQueryLayer(["congress", "congressional", "congressionaldistrict", "congressionaldistricts"], congressionalDistrictFillLayer, { group: "boundaries", slug: "congressionaldistricts", alternateLayers: [congressionalDistrictBorderLayer] });
      registerQueryLayer(["neighborhood", "neighborhoods"], neighborhoodFillLayer, { group: "boundaries", slug: "neighborhoods", alternateLayers: [neighborhoodBorderLayer] });
      registerQueryLayer(["cpac", "cpacs", "planningdistricts"], cpacFillLayer, { group: "boundaries", slug: "cpacs", alternateLayers: [cpacBorderLayer] });
      registerQueryLayer(["health", "healthzone", "healthzones"], healthZoneFillLayer, { group: "boundaries", slug: "healthzones", alternateLayers: [healthZoneBorderLayer] });
      registerQueryLayer(["healthzones-byzipcodes", "healthzonesbyzipcodes", "healthzonesbyzip", "healthzoneslistedzips"], healthZoneByZipCodeLayer, { group: "boundaries", slug: "healthzones-byzipcodes" });
      registerQueryLayer(["jsodistrict", "jsodistricts", "sheriffdistricts"], jsoDistrictFillLayer, { group: "boundaries", slug: "jsodistricts", alternateLayers: [jsoDistrictBorderLayer] });
      registerQueryLayer(["jsosubsection", "jsosubsections", "jsosubsector", "jsosubsectors"], jsoSubsectionFillLayer, { group: "boundaries", slug: "jsosubsections", alternateLayers: [jsoSubsectionBorderLayer] });
      registerQueryLayer(["neighborhoodorganizations", "neighborhoodorgs", "neighborhoodpoints"], neighborhoodOrganizationsLayer, { slug: "neighborhoodorganizations" });
      registerQueryLayer(["substations", "jsosubstations", "policestations"], jsoPoliceStationsLayer, { slug: "substations" });
      registerQueryLayer(["busroutes", "jtabusroutes", "routes"], busRoutesLayer, { slug: "busroutes" });
      registerQueryLayer(["busstops", "jtabusstops", "stops"], busStopsLayer, { slug: "busstops" });
      registerQueryLayer(["traditionalpublicelementary", "publicelementary", "elementaryschools"], fldoeTraditionalElementarySchoolsLayer, { slug: "traditionalpublicelementary" });
      registerQueryLayer(["traditionalpublicmiddle", "publicmiddle", "middleschools"], fldoeTraditionalMiddleSchoolsLayer, { slug: "traditionalpublicmiddle" });
      registerQueryLayer(["traditionalpublichigh", "publichigh", "highschools"], fldoeTraditionalHighSchoolsLayer, { slug: "traditionalpublichigh" });
      registerQueryLayer(["traditionalpubliccombination", "publiccombination"], fldoeTraditionalCombinationSchoolsLayer, { slug: "traditionalpubliccombination" });
      registerQueryLayer(["traditionalpublicmagnet", "publicmagnet", "magnetschools"], fldoeTraditionalMagnetSchoolsLayer, { slug: "traditionalpublicmagnet" });
      registerQueryLayer(["charterelementary", "charterpublicelementary"], fldoeCharterElementarySchoolsLayer, { slug: "charterelementary" });
      registerQueryLayer(["chartermiddle", "charterpublicmiddle"], fldoeCharterMiddleSchoolsLayer, { slug: "chartermiddle" });
      registerQueryLayer(["charterhigh", "charterpublichigh"], fldoeCharterHighSchoolsLayer, { slug: "charterhigh" });
      registerQueryLayer(["chartercombination", "charterpubliccombination"], fldoeCharterCombinationSchoolsLayer, { slug: "chartercombination" });
      registerQueryLayer(["privateelementary", "privateschoolselementary"], privateElementarySchoolsLayer, { slug: "privateelementary" });
      registerQueryLayer(["privatemiddle", "privateschoolsmiddle"], privateMiddleSchoolsLayer, { slug: "privatemiddle" });
      registerQueryLayer(["privatehigh", "privateschoolshigh"], privateHighSchoolsLayer, { slug: "privatehigh" });
      registerQueryLayer(["privatecombination", "privateschoolscombination"], privateCombinationSchoolsLayer, { slug: "privatecombination" });
      registerQueryLayer(["postsecondary", "postsecondaryschools", "colleges"], postSecondarySchoolsLayer, { slug: "postsecondary" });
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
      if (layerType === "county") {
        return getStringColorNumber(properties.geoid || properties.GEOID || properties.name || "County");
      }
      if (layerType === "schoolBoard") {
        return Number.parseInt(properties.school_board_district || properties.SB, 10);
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
      if (layerType === "healthZone") {
        return Number.parseInt(properties.health_zone, 10);
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

    function getCountyBoundaryColor(feature) {
      const properties = feature.properties || {};
      const colorsByGeoid = {
        "12001": "#FA4616",
        "12003": "#5C6F68",
        "12007": "#9B5DE5",
        "12019": "#2A9D8F",
        "12031": "#006778",
        "12035": "#F4A261",
        "12089": "#457B9D",
        "12107": "#D45087",
        "12109": "#6A994E",
        "13039": "#8D6E63",
        "13049": "#7B2CBF"
      };
      return colorsByGeoid[properties.geoid || properties.GEOID] || "#006778";
    }

    function getCityBoundaryColor(feature) {
      const properties = feature.properties || {};
      const colorsByName = {
        "City of Jacksonville": "#006778",
        "City of Atlantic Beach": "#F4CA40",
        "City of Baldwin": "#7B2CBF",
        "City of Jacksonville Beach": "#2A9D8F",
        "City of Neptune Beach": "#D45087"
      };
      return colorsByName[properties.Name || properties.NAME] || "#006778";
    }

    function getBoundaryColor(feature, layerType) {
      if (layerType === "city") {
        return getCityBoundaryColor(feature);
      }
      if (layerType === "county") {
        return getCountyBoundaryColor(feature);
      }

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
        fillColor: color,
        fillOpacity: mode === "border" ? 0 : getOverlayFillOpacity(),
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
      if (layerType === "county") {
        return mode === "border" ? countyBorderLayer : countyFillLayer;
      }
      if (layerType === "schoolBoard") {
        return mode === "border" ? schoolBoardDistrictBorderLayer : schoolBoardDistrictFillLayer;
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
      if (layerType === "healthZone") {
        return mode === "border" ? healthZoneBorderLayer : healthZoneFillLayer;
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
      if (layerType === "county") {
        return properties.label || properties.name || properties.NAME || "County";
      }
      if (layerType === "schoolBoard") {
        return properties.label || (properties.school_board_district ? `Duval County School Board District ${properties.school_board_district}` : "Duval County School Board District");
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
      if (layerType === "healthZone") {
        return properties.label || (properties.health_zone ? `Health Zone ${properties.health_zone}` : "Health Zone");
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

    function getBoundaryTooltipTitle(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "healthZone") {
        return properties.tooltip_label || getBoundaryTitle(feature, layerType);
      }
      return getBoundaryTitle(feature, layerType);
    }

    function getBoundarySubtitle(feature, layerType) {
      const properties = feature.properties || {};
      if (layerType === "atLarge") {
        return properties.council_member_name || properties.C_NAME || "";
      }
      if (layerType === "city") {
        return properties.ESN ? `ESN ${properties.ESN}` : "";
      }
      if (layerType === "county") {
        return properties.boundary_type || "County boundary";
      }
      if (layerType === "schoolBoard") {
        return properties.member_name || "";
      }
      if (layerType === "neighborhood") {
        return properties.NUM_NAME && properties.NUM_NAME !== properties.NAME ? properties.NUM_NAME : "";
      }
      if (layerType === "cpac") {
        return properties.cpac_district ? `Planning District ${properties.planning_district || properties.PD_ID || properties.cpac_district}` : "Planning District";
      }
      if (layerType === "floridaHouse") {
        return properties.state_house_member_name || properties.HSE_NAME || properties.DELEGATES || "";
      }
      if (layerType === "floridaSenate") {
        return properties.state_senate_member_name || properties.SEN_NAME || "";
      }
      if (layerType === "zipCode") {
        return properties.boundary_type || [properties.USPS_CITY, properties.USPS_STATE].filter(Boolean).join(", ");
      }
      if (layerType === "congressional") {
        return properties.CDSESSN ? `${properties.CDSESSN}th Congress` : "";
      }
      if (layerType === "healthZone") {
        return properties.zip_codes_label ? `ZIP Codes: ${properties.zip_codes_label}` : "";
      }
      if (layerType === "jsoDistrict") {
        return "Jacksonville Sheriff's Office";
      }
      if (layerType === "jsoSubsector") {
        return [properties.SECTOR ? `Sector ${properties.SECTOR}` : "", properties.DISTRICT ? `District ${properties.DISTRICT}` : ""].filter(Boolean).join(" / ");
      }
      return properties.MEMBER_NAM || "";
    }

    function appendSchoolBoardMemberPopupDetails(popup, properties) {
      if (properties.member_image_url) {
        const image = document.createElement("img");
        image.src = properties.member_image_url;
        image.alt = properties.member_name || "School Board member";
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      [
        properties.member_role,
        properties.member_phone ? `Phone: ${properties.member_phone}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      if (properties.member_email) {
        const emailLink = document.createElement("a");
        emailLink.href = `mailto:${properties.member_email}`;
        emailLink.textContent = properties.member_email;
        popup.appendChild(emailLink);
      }

      if (properties.member_source_url) {
        const sourceLink = document.createElement("a");
        sourceLink.href = properties.member_source_url;
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = "View School Board page";
        popup.appendChild(sourceLink);
      }
    }

    function getCityCouncilMemberUrl(properties) {
      if (properties.council_member_source_url) {
        return properties.council_member_source_url;
      }

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
      if (layerType === "floridaHouse") {
        return properties.state_house_member_source_url || "";
      }
      if (layerType === "floridaSenate") {
        return properties.state_senate_member_source_url || "";
      }
      return "";
    }

    function isPointInRing(point, ring) {
      let inside = false;
      const x = point[0];
      const y = point[1];

      for (let index = 0, previousIndex = ring.length - 1; index < ring.length; previousIndex = index, index += 1) {
        const current = ring[index];
        const previous = ring[previousIndex];
        const xi = current[0];
        const yi = current[1];
        const xj = previous[0];
        const yj = previous[1];
        const intersects = ((yi > y) !== (yj > y)) && (x < ((xj - xi) * (y - yi)) / (yj - yi) + xi);
        if (intersects) inside = !inside;
      }

      return inside;
    }

    function isPointInPolygonCoordinates(point, polygonCoordinates) {
      if (!polygonCoordinates.length || !isPointInRing(point, polygonCoordinates[0])) return false;
      return !polygonCoordinates.slice(1).some((hole) => isPointInRing(point, hole));
    }

    function isPointInFeatureGeometry(point, geometry) {
      if (!geometry) return false;
      if (geometry.type === "Polygon") {
        return isPointInPolygonCoordinates(point, geometry.coordinates || []);
      }
      if (geometry.type === "MultiPolygon") {
        return (geometry.coordinates || []).some((polygonCoordinates) => isPointInPolygonCoordinates(point, polygonCoordinates));
      }
      return false;
    }

    function countLayerPointsInFeature(pointLayer, polygonFeature) {
      let count = 0;
      const geometry = polygonFeature.geometry || {};
      if (!pointLayer.eachLayer || !geometry.coordinates) return count;

      pointLayer.eachLayer((layer) => {
        if (!layer.getLatLng) return;
        const latLng = layer.getLatLng();
        if (isPointInFeatureGeometry([latLng.lng, latLng.lat], geometry)) {
          count += 1;
        }
      });

      return count;
    }

    function getPolygonRingsFromFeatureGeometry(geometry) {
      if (!geometry) return [];
      if (geometry.type === "Polygon") {
        return geometry.coordinates || [];
      }
      if (geometry.type === "MultiPolygon") {
        return (geometry.coordinates || []).flat();
      }
      return [];
    }

    function isPointOnSegment(point, segmentStart, segmentEnd) {
      const crossProduct = ((point[1] - segmentStart[1]) * (segmentEnd[0] - segmentStart[0])) -
        ((point[0] - segmentStart[0]) * (segmentEnd[1] - segmentStart[1]));
      if (Math.abs(crossProduct) > 1e-10) return false;

      const dotProduct = ((point[0] - segmentStart[0]) * (segmentEnd[0] - segmentStart[0])) +
        ((point[1] - segmentStart[1]) * (segmentEnd[1] - segmentStart[1]));
      if (dotProduct < 0) return false;

      const squaredLength = ((segmentEnd[0] - segmentStart[0]) ** 2) +
        ((segmentEnd[1] - segmentStart[1]) ** 2);
      return dotProduct <= squaredLength;
    }

    function getSegmentOrientation(pointA, pointB, pointC) {
      const value = ((pointB[1] - pointA[1]) * (pointC[0] - pointB[0])) -
        ((pointB[0] - pointA[0]) * (pointC[1] - pointB[1]));
      if (Math.abs(value) < 1e-10) return 0;
      return value > 0 ? 1 : 2;
    }

    function doLineSegmentsIntersect(segmentAStart, segmentAEnd, segmentBStart, segmentBEnd) {
      const orientation1 = getSegmentOrientation(segmentAStart, segmentAEnd, segmentBStart);
      const orientation2 = getSegmentOrientation(segmentAStart, segmentAEnd, segmentBEnd);
      const orientation3 = getSegmentOrientation(segmentBStart, segmentBEnd, segmentAStart);
      const orientation4 = getSegmentOrientation(segmentBStart, segmentBEnd, segmentAEnd);

      if (orientation1 !== orientation2 && orientation3 !== orientation4) return true;
      if (orientation1 === 0 && isPointOnSegment(segmentBStart, segmentAStart, segmentAEnd)) return true;
      if (orientation2 === 0 && isPointOnSegment(segmentBEnd, segmentAStart, segmentAEnd)) return true;
      if (orientation3 === 0 && isPointOnSegment(segmentAStart, segmentBStart, segmentBEnd)) return true;
      if (orientation4 === 0 && isPointOnSegment(segmentAEnd, segmentBStart, segmentBEnd)) return true;
      return false;
    }

    function doesLineCoordinateSequenceIntersectFeature(coordinates, polygonFeature) {
      const geometry = polygonFeature.geometry || {};
      const rings = getPolygonRingsFromFeatureGeometry(geometry);
      if (!coordinates || coordinates.length < 2 || !rings.length) return false;
      if (coordinates.some((point) => isPointInFeatureGeometry(point, geometry))) return true;

      for (let lineIndex = 1; lineIndex < coordinates.length; lineIndex += 1) {
        const lineStart = coordinates[lineIndex - 1];
        const lineEnd = coordinates[lineIndex];
        for (const ring of rings) {
          for (let ringIndex = 1; ringIndex < ring.length; ringIndex += 1) {
            if (doLineSegmentsIntersect(lineStart, lineEnd, ring[ringIndex - 1], ring[ringIndex])) {
              return true;
            }
          }
        }
      }
      return false;
    }

    function doesLineGeometryIntersectFeature(lineGeometry, polygonFeature) {
      if (!lineGeometry || !lineGeometry.coordinates) return false;
      if (lineGeometry.type === "LineString") {
        return doesLineCoordinateSequenceIntersectFeature(lineGeometry.coordinates, polygonFeature);
      }
      if (lineGeometry.type === "MultiLineString") {
        return (lineGeometry.coordinates || []).some((coordinates) => {
          return doesLineCoordinateSequenceIntersectFeature(coordinates, polygonFeature);
        });
      }
      return false;
    }

    function getCoordinateDistanceMiles(start, end) {
      const degreesToRadians = Math.PI / 180;
      const earthRadiusMiles = 3958.8;
      const startLatitude = start[1] * degreesToRadians;
      const endLatitude = end[1] * degreesToRadians;
      const latitudeDelta = (end[1] - start[1]) * degreesToRadians;
      const longitudeDelta = (end[0] - start[0]) * degreesToRadians;
      const haversine = Math.sin(latitudeDelta / 2) ** 2 +
        Math.cos(startLatitude) * Math.cos(endLatitude) * Math.sin(longitudeDelta / 2) ** 2;
      return earthRadiusMiles * 2 * Math.atan2(Math.sqrt(haversine), Math.sqrt(1 - haversine));
    }

    function getRouteSegmentMilesInFeature(coordinates, polygonFeature) {
      const geometry = polygonFeature.geometry || {};
      const totals = { inside: 0, total: 0 };
      if (!coordinates || coordinates.length < 2) return totals;

      for (let index = 1; index < coordinates.length; index += 1) {
        const start = coordinates[index - 1];
        const end = coordinates[index];
        const miles = getCoordinateDistanceMiles(start, end);
        const midpoint = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2];
        totals.total += miles;
        if (isPointInFeatureGeometry(midpoint, geometry)) {
          totals.inside += miles;
        }
      }

      return totals;
    }

    function getRouteGeometryMilesInFeature(lineGeometry, polygonFeature) {
      const totals = { inside: 0, total: 0 };
      const sequences = lineGeometry && lineGeometry.type === "LineString"
        ? [lineGeometry.coordinates]
        : lineGeometry && lineGeometry.type === "MultiLineString"
          ? lineGeometry.coordinates || []
          : [];

      sequences.forEach((coordinates) => {
        const sequenceTotals = getRouteSegmentMilesInFeature(coordinates, polygonFeature);
        totals.inside += sequenceTotals.inside;
        totals.total += sequenceTotals.total;
      });

      return totals;
    }

    function getCoordinateDistanceMeters(start, end, referenceLatitude) {
      const metersPerLatitudeDegree = 110540;
      const metersPerLongitudeDegree = 111320 * Math.cos((referenceLatitude || 0) * Math.PI / 180);
      const longitudeDelta = (end[0] - start[0]) * metersPerLongitudeDegree;
      const latitudeDelta = (end[1] - start[1]) * metersPerLatitudeDegree;
      return Math.sqrt((longitudeDelta ** 2) + (latitudeDelta ** 2));
    }

    function getPointToSegmentDistanceMeters(point, segmentStart, segmentEnd) {
      const referenceLatitude = point[1];
      const metersPerLatitudeDegree = 110540;
      const metersPerLongitudeDegree = 111320 * Math.cos(referenceLatitude * Math.PI / 180);
      const pointMeters = [point[0] * metersPerLongitudeDegree, point[1] * metersPerLatitudeDegree];
      const startMeters = [segmentStart[0] * metersPerLongitudeDegree, segmentStart[1] * metersPerLatitudeDegree];
      const endMeters = [segmentEnd[0] * metersPerLongitudeDegree, segmentEnd[1] * metersPerLatitudeDegree];
      const segmentX = endMeters[0] - startMeters[0];
      const segmentY = endMeters[1] - startMeters[1];
      const segmentLengthSquared = (segmentX ** 2) + (segmentY ** 2);
      if (!segmentLengthSquared) return getCoordinateDistanceMeters(point, segmentStart, referenceLatitude);

      const projectedPosition = Math.max(0, Math.min(1, (
        ((pointMeters[0] - startMeters[0]) * segmentX) +
        ((pointMeters[1] - startMeters[1]) * segmentY)
      ) / segmentLengthSquared));
      const closestPoint = [
        startMeters[0] + (projectedPosition * segmentX),
        startMeters[1] + (projectedPosition * segmentY)
      ];
      const distanceX = pointMeters[0] - closestPoint[0];
      const distanceY = pointMeters[1] - closestPoint[1];
      return Math.sqrt((distanceX ** 2) + (distanceY ** 2));
    }

    function getPointToRingDistanceMeters(point, ring) {
      if (!ring || ring.length < 2) return Number.POSITIVE_INFINITY;
      let minimumDistance = Number.POSITIVE_INFINITY;
      for (let index = 1; index < ring.length; index += 1) {
        minimumDistance = Math.min(minimumDistance, getPointToSegmentDistanceMeters(point, ring[index - 1], ring[index]));
      }
      return minimumDistance;
    }

    function getPointToFeatureBoundaryDistanceMeters(point, geometry) {
      return getPolygonRingsFromFeatureGeometry(geometry).reduce((minimumDistance, ring) => {
        return Math.min(minimumDistance, getPointToRingDistanceMeters(point, ring));
      }, Number.POSITIVE_INFINITY);
    }

    function isStopNearFeatureBoundary(point, polygonFeature) {
      const geometry = polygonFeature.geometry || {};
      return isPointInFeatureGeometry(point, geometry) ||
        getPointToFeatureBoundaryDistanceMeters(point, geometry) <= busRouteBoundaryToleranceMeters;
    }

    function getLayerRouteIdsInFeature(stopLayer, polygonFeature, options) {
      const settings = options || {};
      const routeIds = new Set();
      if (!stopLayer.eachLayer || !polygonFeature || !polygonFeature.geometry) return routeIds;

      stopLayer.eachLayer((layer) => {
        if (!layer.getLatLng || !layer.feature) return;
        const properties = layer.feature.properties || {};
        const stopRouteIds = properties.route_ids || [];
        if (!stopRouteIds.length) return;

        const latLng = layer.getLatLng();
        if (!isStopNearFeatureBoundary([latLng.lng, latLng.lat], polygonFeature)) return;

        stopRouteIds.forEach((routeId) => {
          const normalizedRouteId = String(routeId);
          if (!settings.selectedOnly || selectedBusRouteIds.has(normalizedRouteId)) {
            routeIds.add(normalizedRouteId);
          }
        });
      });

      return routeIds;
    }

    function countLayerRoutesInFeature(stopLayer, polygonFeature) {
      return getLayerRouteIdsInFeature(stopLayer, polygonFeature, { selectedOnly: true }).size;
    }

    function getActiveHealthZoneLayer() {
      if (map.hasLayer(healthZoneByZipCodeLayer)) return healthZoneByZipCodeLayer;
      if (map.hasLayer(healthZoneFillLayer)) return healthZoneFillLayer;
      if (map.hasLayer(healthZoneBorderLayer)) return healthZoneBorderLayer;
      return null;
    }

    function getHealthZoneCountFeature(feature) {
      const properties = feature.properties || {};
      const healthZone = properties.health_zone;
      const sourceLayer = getActiveHealthZoneLayer();
      const polygons = [];

      if (!sourceLayer || !sourceLayer.eachLayer || healthZone === undefined || healthZone === null) {
        return feature;
      }

      sourceLayer.eachLayer((layer) => {
        const layerFeature = layer.feature || {};
        const layerProperties = layerFeature.properties || {};
        const geometry = layerFeature.geometry || {};
        if (layerProperties.health_zone !== healthZone) return;

        if (geometry.type === "Polygon") {
          polygons.push(geometry.coordinates);
        } else if (geometry.type === "MultiPolygon") {
          polygons.push(...(geometry.coordinates || []));
        }
      });

      if (!polygons.length) return feature;

      return {
        type: "Feature",
        properties,
        geometry: {
          type: "MultiPolygon",
          coordinates: polygons
        }
      };
    }

    function getPointCountFeature(feature, layerType) {
      if (layerType === "healthZone") {
        return getHealthZoneCountFeature(feature);
      }
      return feature;
    }

    function appendActivePointCounts(popup, feature, boundaryTitle) {
      const activeCounts = countablePointLayers
        .filter((pointLayer) => map.hasLayer(pointLayer.layer))
        .map((pointLayer) => ({
          label: pointLayer.label,
          count: countLayerPointsInFeature(pointLayer.layer, feature)
        }));
      if (map.hasLayer(busRoutesLayer)) {
        activeCounts.push({
          label: "JTA Bus Routes",
          count: countLayerRoutesInFeature(busStopsLayer, feature)
        });
      }

      if (!activeCounts.length) return;

      const heading = document.createElement("strong");
      heading.textContent = `Data points in ${boundaryTitle || "this area"}:`;
      popup.appendChild(heading);

      activeCounts.forEach((pointLayer) => {
        const line = document.createElement("span");
        line.textContent = `${pointLayer.label}: ${pointLayer.count.toLocaleString()}`;
        popup.appendChild(line);
      });
    }

    function createBoundaryPopup(feature, layerType) {
      const popup = document.createElement("div");
      const titleUrl = getBoundaryTitleUrl(feature, layerType);
      const title = titleUrl ? document.createElement("a") : document.createElement("strong");
      const subtitle = getBoundarySubtitle(feature, layerType);
      const pointCountFeature = getPointCountFeature(feature, layerType);
      const boundaryTitle = getBoundaryTitle(feature, layerType);

      popup.className = "maps-district-popup";
      title.textContent = boundaryTitle;
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

      if (layerType === "schoolBoard") {
        appendSchoolBoardMemberPopupDetails(popup, feature.properties || {});
      }

      if (layerType === "atLarge") {
        appendCityCouncilMemberPopupDetails(popup, feature.properties || {});
      }

      if (layerType === "floridaHouse") {
        appendStateLegislatorPopupDetails(popup, feature.properties || {}, "state_house", "House member");
      }

      if (layerType === "floridaSenate") {
        appendStateLegislatorPopupDetails(popup, feature.properties || {}, "state_senate", "Senator");
      }

      if (layerType === "healthZone") {
        appendHealthZonePopupDetails(popup, feature.properties || {});
      }

      if (layerType === "zipCode") {
        appendZipCodePopupDetails(popup, feature.properties || {});
      }

      appendActivePointCounts(popup, pointCountFeature, boundaryTitle);

      return popup;
    }

    function appendZipCodePopupDetails(popup, properties) {
      [
        properties.source,
        properties.caveat
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      if (properties.source_url) {
        const sourceLink = document.createElement("a");
        sourceLink.href = properties.source_url;
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = "View Census TIGER/Line source";
        popup.appendChild(sourceLink);
      }
    }

    function appendHealthZonePopupDetails(popup, properties) {
      [
        properties.assumption_note,
        properties.missing_geometry_note
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
    }

    function appendStateLegislatorPopupDetails(popup, properties, prefix, fallbackLabel) {
      const name = properties[`${prefix}_member_name`] || "";
      const chamber = properties[`${prefix}_member_chamber`] || "";
      const district = properties[`${prefix}_member_district`] || "";
      const party = properties[`${prefix}_member_party`] || "";
      const leadershipRole = properties[`${prefix}_member_leadership_role`] || "";
      const phone = properties[`${prefix}_member_phone`] || "";
      const capitolPhone = properties[`${prefix}_member_capitol_phone`] || "";
      const email = properties[`${prefix}_member_email`] || "";
      const contactUrl = properties[`${prefix}_member_contact_url`] || "";
      const sourceUrl = properties[`${prefix}_member_source_url`] || "";
      const photoUrl = properties[`${prefix}_member_photo_url`] || "";
      const districtOffice = properties[`${prefix}_member_district_office`] || "";
      const cityOfResidence = properties[`${prefix}_member_city_of_residence`] || "";

      if (photoUrl) {
        const image = document.createElement("img");
        image.src = photoUrl;
        image.alt = name || fallbackLabel;
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      [
        chamber && district ? `${chamber} District ${district}` : "",
        party,
        leadershipRole,
        cityOfResidence ? `City of Residence: ${cityOfResidence}` : "",
        phone ? `Phone: ${phone}` : "",
        capitolPhone && capitolPhone !== phone ? `Capitol Phone: ${capitolPhone}` : "",
        districtOffice ? `District Office: ${districtOffice}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      if (email) {
        const emailLink = document.createElement("a");
        emailLink.href = `mailto:${email}`;
        emailLink.textContent = email;
        popup.appendChild(emailLink);
      }

      if (contactUrl) {
        const contactLink = document.createElement("a");
        contactLink.href = contactUrl;
        contactLink.target = "_blank";
        contactLink.rel = "noopener";
        contactLink.textContent = `Contact ${fallbackLabel}`;
        popup.appendChild(contactLink);
      }

      if (sourceUrl) {
        const sourceLink = document.createElement("a");
        sourceLink.href = sourceUrl;
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = `View ${fallbackLabel} page`;
        popup.appendChild(sourceLink);
      }
    }

    function appendCityCouncilMemberPopupDetails(popup, properties) {
      if (properties.council_member_photo_url) {
        const image = document.createElement("img");
        image.src = properties.council_member_photo_url;
        image.alt = properties.council_member_name || "City Council member";
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      [
        properties.council_member_leadership_role,
        properties.council_member_role,
        properties.council_member_phone ? `Phone: ${properties.council_member_phone}` : "",
        properties.council_member_assistant ? `Assistant: ${properties.council_member_assistant}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      if (properties.council_member_email) {
        const emailLink = document.createElement("a");
        emailLink.href = `mailto:${properties.council_member_email}`;
        emailLink.textContent = properties.council_member_email;
        popup.appendChild(emailLink);
      }

      if (properties.council_member_source_url) {
        const sourceLink = document.createElement("a");
        sourceLink.href = properties.council_member_source_url;
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = "View City Council member page";
        popup.appendChild(sourceLink);
      }
    }

    function createCouncilDistrictPopup(feature) {
      const properties = feature.properties || {};
      const district = properties.CC || properties.DISTRICT_N || properties.DISTRICT || "";
      const member = properties.council_member_name || properties.MEMBER_NAM || "";
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

      appendCityCouncilMemberPopupDetails(popup, properties);
      appendActivePointCounts(popup, feature, title.textContent);

      return popup;
    }

    function addCouncilDistrictInteractivity(feature, layer, mode) {
      const district = (feature.properties || {}).CC || getDistrictNumber(feature);
      layer.options.boundaryMode = mode;
      layer.options.boundaryType = "district";
      layer.bindPopup(() => createCouncilDistrictPopup(feature));
      layer.on("click", function () {
        if (mapInteractionMode === "focus") {
          focusBoundaryFeature(feature, layer, mode, "district");
        }
        if (compareModeEnabled) {
          pinBoundaryFeature(feature, "district");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, mode, layerType: "district" });
      });
      if (district && supportsPointerHover) {
        layer.bindTooltip(`City Council District ${district}`, {
          sticky: true
        });
      }
      if (supportsPointerHover) {
        layer.on({
          mouseover: function () {
            layer.setStyle({
              fillOpacity: mode === "border" ? 0 : getOverlayFillOpacity(1.25),
              weight: mode === "border" ? 1.75 : 1.25
            });
          },
          mouseout: function () {
            if (focusedBoundary && doesFeatureMatchFocus(feature, focusedBoundary)) {
              setFocusedBoundaryStyle(layer);
              return;
            }
            layer.setStyle(getCouncilDistrictStyle(feature, mode));
          }
        });
      }
    }

    function addBoundaryInteractivity(feature, layer, mode, layerType) {
      layer.options.boundaryMode = mode;
      layer.options.boundaryType = layerType;
      layer.bindPopup(() => createBoundaryPopup(feature, layerType));
      layer.on("click", function () {
        if (mapInteractionMode === "focus") {
          focusBoundaryFeature(feature, layer, mode, layerType);
        }
        if (compareModeEnabled) {
          pinBoundaryFeature(feature, layerType);
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, mode, layerType });
      });
      if (supportsPointerHover) {
        layer.bindTooltip(getBoundaryTooltipTitle(feature, layerType), {
          sticky: true
        });
      }
      if (supportsPointerHover) {
        layer.on({
          mouseover: function () {
            layer.setStyle({
              fillOpacity: mode === "border" ? 0 : getOverlayFillOpacity(1.25),
              weight: mode === "border" ? 1.75 : 1.25
            });
          },
          mouseout: function () {
            if (focusedBoundary && doesFeatureMatchFocus(feature, focusedBoundary)) {
              setFocusedBoundaryStyle(layer);
              return;
            }
            layer.setStyle(getBoundaryStyle(feature, mode, layerType));
          }
        });
      }
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

    function getBusRouteTitle(feature) {
      const properties = feature.properties || {};
      const name = [properties.route_short_name, properties.route_long_name].filter(Boolean).join(" - ");
      return name || `Route ${properties.route_id || ""}`.trim() || "JTA Bus Route";
    }

    function registerBusRouteFeature(feature, layer) {
      const properties = feature.properties || {};
      const routeId = properties.route_id ? String(properties.route_id) : "";
      if (!routeId) return;

      if (!busRouteLayersByRouteId.has(routeId)) {
        busRouteLayersByRouteId.set(routeId, []);
      }
      busRouteLayersByRouteId.get(routeId).push(layer);
      if (!busRouteMetadataByRouteId.has(routeId)) {
        busRouteMetadataByRouteId.set(routeId, {
          color: normalizeHexColor(properties.route_color, "#0f766e"),
          title: getBusRouteTitle(feature)
        });
        selectedBusRouteIds.add(routeId);
        populateBusRouteFilterControls();
      }
    }

    function createBusRoutePopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = getBusRouteTitle(feature);
      popup.appendChild(title);

      if (properties.route_pdf_url) {
        const scheduleLink = document.createElement("a");
        scheduleLink.className = "maps-route-pdf-link";
        scheduleLink.href = properties.route_pdf_url;
        scheduleLink.target = "_blank";
        scheduleLink.rel = "noopener";
        scheduleLink.textContent = "JTA schedule PDF";
        popup.appendChild(scheduleLink);
      }

      (properties.route_schedule || []).forEach((value) => {
        const scheduleLine = document.createElement("span");
        scheduleLine.textContent = value;
        popup.appendChild(scheduleLine);
      });

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
      const name = getBusRouteTitle(feature);
      registerBusRouteFeature(feature, layer);
      layer.bindPopup(createBusRoutePopup(feature));
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "busRoute");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "busRoute" });
      });
      if (supportsPointerHover) {
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
    }

    function addBusStopInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createBusStopPopup(feature));
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "busStop");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "busStop" });
      });
      if (properties.stop_name && supportsPointerHover) {
        layer.bindTooltip(properties.stop_name, {
          sticky: true
        });
      }
    }

    function addPoliceStationInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createPoliceStationPopup(feature));
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "policeStation");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "policeStation" });
      });
      if (supportsPointerHover) {
        layer.bindTooltip(properties.name || "JSO Substation", {
          sticky: true
        });
      }
    }

    function addNeighborhoodOrganizationInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createNeighborhoodOrganizationPopup(feature));
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "neighborhoodOrganization");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "neighborhoodOrganization" });
      });
      if (supportsPointerHover) {
        layer.bindTooltip(properties.name || "Neighborhood Organization", {
          sticky: true
        });
      }
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
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "school");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "school" });
      });
      if (name && supportsPointerHover) {
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
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "fldoeSchool");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "fldoeSchool" });
      });
      if (name && supportsPointerHover) {
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
      marker.feature = {
        type: "Feature",
        properties: place,
        geometry: {
          type: "Point",
          coordinates: [place.lng, place.lat]
        }
      };

      marker.bindPopup(createPlacePopup(place)).addTo(targetLayer);
      marker.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(marker.feature, "place");
        }
      });
      marker.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature: marker.feature, layer: marker, layerType: "place" });
      });
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
      updateZoomHomeDefaultBounds();
    }

    function loadCouncilDistricts() {
      beginMapDataLoad();
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
          updateZoomHomeDefaultBounds();
          if (!places.length && councilDistrictFillLayer.getLayers().length) {
            map.fitBounds(councilDistrictFillLayer.getBounds(), {
              padding: [24, 24]
            });
          }
        })
        .catch((error) => {
          console.warn(error);
        })
        .finally(() => {
          finishMapDataLoad();
        });
    }

    function loadBoundaryLayers(url, fillLayer, borderLayer, label) {
      beginMapDataLoad();
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
          if (focusedBoundary) {
            applyFocusToBoundaryLayer(focusedBoundary.sourceLayer, focusedBoundary);
            applyFocusToPointLayers(focusedBoundary.focusFeature);
            applyFocusToBusRoutes(focusedBoundary.focusFeature);
          }
        })
        .catch((error) => {
          console.warn(error);
        })
        .finally(() => {
          finishMapDataLoad();
        });
    }

    function loadGeoJsonLayer(url, layer, label) {
      beginMapDataLoad();
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
          if (focusedBoundary) {
            applyFocusToBoundaryLayer(focusedBoundary.sourceLayer, focusedBoundary);
            applyFocusToPointLayers(focusedBoundary.focusFeature);
            applyFocusToBusRoutes(focusedBoundary.focusFeature);
          }
        })
        .catch((error) => {
          console.warn(error);
        })
        .finally(() => {
          finishMapDataLoad();
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
      "/data/duval-county-school-board-districts.geojson",
      schoolBoardDistrictFillLayer,
      schoolBoardDistrictBorderLayer,
      "Duval County School Board districts"
    );
    loadBoundaryLayers(
      "/data/city-boundaries.geojson",
      cityFillLayer,
      cityBorderLayer,
      "city boundaries"
    );
    loadBoundaryLayers(
      "/data/counties.geojson",
      countyFillLayer,
      countyBorderLayer,
      "county boundaries"
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
    loadBoundaryLayers(
      "/data/duval-health-zones.geojson",
      healthZoneFillLayer,
      healthZoneBorderLayer,
      "Duval County health zones"
    );
    loadGeoJsonLayer("/data/duval-health-zones-by-zipcodes.geojson", healthZoneByZipCodeLayer, "Duval County health zones by listed ZIP codes");
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

    addDistrictLayerControl();
    zoomHomeControl = L.Control.zoomHome({
      position: "topleft"
    });
    zoomHomeControl.addTo(map);
    updateZoomHomeDefaultBounds();
    L.control.fullscreen({
      position: "topleft"
    }).addTo(map);
    addPinnedCardPanel();
    addFocusKeyboardShortcut();
    addCompareKeyboardShortcut();
    addMapContextMenuHandlers();
    registerMapQueryLayers();
    activateOpacityQuery();
    activateQueryLayers();
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
