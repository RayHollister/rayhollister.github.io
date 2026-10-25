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
  .leaflet-container {
    background: #ffffff;
  }
  .leaflet-container.maps-modifier-rotating {
    cursor: grabbing;
  }
  .leaflet-top .leaflet-control {
    margin-bottom: 10px;
  }

  #ray-map .leaflet-bottom.leaflet-left,
  #ray-map .leaflet-bottom.leaflet-right {
    z-index: 800;
  }

  #ray-map .leaflet-top.leaflet-left.maps-top-left-menu {
    z-index: 1000;
  }
  .maps-page {
    --maps-control-panel-header-height: 2.05rem;
    --maps-control-panel-max-height: calc(100vh - 6rem);
    --maps-control-panel-max-height: calc(100dvh - 6rem);
    display: grid;
    height: calc(100vh - 56px);
    height: calc(100dvh - 56px);
    min-height: 0;
    position: relative;
    z-index: 0;
  }

  .maps-page:has(#ray-map.leaflet-pseudo-fullscreen) {
    z-index: 1300;
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

  .maps-district-popup .maps-popup-title {
    font-weight: 700;
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

  .maps-district-popup.maps-district-popup--with-photo {
    align-items: start;
    column-gap: 0.6rem;
    display: grid;
    grid-template-columns: 72px minmax(9rem, max-content);
    max-width: min(42rem, calc(100vw - 7rem));
    min-width: 15.75rem;
    width: fit-content;
  }

  .maps-district-popup.maps-district-popup--with-photo img {
    grid-column: 1;
    grid-row: 1 / span 20;
    margin-bottom: 0;
  }

  .maps-district-popup.maps-district-popup--with-photo > :not(img) {
    grid-column: 2;
    max-width: calc(100vw - 12rem);
    min-width: 0;
    overflow-wrap: normal;
  }

  .maps-district-popup.maps-district-popup--with-photo a {
    overflow-wrap: break-word;
    word-break: normal;
  }

  .maps-district-popup.maps-district-popup--with-photo .maps-popup-title {
    margin-top: 0;
  }

  #ray-map .leaflet-popup-content:has(.maps-district-popup--with-photo) {
    max-width: min(42rem, calc(100vw - 7rem));
    width: fit-content !important;
  }

  #ray-map .leaflet-popup-content.maps-popup-content--contact-width:has(.maps-district-popup--with-photo) {
    max-width: min(20rem, calc(100vw - 7rem));
    width: min(20rem, calc(100vw - 7rem)) !important;
  }

  #ray-map .leaflet-popup-content.maps-popup-content--contact-width .maps-district-popup.maps-district-popup--with-photo {
    grid-template-columns: 72px minmax(0, 1fr);
    max-width: none;
    width: 100%;
  }

  #ray-map .leaflet-popup-content.maps-popup-content--contact-width .maps-district-popup.maps-district-popup--with-photo > :not(img) {
    max-width: none;
  }

  #ray-map .leaflet-control-attribution {
    display: none;
    max-width: min(36rem, calc(100vw - 5rem));
  }

  #ray-map.maps-attribution-expanded .leaflet-control-attribution {
    display: block;
  }

  .maps-attribution-toggle {
    background: #fff;
  }

  .maps-attribution-toggle button {
    align-items: center;
    background: transparent;
    border: 0;
    color: #24292f;
    cursor: pointer;
    display: flex;
    font: 700 13px/1 sans-serif;
    height: 30px;
    justify-content: center;
    padding: 0;
    width: 30px;
  }

  #ray-map .leaflet-top.leaflet-left.maps-top-left-menu:not(.is-open) > .leaflet-control:not(.maps-top-left-menu-toggle) {
    display: none;
  }

  .maps-top-left-menu-toggle {
    background: #fff;
  }

  .maps-top-left-menu-toggle button {
    align-items: center;
    background: transparent;
    border: 0;
    color: #24292f;
    cursor: pointer;
    display: flex;
    font: 700 20px/1 sans-serif;
    height: 30px;
    justify-content: center;
    padding: 0;
    width: 30px;
  }

  .maps-district-popup > .maps-senator-card {
    border-top: 1px solid #d0d7de;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
  }

  .maps-district-popup > .maps-senator-card:first-of-type {
    border-top: 0;
    margin-top: 0.35rem;
    padding-top: 0;
  }

  @media (max-width: 360px) {
    #ray-map .leaflet-popup-content.maps-popup-content--contact-width:has(.maps-district-popup--with-photo) {
      width: calc(100vw - 7rem) !important;
    }

    #ray-map .leaflet-popup-content.maps-popup-content--contact-width .maps-district-popup.maps-district-popup--with-photo {
      grid-template-columns: 1fr;
      min-width: 0;
    }

    .maps-district-popup.maps-district-popup--with-photo {
      grid-template-columns: 1fr;
      min-width: 0;
      width: min(13rem, calc(100vw - 7rem));
    }

    .maps-district-popup.maps-district-popup--with-photo img,
    .maps-district-popup.maps-district-popup--with-photo > :not(img) {
      grid-column: 1;
      grid-row: auto;
    }

    .maps-district-popup.maps-district-popup--with-photo img {
      margin-bottom: 0.4rem;
    }
  }

  .leaflet-popup.maps-draggable-popup .leaflet-popup-content-wrapper {
    cursor: grab;
  }

  .leaflet-popup.maps-draggable-popup .leaflet-popup-content-wrapper a,
  .leaflet-popup.maps-draggable-popup .leaflet-popup-content-wrapper button {
    cursor: pointer;
  }

  .leaflet-popup.maps-popup-dragging .leaflet-popup-content-wrapper {
    cursor: grabbing;
    user-select: none;
  }

  .maps-control-panel,
  .maps-basemap-control,
  .maps-leadership-locations-control {
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

  .maps-basemap-control.is-open .maps-control-panel__header {
    border-bottom: 1px solid #d0d7de;
    gap: 0.35rem;
    justify-content: flex-start;
    padding-right: 0.45rem;
  }

  .maps-leadership-locations-control.is-open .maps-control-panel__header {
    border-bottom: 1px solid #d0d7de;
  }

  .maps-layers-control:not(.is-open) .maps-control-panel__header {
    display: block;
  }

  .maps-basemap-control:not(.is-open) .maps-control-panel__header {
    display: block;
  }

  .maps-leadership-locations-control:not(.is-open) .maps-control-panel__header {
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

  .maps-layers-control .maps-control-panel__body,
  .maps-basemap-control .maps-control-panel__body {
    max-height: calc(var(--maps-open-control-max-height, var(--maps-control-panel-max-height)) - var(--maps-control-panel-header-height));
    overflow-y: auto;
  }

  .maps-basemap-control .maps-control-panel__body {
    display: flex;
    flex-direction: column;
    max-height: calc(var(--maps-open-control-max-height, var(--maps-control-panel-max-height)) - var(--maps-control-panel-header-height));
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

  .maps-basemap-control .maps-layer-subheading {
    border-top: 1px solid #d0d7de;
    margin: 0;
    padding: 0.45rem 0.6rem 0.2rem;
  }

  .maps-basemap-control .maps-historic-map-opacity-control {
    box-sizing: border-box;
    margin: 0.1rem 0.6rem 0.35rem;
    width: calc(100% - 1.2rem);
  }

  .maps-basemap-control .maps-layer-control-row {
    align-items: center;
    cursor: pointer;
    display: flex;
    gap: 0.45rem;
    padding: 0.35rem 0.6rem 0.5rem;
  }

  .maps-leadership-locations-control .maps-control-panel__body {
    display: flex;
    flex-direction: column;
    width: min(19rem, calc(100vw - 5rem));
  }

  .maps-leadership-locations-control__title {
    color: #57606a;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 0.45rem 0.6rem 0.2rem;
    text-transform: uppercase;
  }

  .maps-leadership-locations-control__row {
    align-items: flex-start;
    cursor: pointer;
    display: flex;
    gap: 0.4rem;
    padding: 0.35rem 0.6rem;
  }

  .maps-leadership-locations-control__row input {
    flex: 0 0 auto;
    margin: 0.2rem 0 0;
  }

  .maps-leadership-location-popup address {
    font-style: normal;
    margin: 0.35rem 0 0;
  }

  .maps-leadership-location-popup .maps-leadership-location-popup__date {
    margin-top: 0;
  }

  .maps-leadership-location-popup .maps-leadership-location-popup__directions {
    margin-top: 0.65rem;
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

  .maps-layer-heading--terrain-hazards {
    margin-bottom: 0.15rem;
  }

  .leaflet-control-layers-overlays > .maps-layer-heading:first-child {
    border-top: 0;
    margin-top: 0;
    padding-top: 0;
  }

  .leaflet-control-layers-overlays > .maps-location-info-header + .maps-layer-heading {
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

  .maps-layer-accordion {
    margin: 0.35rem 0 0;
  }

  .maps-layer-accordion > summary {
    color: #57606a;
    cursor: pointer;
    font-size: 0.78rem;
    font-weight: 700;
  }

  .maps-layer-accordion__body {
    margin: 0.2rem 0 0;
  }

  .maps-layer-group-row {
    display: grid;
    gap: 0.3rem;
    grid-template-columns: minmax(9rem, 1fr) auto;
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

  .maps-location-info-header {
    align-items: center;
    color: #57606a;
    display: none;
    font-size: 0.78rem;
    font-weight: 700;
    gap: 0.3rem;
    grid-template-columns: minmax(9rem, 1fr) auto;
    margin-top: 0.35rem;
  }

  .maps-layers-control.has-user-location .maps-location-info-header {
    display: grid;
  }

  .maps-location-info-column {
    display: none;
    justify-self: end;
  }

  .maps-layers-control.has-user-location .maps-location-info-column {
    display: inline-flex;
  }

  .maps-location-info-icon {
    align-items: center;
    display: inline-flex;
    height: 14px;
    justify-content: center;
    width: 14px;
  }

  .maps-location-info-icon svg {
    display: block;
    fill: currentColor;
    height: 14px;
    width: 14px;
  }

  .maps-you-are-here-section {
    border-top: 1px solid #d0d7de;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
  }

  .maps-you-are-here-section:first-of-type {
    border-top: 0;
    margin-top: 0.35rem;
    padding-top: 0;
  }

  .maps-you-are-here-actions {
    border-top: 1px solid #d0d7de;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
  }

  .maps-layer-reference-link {
    color: inherit;
    text-decoration-color: currentColor;
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

  .maps-layers-control.is-open,
  .maps-pinned-card-panel {
    max-height: var(--maps-open-control-max-height, var(--maps-control-panel-max-height));
  }

  .maps-basemap-control.is-open {
    max-height: var(--maps-open-control-max-height, var(--maps-control-panel-max-height));
  }

  .maps-layers-control .maps-layer-opacity-control,
  .maps-basemap-control .maps-layer-opacity-control {
    align-items: center;
    display: flex;
    flex: 1 1 1rem;
    height: 30px;
    justify-content: center;
    min-width: 5rem;
    position: relative;
  }

  .maps-layers-control .maps-layer-opacity-control::after,
  .maps-basemap-control .maps-layer-opacity-control::after {
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

  .maps-basemap-control:not(.is-open) .maps-basemap-header-actions {
    display: none;
  }

  .maps-layer-header-actions,
  .maps-basemap-header-actions {
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
    min-height: 0;
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

  /* Keep boundary strokes at their final screen width during Leaflet's
     temporary SVG scale so they do not appear to zoom again on redraw. */
  #ray-map .leaflet-pane > svg path {
    vector-effect: non-scaling-stroke;
  }

  /* Smooth-wheel zoom already supplies every intermediate transform. Do not
     let Leaflet's 250ms discrete-zoom transition replay the final SVG scale. */
  #ray-map.maps-smooth-wheel-zooming .leaflet-pane > svg.leaflet-zoom-animated,
  #ray-map.maps-smooth-wheel-zooming .leaflet-elevation-pane .leaflet-zoom-animated {
    transition: none;
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

  .maps-elevation-legend {
    background: rgba(255, 255, 255, 0.94);
    border-radius: 4px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0.4);
    color: #24292f;
    display: none;
    font-size: 0.72rem;
    line-height: 1.2;
    padding: 0.45rem 0.55rem;
  }

  .maps-elevation-legend.is-visible {
    display: block;
  }

  .maps-elevation-legend strong {
    display: block;
    margin-bottom: 0.3rem;
  }

  .maps-elevation-legend__row {
    align-items: center;
    display: flex;
    gap: 0.35rem;
    margin-top: 0.12rem;
  }

  .maps-elevation-legend__swatch {
    border: 1px solid rgba(0, 0, 0, 0.2);
    display: inline-block;
    height: 0.65rem;
    width: 0.9rem;
  }

  .maps-historic-placement-handle {
    align-items: center;
    background: #fff;
    border: 2px solid #0969da;
    box-shadow: 0 1px 4px rgb(27 31 36 / 35%);
    box-sizing: border-box;
    cursor: nwse-resize;
    display: flex;
    height: 16px;
    justify-content: center;
    width: 16px;
  }

  .maps-historic-placement-handle--move {
    background: #0969da;
    border-color: #fff;
    border-radius: 50%;
    color: #fff;
    cursor: move;
    font-size: 11px;
    height: 22px;
    line-height: 1;
    width: 22px;
  }

  .maps-historic-placement-handle--rotate {
    background: #fff;
    border-color: #0969da;
    border-radius: 50%;
    color: #0969da;
    cursor: grab;
    font-size: 16px;
    font-weight: 700;
    height: 22px;
    line-height: 1;
    width: 22px;
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

  .maps-user-location-icon {
    background: transparent;
    border: 0;
  }

  .maps-user-location-marker {
    height: 88px;
    position: relative;
    width: 88px;
  }

  .maps-user-location-marker__heading {
    height: 88px;
    left: 0;
    opacity: 0;
    position: absolute;
    top: 0;
    transform: rotate(var(--maps-user-map-bearing, 0deg));
    transform-origin: 44px 44px;
    width: 88px;
  }

  .maps-user-location-marker.has-heading .maps-user-location-marker__heading {
    opacity: 1;
  }

  .maps-user-location-marker__heading svg {
    display: block;
    filter: blur(0.35px);
    height: 88px;
    transform: rotate(var(--maps-user-heading, 0deg));
    transform-origin: 44px 44px;
    transition: transform 250ms ease-out;
    width: 88px;
  }

  .maps-user-location-marker__dot {
    background: #146ff5;
    border: 6px solid #fff;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgb(0 0 0 / 42%);
    box-sizing: border-box;
    height: 32px;
    left: 28px;
    position: absolute;
    top: 28px;
    width: 32px;
  }

  .maps-polling-location-pointer-icon {
    background: transparent;
    border: 0;
  }

  .maps-polling-location-pointer {
    background: #7c3aed;
    border: 3px solid #fff;
    border-radius: 50% 50% 50% 0;
    box-shadow: 0 2px 6px rgb(0 0 0 / 45%);
    box-sizing: border-box;
    display: block;
    height: 28px;
    position: relative;
    transform: rotate(-45deg);
    width: 28px;
  }

  .maps-polling-location-pointer::after {
    background: #fff;
    border-radius: 50%;
    content: "";
    height: 8px;
    left: 7px;
    position: absolute;
    top: 7px;
    width: 8px;
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

    .maps-control-panel__body {
      max-height: calc(var(--maps-control-panel-max-height) - var(--maps-control-panel-header-height));
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
<script src="/leaflet/imageoverlay-rotated/Leaflet.ImageOverlay.Rotated.js"></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet-rotate@0.2.8/dist/leaflet-rotate-src.js"></script>
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
    const Leaflet = L;
    const RayRotatedImageOverlay = Leaflet.RayRotatedImageOverlay;
    const initialMapParams = new URLSearchParams(window.location.search);
    const defaultMapCenter = [30.3322, -81.6557];
    const defaultMapZoom = 11;
    const requestedLatitude = initialMapParams.has("lat") ? Number(initialMapParams.get("lat")) : NaN;
    const requestedLongitude = initialMapParams.has("lng") ? Number(initialMapParams.get("lng")) : NaN;
    const requestedZoom = initialMapParams.has("zoom") ? Number(initialMapParams.get("zoom")) : NaN;
    const requestedRotation = initialMapParams.has("rotation") ? Number(initialMapParams.get("rotation")) : NaN;
    const hasRequestedMapCoordinates = Number.isFinite(requestedLatitude) && requestedLatitude >= -85.051129 && requestedLatitude <= 85.051129 &&
      Number.isFinite(requestedLongitude) && requestedLongitude >= -180 && requestedLongitude <= 180;
    const initialMapCenter = hasRequestedMapCoordinates
      ? [requestedLatitude, requestedLongitude]
      : defaultMapCenter;
    const initialMapZoom = Number.isFinite(requestedZoom)
      ? Math.max(4, Math.min(20, requestedZoom))
      : defaultMapZoom;
    const initialMapRotation = Number.isFinite(requestedRotation)
      ? ((requestedRotation % 360) + 360) % 360
      : 0;
    const map = Leaflet.map("ray-map", {
      minZoom: 4,
      maxZoom: 20,
      maxBounds: [[-85.051129, -Infinity], [85.051129, Infinity]],
      maxBoundsViscosity: 1,
      zoomControl: false,
      scrollWheelZoom: false,
      smoothWheelZoom: true,
      smoothSensitivity: 1,
      zoomSnap: 0,
      zoomAnimationThreshold: 1,
      rotate: true,
      rotateControl: {
        closeOnZeroBearing: false,
        position: "topleft"
      },
      touchRotate: true,
      bearing: initialMapRotation,
      fullscreenControl: false
    }).setView(initialMapCenter, initialMapZoom);
    const mapLibrePane = map.createPane("mapLibrePane", map.getContainer());
    mapLibrePane.style.zIndex = "0";
    map._mapPane.style.zIndex = "1";
    const historicMapsPane = map.createPane("historicMapsPane", map._norotatePane);
    historicMapsPane.style.zIndex = "350";
    const elevationPane = map.createPane("elevationPane", map._rotatePane);
    elevationPane.style.pointerEvents = "none";
    elevationPane.style.zIndex = "250";
    const historicPlacementPane = map.createPane("historicPlacementPane", map._rotatePane);
    historicPlacementPane.style.zIndex = "350";
    const navigationMarkerPane = map.createPane("navigationMarkerPane", map._norotatePane);
    navigationMarkerPane.style.zIndex = "750";
    const pollingLocationPointerPane = map.createPane("pollingLocationPointerPane", map._norotatePane);
    pollingLocationPointerPane.style.pointerEvents = "none";
    pollingLocationPointerPane.style.zIndex = "850";

    let mapQueryUpdateTimer;

    function formatMapQueryNumber(value, decimalPlaces) {
      return String(Number(value.toFixed(decimalPlaces)));
    }

    function updateMapViewQueryUrl() {
      const center = map.getCenter();
      const zoom = map.getZoom();
      const bearing = Number.isFinite(map.getBearing()) ? map.getBearing() : 0;
      const normalizedBearing = ((bearing % 360) + 360) % 360;
      const url = new URL(window.location.href);
      url.searchParams.set("lat", formatMapQueryNumber(center.lat, 6));
      url.searchParams.set("lng", formatMapQueryNumber(center.lng, 6));
      url.searchParams.set("zoom", formatMapQueryNumber(zoom, 2));
      url.searchParams.set("rotation", formatMapQueryNumber(normalizedBearing, 1));
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function scheduleMapViewQueryUpdate() {
      window.clearTimeout(mapQueryUpdateTimer);
      mapQueryUpdateTimer = window.setTimeout(updateMapViewQueryUrl, 120);
    }

    map.on("moveend zoomend", scheduleMapViewQueryUpdate);
    map.on("rotate", scheduleMapViewQueryUpdate);
    window.requestAnimationFrame(updateMapViewQueryUrl);

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
    const createMapLibreLayer = typeof L.maplibreGL === "function"
      ? L.maplibreGL.bind(L)
      : null;
    const defaultBaseMapKey = "positron";
    let activeBaseMapKey = defaultBaseMapKey;
    let baseMapControlElement;
    let baseMapLayer;
    let baseMapOpacityInput;
    let baseMapOpacityLabel;
    let baseMapTileOpacity = 1;
    let baseMapRequestId = 0;
    const defaultHistoricMapOpacity = 1;
    let historicMapOpacity = defaultHistoricMapOpacity;
    let historicMapOpacityInput;
    let historicMapOpacityLabel;
    let zoomHomeControl;
    const censusReporterGeographyPromises = new Map();
    const squareMetersPerSquareMile = 2589988.110336;
    const supportsPointerHover = window.matchMedia
      ? window.matchMedia("(hover: hover) and (pointer: fine)").matches
      : true;

    function addModifierDragRotation() {
      const container = map.getContainer();
      let activePointerId = null;
      let startingBearing = 0;
      let startingX = 0;

      container.addEventListener("pointerdown", function (event) {
        if (!event.metaKey || event.button !== 0 || event.target.closest(".leaflet-control")) return;
        activePointerId = event.pointerId;
        startingBearing = map.getBearing();
        startingX = event.clientX;
        map.dragging.disable();
        container.classList.add("maps-modifier-rotating");
        container.setPointerCapture(activePointerId);
        event.preventDefault();
        event.stopPropagation();
      }, true);

      container.addEventListener("pointermove", function (event) {
        if (event.pointerId !== activePointerId) return;
        map.setBearing(startingBearing + ((event.clientX - startingX) * 0.4));
        event.preventDefault();
        event.stopPropagation();
      }, true);

      function stopModifierDragRotation(event) {
        if (event.pointerId !== activePointerId) return;
        if (container.hasPointerCapture(activePointerId)) {
          container.releasePointerCapture(activePointerId);
        }
        activePointerId = null;
        container.classList.remove("maps-modifier-rotating");
        map.dragging.enable();
        event.preventDefault();
        event.stopPropagation();
      }

      container.addEventListener("pointerup", stopModifierDragRotation, true);
      container.addEventListener("pointercancel", stopModifierDragRotation, true);
    }

    function createBearingAwareMapLibreLayer(options) {
      const layer = createMapLibreLayer({
        ...options,
        pane: "mapLibrePane",
        padding: 0
      });

      layer._resizeContainer = function () {
        if (!this._container || !this._map) return;
        const size = this._map.getSize();
        this._container.style.width = `${size.x}px`;
        this._container.style.height = `${size.y}px`;
      };

      layer._initContainer = function () {
        this._container = L.DomUtil.create("div", "leaflet-gl-layer maps-maplibre-bearing-layer");
        this._resizeContainer();
        L.DomUtil.setPosition(this._container, L.point(0, 0));
      };

      layer._transformGL = function (gl, view) {
        const target = view || {};
        const center = target.center || this._map.getCenter();
        const zoom = Number.isFinite(target.zoom) ? target.zoom : this._map.getZoom();
        gl.jumpTo({
          center: [center.lng, center.lat],
          zoom: zoom - 1,
          // Leaflet Rotate applies positive angles clockwise in screen space;
          // MapLibre bearings rotate the rendered map in the opposite direction.
          bearing: -this._map.getBearing()
        });
      };

      layer._update = function () {
        if (!this._map || !this._glMap) return;
        this._resizeContainer();
        L.DomUtil.setPosition(this._container, L.point(0, 0));
        this._transformGL(this._glMap);
      };

      layer._animateZoom = function (event) {
        if (!this._glMap) return;
        this._transformGL(this._glMap, event);
      };

      layer._pinchZoom = layer._animateZoom;
      layer._zoomStart = function () {};
      layer._zoomEnd = function () {
        this._update();
      };
      layer._transitionEnd = function () {
        this._update();
      };
      layer._resize = function () {
        this._resizeContainer();
        if (this._glMap) this._glMap.resize();
        this._update();
      };
      layer._throttledUpdate = L.Util.throttle(layer._update, layer.options.updateInterval, layer);

      const originalGetEvents = layer.getEvents;
      layer.getEvents = function () {
        return {
          ...originalGetEvents.call(this),
          rotate: this._throttledUpdate
        };
      };

      return layer;
    }

    function getBaseMapQueryKey() {
      const requestedBaseMap = new URLSearchParams(window.location.search).get("basemap");
      return Object.prototype.hasOwnProperty.call(baseMapStyles, requestedBaseMap)
        ? requestedBaseMap
        : defaultBaseMapKey;
    }

    function updateBaseMapQueryUrl() {
      const url = new URL(window.location.href);
      url.searchParams.set("basemap", activeBaseMapKey);
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    async function setBaseMap(baseMapKey, options) {
      const config = baseMapStyles[baseMapKey];
      const settings = options || {};
      const requestId = ++baseMapRequestId;
      if (!config) return false;
      if (config.type !== "tile" && (!window.maplibregl || !createMapLibreLayer || /HeadlessChrome/.test(window.navigator.userAgent) || (maplibregl.supported && !maplibregl.supported({ failIfMajorPerformanceCaveat: true })))) {
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
        baseMapLayer = createBearingAwareMapLibreLayer({
          style: nextStyle
        }).addTo(map);
      }
      activeBaseMapKey = baseMapKey;
      applyBaseMapTileOpacity();
      updateBaseMapControl();
      if (settings.updateUrl !== false) {
        updateBaseMapQueryUrl();
      }
      return true;
    }

    function getBaseMapLayerContainer() {
      if (!baseMapLayer) return null;
      if (baseMapLayer.getContainer) {
        return baseMapLayer.getContainer();
      }
      return baseMapLayer._container || null;
    }

    function applyBaseMapTileOpacity() {
      if (!baseMapLayer) return;
      if (baseMapLayer.setOpacity) {
        baseMapLayer.setOpacity(baseMapTileOpacity);
      }
      const container = getBaseMapLayerContainer();
      if (container) {
        container.style.opacity = String(baseMapTileOpacity);
      }
    }

    function refreshActiveBaseMap() {
      if (baseMapStyles[activeBaseMapKey] && baseMapStyles[activeBaseMapKey].type !== "tile") {
        setBaseMap(activeBaseMapKey, { quiet: true, updateUrl: false });
      }
    }

    function updateBaseMapControl() {
      if (!baseMapControlElement) return;
      baseMapControlElement.querySelectorAll("button[data-base-map]").forEach((button) => {
        const key = button.dataset.baseMap;
        button.setAttribute("aria-pressed", String(key === activeBaseMapKey));
      });
    }

    function setBaseMapTileOpacity(value) {
      baseMapTileOpacity = Math.max(0, Math.min(1, Number.isFinite(value) ? value : 1));
      applyBaseMapTileOpacity();
      updateBaseMapTileOpacityControl();
    }

    function updateOpacityRangeVisual(input, label, opacity, labelText) {
      const opacityPercent = Math.round(opacity * 100);
      const thumbBorderChannel = Math.round(opacity * 255);
      const opacityFillChannel = Math.round(255 - ((255 - 66) * opacity));
      const title = `${labelText}: ${opacityPercent}%`;

      if (input) {
        input.value = String(opacityPercent);
        input.title = title;
        input.style.setProperty("--maps-layer-opacity-alpha", String(opacity));
        input.style.setProperty("--maps-layer-opacity-fill-color", `rgb(${opacityFillChannel} ${opacityFillChannel} ${opacityFillChannel})`);
        input.style.setProperty("--maps-layer-opacity-percent", `${opacityPercent}%`);
        input.style.setProperty("--maps-layer-thumb-border-color", `rgb(${thumbBorderChannel} ${thumbBorderChannel} ${thumbBorderChannel})`);
      }
      if (label) {
        label.title = title;
      }
    }

    function updateBaseMapTileOpacityControl() {
      updateOpacityRangeVisual(baseMapOpacityInput, baseMapOpacityLabel, baseMapTileOpacity, "Map tile opacity");
    }

    function updateHistoricMapOpacityControl() {
      updateOpacityRangeVisual(historicMapOpacityInput, historicMapOpacityLabel, historicMapOpacity, "Historic map opacity");
    }

    function updateHistoricMapOpacityQueryUrl() {
      const url = new URL(window.location.href);
      url.searchParams.set("hm-opacity", String(Math.round(historicMapOpacity * 100)));
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function setHistoricMapOpacity(value, options) {
      const settings = options || {};
      historicMapOpacity = Math.max(0, Math.min(1, Number.isFinite(value) ? value : defaultHistoricMapOpacity));
      historicMapLayers.forEach((layer) => layer.setOpacity(historicMapOpacity));
      updateHistoricMapOpacityControl();
      if (settings.updateUrl) {
        updateHistoricMapOpacityQueryUrl();
      }
    }

    function createHistoricMapOpacityControl() {
      const opacityLabel = document.createElement("label");
      const opacityInput = document.createElement("input");

      opacityLabel.className = "maps-layer-opacity-control maps-historic-map-opacity-control";
      opacityInput.type = "range";
      opacityInput.min = "0";
      opacityInput.max = "100";
      opacityInput.step = "1";
      opacityInput.setAttribute("aria-label", "Historic map opacity");
      opacityInput.addEventListener("input", function () {
        setHistoricMapOpacity(Number(opacityInput.value) / 100, { updateUrl: true });
      });
      opacityLabel.appendChild(opacityInput);
      historicMapOpacityInput = opacityInput;
      historicMapOpacityLabel = opacityLabel;
      updateHistoricMapOpacityControl();
      return opacityLabel;
    }

    function setupCollapsibleMapControl(container, label, body, options) {
      const toggle = document.createElement("button");
      const settings = options || {};
      const headerAction = settings.headerAction || null;
      let header = null;

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

      function updateViewportMaxHeight() {
        if (!container.classList.contains("is-open")) return;
        const mapBounds = map.getContainer().getBoundingClientRect();
        const controlBounds = container.getBoundingClientRect();
        const availableHeight = Math.max(70, Math.floor(mapBounds.bottom - controlBounds.top - 10));
        container.style.setProperty("--maps-open-control-max-height", `${availableHeight}px`);
      }

      function setOpen(open) {
        container.classList.toggle("is-open", open);
        toggle.setAttribute("aria-expanded", String(open));
        if (open) {
          window.requestAnimationFrame(updateViewportMaxHeight);
        } else {
          container.style.removeProperty("--maps-open-control-max-height");
        }
      }

      toggle.addEventListener("click", function () {
        setOpen(!container.classList.contains("is-open"));
      });
      document.addEventListener("click", function (event) {
        if (container.classList.contains("is-open") && !container.contains(event.target)) {
          setOpen(false);
        }
      });
      window.addEventListener("resize", updateViewportMaxHeight);
      map.on("resize", updateViewportMaxHeight);
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
          body.appendChild(createLayerSubheading("Historic Maps"));
          body.appendChild(createHistoricMapOpacityControl());
          historicMapDefinitions.forEach((definition) => {
            const historicMapControl = createBoundaryLayerInput(
              definition.label,
              definition.layer,
              { countable: false, geometryType: "polygon", querySlug: definition.slug }
            );
            historicMapControl.input.checked = map.hasLayer(definition.layer);
            body.appendChild(historicMapControl.labelElement);
          });
          controlApi = setupCollapsibleMapControl(container, "Basemap", body, {
            headerAction: createBaseMapHeaderActions(),
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

    function createDirectionsLink(label, href) {
      const link = document.createElement("a");
      link.href = href;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = label;
      return link;
    }

    function createLeadershipLocationPopup(location) {
      const popup = document.createElement("div");
      const date = document.createElement("span");
      const title = document.createElement("strong");
      const address = document.createElement("address");
      const directionsLabel = document.createElement("strong");
      const destination = `${location.lat},${location.lng}`;

      popup.className = "maps-district-popup maps-leadership-location-popup";
      date.className = "maps-leadership-location-popup__date";
      date.textContent = location.displayDate;
      title.textContent = location.name;
      location.addressLines.forEach((line, index) => {
        if (index) address.appendChild(document.createElement("br"));
        address.appendChild(document.createTextNode(line));
      });
      directionsLabel.className = "maps-leadership-location-popup__directions";
      directionsLabel.textContent = "Get Directions:";

      popup.appendChild(date);
      popup.appendChild(title);
      popup.appendChild(address);
      popup.appendChild(directionsLabel);
      popup.appendChild(createDirectionsLink("Google Maps", `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(destination)}`));
      popup.appendChild(createDirectionsLink("Apple Maps", `https://maps.apple.com/?daddr=${encodeURIComponent(destination)}&dirflg=d`));
      popup.appendChild(createDirectionsLink("Waze Maps", `https://www.waze.com/ul?ll=${encodeURIComponent(destination)}&navigate=yes`));
      return popup;
    }

    function getLeadershipLocationQueryIds() {
      const params = new URLSearchParams(window.location.search);
      return params.getAll("lj")
        .flatMap((value) => String(value).split(","))
        .map((value) => Number.parseInt(value, 10))
        .filter((value) => Number.isInteger(value));
    }

    function updateLeadershipLocationQueryUrl(markers) {
      const url = new URL(window.location.href);
      const queryIds = markers
        .filter(({ input }) => input.checked)
        .map(({ location }) => location.queryId)
        .sort((first, second) => first - second);

      url.searchParams.delete("lj");
      if (queryIds.length) {
        url.searchParams.set("lj", queryIds.join(","));
      }
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function activateLeadershipLocationQuery(markers) {
      const queryIds = getLeadershipLocationQueryIds();
      const activeMarkers = markers
        .filter(({ location, marker, input }) => {
          if (!queryIds.includes(location.queryId)) return false;
          input.checked = true;
          leadershipJaxLocationsLayer.addLayer(marker);
          return true;
        })
        .sort((first, second) => second.location.queryId - first.location.queryId);
      if (!activeMarkers.length) return;

      initialVisibleLayerFitComplete = true;
      if (activeMarkers.length === 1) {
        map.setView(activeMarkers[0].marker.getLatLng(), 15);
      } else {
        const bounds = L.latLngBounds(activeMarkers.map(({ marker }) => marker.getLatLng()));
        map.fitBounds(bounds, { padding: [32, 32] });
      }
      orderMapLayers();
      activeMarkers[0].marker.openPopup();
    }

    function addLeadershipJaxLocationsControl() {
      const markers = leadershipJaxLocations.map((location) => {
        const marker = L.marker([location.lat, location.lng], {
          title: `${location.displayDate} - ${location.name}`
        });
        marker.bindPopup(createLeadershipLocationPopup(location));
        return { location, marker, input: null };
      });

      const LeadershipLocationsControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "maps-leadership-locations-control leaflet-bar leaflet-control");
          const body = document.createElement("div");
          const title = document.createElement("div");

          title.className = "maps-leadership-locations-control__title";
          title.textContent = "LJ Training Locations";
          body.appendChild(title);
          markers.forEach((markerConfig) => {
            const { location, marker } = markerConfig;
            const row = document.createElement("label");
            const input = document.createElement("input");
            const name = document.createElement("span");

            row.className = "maps-leadership-locations-control__row";
            input.type = "checkbox";
            input.className = "leaflet-control-layers-selector";
            input.dataset.leadershipLocation = location.name;
            markerConfig.input = input;
            name.textContent = location.menuLabel;
            input.addEventListener("change", function () {
              if (input.checked) {
                leadershipJaxLocationsLayer.addLayer(marker);
              } else {
                leadershipJaxLocationsLayer.removeLayer(marker);
              }
              orderMapLayers();
              updateLeadershipLocationQueryUrl(markers);
            });
            row.appendChild(input);
            row.appendChild(name);
            body.appendChild(row);
          });
          container.appendChild(body);
          setupCollapsibleMapControl(container, "LJ Training Locations", body, {
            iconPath: "M160 64C124.7 64 96 92.7 96 128L96 512C96 547.3 124.7 576 160 576L480 576C515.3 576 544 547.3 544 512L544 128C544 92.7 515.3 64 480 64L416 64C416 28.7 387.3 0 352 0L288 0C252.7 0 224 28.7 224 64L160 64zM288 48L352 48C360.8 48 368 55.2 368 64L368 96L272 96L272 64C272 55.2 279.2 48 288 48zM208 192L432 192C445.3 192 456 202.7 456 216C456 229.3 445.3 240 432 240L208 240C194.7 240 184 229.3 184 216C184 202.7 194.7 192 208 192zM208 288L432 288C445.3 288 456 298.7 456 312C456 325.3 445.3 336 432 336L208 336C194.7 336 184 325.3 184 312C184 298.7 194.7 288 208 288zM208 384L336 384C349.3 384 360 394.7 360 408C360 421.3 349.3 432 336 432L208 432C194.7 432 184 421.3 184 408C184 394.7 194.7 384 208 384z"
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          activateLeadershipLocationQuery(markers);
          return container;
        }
      });

      map.addControl(new LeadershipLocationsControl());
    }

    function createBaseMapHeaderActions() {
      const wrapper = document.createElement("div");
      const opacityLabel = document.createElement("label");
      const opacityInput = document.createElement("input");

      wrapper.className = "maps-basemap-header-actions";
      opacityLabel.className = "maps-layer-opacity-control maps-basemap-opacity-control";
      opacityInput.type = "range";
      opacityInput.min = "0";
      opacityInput.max = "100";
      opacityInput.step = "1";
      opacityInput.setAttribute("aria-label", "Map tile opacity");
      opacityInput.addEventListener("input", function () {
        setBaseMapTileOpacity(Number(opacityInput.value) / 100);
      });
      opacityLabel.appendChild(opacityInput);
      wrapper.appendChild(opacityLabel);
      baseMapOpacityInput = opacityInput;
      baseMapOpacityLabel = opacityLabel;
      updateBaseMapTileOpacityControl();
      return wrapper;
    }

    let userAccuracyCircle;
    let userHeading;
    let userHeadingDisplayRotation;
    let userHeadingTrackingStarted = false;
    let userLocationMarker;
    let userLocationLatLng;
    let locateControlContainer;
    let locateControlIcon;
    let locateControlLink;
    let locateShouldSetInitialView = false;
    let showYouAreHereCardWhenLocated = false;
    let userLocationTrackingActive = false;
    let layersControlApi;
    let layersControlElement;
    const locationInfoControls = [];
    const selectedLocationInfoLayerTypes = new Set([
      "votingPrecinct",
      "district",
      "atLarge",
      "schoolBoard",
      "floridaHouse",
      "floridaSenate",
      "congressional",
      "usSenate"
    ]);

    function isMobileLocationHeadingEnabled() {
      return window.matchMedia && window.matchMedia("(max-width: 760px)").matches;
    }

    function getScreenOrientationAngle() {
      if (window.screen && window.screen.orientation && Number.isFinite(window.screen.orientation.angle)) {
        return window.screen.orientation.angle;
      }
      return Number.isFinite(window.orientation) ? window.orientation : 0;
    }

    function updateUserLocationHeadingMarker() {
      if (!userLocationMarker || !Number.isFinite(userHeading)) return;
      const markerElement = userLocationMarker.getElement();
      const headingElement = markerElement && markerElement.querySelector(".maps-user-location-marker");
      if (!headingElement) return;
      const mapBearing = Number.isFinite(map.getBearing()) ? map.getBearing() : 0;
      if (Number.isFinite(userHeadingDisplayRotation)) {
        const shortestTurn = ((userHeading - userHeadingDisplayRotation + 540) % 360) - 180;
        userHeadingDisplayRotation += shortestTurn;
      } else {
        userHeadingDisplayRotation = userHeading;
      }
      headingElement.classList.add("has-heading");
      headingElement.style.setProperty("--maps-user-map-bearing", `${mapBearing}deg`);
      headingElement.style.setProperty("--maps-user-heading", `${userHeadingDisplayRotation}deg`);
    }

    map.on("rotate", updateUserLocationHeadingMarker);

    function handleDeviceOrientation(event) {
      let heading;
      if (Number.isFinite(event.webkitCompassHeading)) {
        heading = event.webkitCompassHeading;
      } else if (event.absolute && Number.isFinite(event.alpha)) {
        heading = 360 - event.alpha + getScreenOrientationAngle();
      }
      if (!Number.isFinite(heading)) return;
      userHeading = ((heading % 360) + 360) % 360;
      updateUserLocationHeadingMarker();
    }

    function startMobileLocationHeading() {
      if (!isMobileLocationHeadingEnabled() || userHeadingTrackingStarted || typeof window.DeviceOrientationEvent === "undefined") {
        return;
      }

      function addHeadingListeners() {
        if (!userLocationTrackingActive || userHeadingTrackingStarted) return;
        userHeadingTrackingStarted = true;
        window.addEventListener("deviceorientationabsolute", handleDeviceOrientation, true);
        window.addEventListener("deviceorientation", handleDeviceOrientation, true);
      }

      if (typeof window.DeviceOrientationEvent.requestPermission === "function") {
        window.DeviceOrientationEvent.requestPermission()
          .then((permission) => {
            if (permission === "granted") addHeadingListeners();
          })
          .catch(() => {});
      } else {
        addHeadingListeners();
      }
    }

    function stopMobileLocationHeading() {
      window.removeEventListener("deviceorientationabsolute", handleDeviceOrientation, true);
      window.removeEventListener("deviceorientation", handleDeviceOrientation, true);
      userHeadingTrackingStarted = false;
      userHeading = undefined;
      userHeadingDisplayRotation = undefined;
    }

    function createUserLocationIcon() {
      return L.divIcon({
        className: "maps-user-location-icon",
        html: '<div class="maps-user-location-marker"><div class="maps-user-location-marker__heading"><svg viewBox="0 0 88 88" aria-hidden="true"><defs><linearGradient id="maps-user-heading-gradient" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="rgb(20, 111, 245)" stop-opacity="0.3"/><stop offset="1" stop-color="rgb(92, 92, 246)" stop-opacity="0"/></linearGradient></defs><path fill="url(#maps-user-heading-gradient)" d="M44 44 L20 0 H68 Z"/></svg></div><span class="maps-user-location-marker__dot"></span></div>',
        iconAnchor: [44, 44],
        iconSize: [88, 88],
        popupAnchor: [0, -22]
      });
    }

    function updateLocateControlLabel() {
      if (!locateControlLink) return;
      const label = userLocationTrackingActive ? "Stop navigation" : "Show me where I am";
      locateControlLink.title = label;
      locateControlLink.setAttribute("aria-label", label);
      locateControlLink.setAttribute("aria-pressed", String(userLocationTrackingActive));
    }

    function startUserLocationTracking() {
      userLocationTrackingActive = true;
      updateLocateControlLabel();
      startMobileLocationHeading();
      if (locateControlContainer) {
        L.DomUtil.addClass(locateControlContainer, "requesting");
        L.DomUtil.removeClass(locateControlContainer, "active");
        L.DomUtil.removeClass(locateControlContainer, "following");
      }
      if (locateControlIcon) {
        L.DomUtil.removeClass(locateControlIcon, "leaflet-control-locate-location-arrow");
        L.DomUtil.addClass(locateControlIcon, "leaflet-control-locate-spinner");
      }
      locateShouldSetInitialView = true;
      map.stopLocate();
      map.locate({
        enableHighAccuracy: true,
        setView: false,
        watch: true
      });
    }

    function stopUserLocationTracking() {
      userLocationTrackingActive = false;
      locateShouldSetInitialView = false;
      showYouAreHereCardWhenLocated = false;
      map.stopLocate();
      stopMobileLocationHeading();
      if (userLocationMarker) {
        map.removeLayer(userLocationMarker);
        userLocationMarker = undefined;
      }
      if (userAccuracyCircle) {
        map.removeLayer(userAccuracyCircle);
        userAccuracyCircle = undefined;
      }
      userLocationLatLng = undefined;
      const userLocationCardIndex = pinnedBoundaryCards.findIndex((card) => card.layerType === "userLocation");
      if (userLocationCardIndex >= 0) {
        pinnedBoundaryCards.splice(userLocationCardIndex, 1);
        renderPinnedCards();
      }
      updateLocationInfoControlVisibility();
      setLocateControlState();
      const url = new URL(window.location.href);
      url.searchParams.delete("locate");
      url.searchParams.delete("navigation");
      url.searchParams.delete("nav");
      url.searchParams.delete("yah");
      window.history.replaceState(window.history.state, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function activateLocateQuery() {
      const params = new URLSearchParams(window.location.search);
      const locateRequested = String(params.get("locate") || "").trim().toLowerCase() === "yes";
      const navigationRequested = ["navigation", "nav"].some((name) => (
        String(params.get(name) || "").trim().toLowerCase() === "yes"
      ));
      const youAreHereRequested = String(params.get("yah") || "").trim().toLowerCase() === "yes";
      if (!locateRequested && !navigationRequested && !youAreHereRequested) return;
      showYouAreHereCardWhenLocated = youAreHereRequested;
      startUserLocationTracking();
    }

    function addLocateControl() {
      const LocateControl = L.Control.extend({
        options: {
          position: "bottomright"
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
            if (userLocationTrackingActive) {
              stopUserLocationTracking();
            } else {
              startUserLocationTracking();
            }
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          locateControlContainer = container;
          locateControlIcon = icon;
          locateControlLink = link;
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
      updateLocateControlLabel();
    }

    function isLocalGeolocationBlocked(error) {
      const message = error && error.message ? error.message : "";
      return !window.isSecureContext && /secure origins/i.test(message);
    }

    function findContainingFeature(layerGroup, latLng) {
      let containingFeature;
      if (!layerGroup || !layerGroup.eachLayer || !latLng) return containingFeature;
      const point = [latLng.lng, latLng.lat];

      layerGroup.eachLayer((featureLayer) => {
        if (containingFeature || !featureLayer.feature) return;
        if (isPointInFeatureGeometry(point, featureLayer.feature.geometry)) {
          containingFeature = featureLayer.feature;
        }
      });

      return containingFeature;
    }

    function updateLocationInfoControlVisibility() {
      if (layersControlElement) {
        layersControlElement.classList.toggle("has-user-location", Boolean(userLocationLatLng));
      }
      locationInfoControls.forEach((control) => {
        control.input.checked = selectedLocationInfoLayerTypes.has(control.layerType);
      });
    }

    function openLayersMenuForLocationInfo() {
      if (layersControlApi) {
        layersControlApi.setOpen(true);
      }
    }

    function createYouAreHereCard() {
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      const selectedControls = locationInfoControls
        .filter((control) => selectedLocationInfoLayerTypes.has(control.layerType))
        .sort((left, right) => {
          if (left.layerType === "votingPrecinct") return -1;
          if (right.layerType === "votingPrecinct") return 1;
          return 0;
        });

      popup.className = "maps-district-popup maps-you-are-here-card";
      title.textContent = "You are here";
      popup.appendChild(title);

      selectedControls.forEach((control) => {
        const feature = findContainingFeature(control.layer, userLocationLatLng);
        const contents = feature
          ? getLocationInfoCardContents(control, feature)
          : [document.createElement("div")];

        contents.forEach((content) => {
          const section = document.createElement("section");
          section.className = "maps-you-are-here-section";
          if (feature) {
            section.appendChild(content);
          } else {
            const missingLine = document.createElement("span");
            missingLine.textContent = `${control.label}: not found for this location`;
            section.appendChild(missingLine);
          }
          popup.appendChild(section);
        });
      });

      const actions = document.createElement("div");
      const link = document.createElement("a");
      actions.className = "maps-you-are-here-actions";
      link.href = "#";
      link.textContent = "Show other information";
      link.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        openLayersMenuForLocationInfo();
      });
      actions.appendChild(link);
      popup.appendChild(actions);

      return popup;
    }

    function getLocationInfoCardContents(control, feature) {
      if (control.layerType === "district") {
        return [createCouncilDistrictPopup(feature)];
      }
      if (control.layerType === "usSenate") {
        return createUsSenatorCards(feature.properties || {}, { prefixTitle: "Senator" });
      }
      return [createBoundaryPopup(feature, control.layerType)];
    }

    function updateYouAreHereCard() {
      updateLocationInfoControlVisibility();
      if (pinnedBoundaryCards.some((card) => card.layerType === "userLocation")) {
        renderPinnedCards();
      }
    }

    function showYouAreHereCardInPanel() {
      if (!userLocationLatLng) return;
      const existingCard = pinnedBoundaryCards.find((card) => card.layerType === "userLocation");
      if (!existingCard) {
        pinnedBoundaryCards.unshift({
          key: "userLocation",
          layerType: "userLocation",
          title: "You are here"
        });
      }
      renderPinnedCards();
    }

    map.on("locationfound", function (event) {
      if (locateShouldSetInitialView) {
        locateShouldSetInitialView = false;
        map.setView(event.latlng, Math.min(16, map.getMaxZoom()));
      }
      setLocateControlState("following");
      userLocationLatLng = event.latlng;
      updateLocationInfoControlVisibility();

      if (Number.isFinite(event.heading)) {
        userHeading = event.heading;
      }
      if (userLocationMarker) {
        userLocationMarker.setLatLng(event.latlng);
      } else {
        const markerOptions = {
          pane: "navigationMarkerPane",
          title: "Your location"
        };
        markerOptions.icon = createUserLocationIcon();
        userLocationMarker = L.marker(event.latlng, markerOptions)
          .addTo(map)
          .on("click", showYouAreHereCardInPanel);
      }
      updateUserLocationHeadingMarker();
      if (userAccuracyCircle) {
        userAccuracyCircle
          .setLatLng(event.latlng)
          .setRadius(event.accuracy || 0);
      } else {
        userAccuracyCircle = L.circle(event.latlng, {
          color: "#0969da",
          fillColor: "#0969da",
          fillOpacity: 0.12,
          radius: event.accuracy || 0,
          weight: 1
        }).addTo(map);
      }
      if (showYouAreHereCardWhenLocated) {
        showYouAreHereCardWhenLocated = false;
        showYouAreHereCardInPanel();
      }
    });

    map.on("locationerror", function (error) {
      userLocationTrackingActive = false;
      stopMobileLocationHeading();
      locateShouldSetInitialView = false;
      setLocateControlState();
      if (isLocalGeolocationBlocked(error)) {
        console.warn(error.message || "Geolocation requires HTTPS or localhost.");
        return;
      }
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

    function addAttributionToggleControl() {
      const AttributionToggleControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "leaflet-bar leaflet-control maps-attribution-toggle");
          const button = L.DomUtil.create("button", "", container);
          const mapContainer = map.getContainer();

          button.type = "button";
          button.textContent = "©";
          button.title = "Map credits and data sources";
          button.setAttribute("aria-label", "Show map credits and data sources");
          button.setAttribute("aria-expanded", "false");

          function setOpen(open) {
            mapContainer.classList.toggle("maps-attribution-expanded", open);
            button.textContent = open ? "×" : "©";
            button.title = open ? "Hide map credits and data sources" : "Map credits and data sources";
            button.setAttribute("aria-label", open ? "Hide map credits and data sources" : "Show map credits and data sources");
            button.setAttribute("aria-expanded", String(open));
          }

          button.addEventListener("click", function () {
            setOpen(!mapContainer.classList.contains("maps-attribution-expanded"));
          });
          map.on("click", function () {
            setOpen(false);
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          return container;
        }
      });

      map.addControl(new AttributionToggleControl());
    }

    addAttributionToggleControl();

    const markerIcon = window.L.ExtraMarkers ? L.ExtraMarkers.icon({
      icon: "fa-map-marker-alt",
      markerColor: "black",
      shape: "circle",
      prefix: "fas"
    }) : undefined;
    const leadershipJaxLocations = [
      {
        displayDate: "Thursday, 10/15/2026",
        menuLabel: "10/15/26 - Feeding Northeast Florida",
        name: "Feeding Northeast Florida",
        addressLines: ["5245 Old Kings Road", "Jacksonville, FL 32254"],
        lat: 30.364164280472675,
        lng: -81.73475699989007,
        queryId: 3
      },
      {
        displayDate: "Thursday, 9/17/2026",
        menuLabel: "9/17/26 - Ritz Theatre and Museum",
        name: "Ritz Theatre and Museum",
        addressLines: ["829 N. Davis Street", "Jacksonville, FL 32202"],
        lat: 30.335230069603266,
        lng: -81.66702419790622,
        queryId: 2
      },
      {
        displayDate: "Thursday, 8/13/2026 & Friday, 8/14/2026",
        menuLabel: "8/13/26 & 8/14/26 - LJ Opening Retreat",
        name: "LJ Opening Retreat",
        addressLines: ["World Golf Village Renaissance St. Augustine Resort", "500 S Legacy Trail", "St. Augustine, FL 32092, USA"],
        lat: 29.98996,
        lng: -81.46825,
        queryId: 1
      }
    ];
    const activePlaceLayer = L.layerGroup().addTo(map);
    const archivedPlaceLayer = L.layerGroup();
    const leadershipJaxLocationsLayer = L.layerGroup().addTo(map);
    const HistoricMapLayer = L.Layer.extend({
      initialize: function (annotationUrl, bounds, options) {
        const settings = options || {};
        this._annotationUrl = annotationUrl;
        this._bounds = L.latLngBounds(bounds);
        this._label = settings.label || "Historic map";
        this._localIiifPattern = settings.localIiifPattern || null;
        const attributionLabel = settings.attributionLabel || `Library of Congress, ${this._label} Sanborn Map`;
        const georeferenceCredit = settings.georeferenceCredit || '<a href="https://mapsnap.org/" target="_blank" rel="noopener">mapsnap</a>';
        this._attribution = `<a href="${settings.sourceUrl}" target="_blank" rel="noopener">${attributionLabel}</a> · Georeferencing: ${georeferenceCredit}`;
        this._loadRequest = 0;
        this._opacity = historicMapOpacity;
      },

      onAdd: function (targetMap) {
        this._map = targetMap;
        this._loadRequest += 1;
        const loadRequest = this._loadRequest;
        initialVisibleLayerFitComplete = true;
        targetMap.attributionControl.addAttribution(this._attribution);
        if (this._placementCorners && this._placementImageUrl) {
          this._showPlacement();
          return;
        }
        this._load(loadRequest);
      },

      onRemove: function (targetMap) {
        this._loadRequest += 1;
        (this._warpedLayers || []).forEach((layer) => {
          if (targetMap.hasLayer(layer)) targetMap.removeLayer(layer);
        });
        if (this._placementOverlay && targetMap.hasLayer(this._placementOverlay)) {
          targetMap.removeLayer(this._placementOverlay);
        }
        targetMap.attributionControl.removeAttribution(this._attribution);
        this._map = null;
      },

      getBounds: function () {
        return this._bounds;
      },

      setOpacity: function (opacity) {
        this._opacity = opacity;
        (this._warpedLayers || []).forEach((layer) => layer.setOpacity && layer.setOpacity(opacity));
        if (this._placementOverlay) this._placementOverlay.setOpacity(opacity);
        return this;
      },

      setPlacement: function (corners, imageUrl) {
        this._placementCorners = {
          topLeft: Leaflet.latLng(corners.topLeft),
          topRight: Leaflet.latLng(corners.topRight),
          bottomRight: Leaflet.latLng(corners.bottomRight),
          bottomLeft: Leaflet.latLng(corners.bottomLeft)
        };
        this._placementImageUrl = imageUrl || this._placementImageUrl;
        if (this._map) this._showPlacement();
        return this;
      },

      getPlacement: function () {
        if (!this._placementCorners) return null;
        return Object.fromEntries(Object.entries(this._placementCorners).map(([name, latLng]) => [
          name,
          Leaflet.latLng(latLng)
        ]));
      },

      _showPlacement: function () {
        if (!this._map || !this._placementImageUrl || !this._placementCorners) return;
        (this._warpedLayers || []).forEach((layer) => {
          if (this._map.hasLayer(layer)) this._map.removeLayer(layer);
        });
        if (!this._placementOverlay) {
          this._placementOverlay = new RayRotatedImageOverlay(
            this._placementImageUrl,
            this._placementCorners.topLeft,
            this._placementCorners.topRight,
            this._placementCorners.bottomLeft,
            {
            interactive: false,
            opacity: this._opacity,
            pane: "historicPlacementPane"
            }
          );
        } else {
          this._placementOverlay.reposition(
            this._placementCorners.topLeft,
            this._placementCorners.topRight,
            this._placementCorners.bottomLeft
          );
          this._placementOverlay.setOpacity(this._opacity);
        }
        if (!this._map.hasLayer(this._placementOverlay)) this._placementOverlay.addTo(this._map);
        this.bringToBack();
      },

      bringToBack: function () {
        (this._warpedLayers || []).forEach((layer) => layer.bringToBack && layer.bringToBack());
        if (this._placementOverlay && this._placementOverlay.bringToBack) this._placementOverlay.bringToBack();
        return this;
      },

      _load: async function (loadRequest) {
        try {
          if (!this._warpedLayers) {
            const leafletNamespace = window.L;
            let allmaps;
            try {
              [allmaps, this._allmapsRender] = await Promise.all([
                import("https://cdn.jsdelivr.net/npm/@allmaps/leaflet@1.0.0-beta.55/+esm"),
                import("https://cdn.jsdelivr.net/npm/@allmaps/render@1.0.0-beta.84/+esm")
              ]);
            } finally {
              window.L = leafletNamespace;
            }
            if (loadRequest !== this._loadRequest || !this._map) return;
            const annotationResponse = await fetch(this._annotationUrl);
            if (!annotationResponse.ok) {
              throw new Error(`Historic map annotation request failed: ${annotationResponse.status}`);
            }
            const annotation = await annotationResponse.json();
            (annotation.items || []).forEach((item) => {
              const source = item && item.target && item.target.source;
              if (source && typeof source.id === "string") {
                const sheetMatch = this._localIiifPattern && source.id.match(this._localIiifPattern);
                if (sheetMatch) {
                  source.id = new URL(`/data/historic-maps/iiif/${sheetMatch[1]}`, window.location.origin).href;
                }
              }
            });
            const sourceUrls = [...new Set((annotation.items || []).map((item) => {
              const source = item && item.target && item.target.source;
              return source && source.id;
            }).filter(Boolean))];
            const imageInfos = await Promise.all(sourceUrls.map(async (sourceUrl) => {
              const response = await fetch(`${sourceUrl}/info.json`);
              if (!response.ok) {
                throw new Error(`Historic map image information request failed: ${response.status}`);
              }
              const imageInfo = await response.json();
              imageInfo["@id"] = sourceUrl;
              return imageInfo;
            }));
            if (loadRequest !== this._loadRequest || !this._map) return;
            const groupedItems = [];
            const sourceOccurrences = new Map();
            (annotation.items || []).forEach((item) => {
              const sourceUrl = item && item.target && item.target.source && item.target.source.id;
              const occurrence = sourceOccurrences.get(sourceUrl) || 0;
              sourceOccurrences.set(sourceUrl, occurrence + 1);
              if (!groupedItems[occurrence]) groupedItems[occurrence] = [];
              groupedItems[occurrence].push(item);
            });
            this._warpedLayers = groupedItems.map((items) => {
              const layer = new allmaps.WarpedMapLayer(undefined, {
                opacity: this._opacity,
                pane: "historicMapsPane"
              });
              layer.canvas.classList.remove("leaflet-zoom-animated");
              const renderHistoricMap = (view) => {
                if (!layer._map || !layer.renderer || !layer.canvas) return;
                const target = view || {};
                const center = target.center || layer._map.getCenter();
                const zoom = Number.isFinite(target.zoom) ? target.zoom : layer._map.getZoom();
                const crs = layer._map.options.crs;
                const projectedCenter = crs.project(center);
                const centerPixel = layer._map.project(center, zoom);
                const adjacentLatLng = layer._map.unproject(centerPixel.add([1, 0]), zoom);
                const adjacentProjected = crs.project(adjacentLatLng);
                const projectedUnitsPerPixel = Math.hypot(
                  adjacentProjected.x - projectedCenter.x,
                  adjacentProjected.y - projectedCenter.y
                );
                const size = layer._map.getSize();
                const mapPanePosition = layer._map._getMapPanePos();
                L.DomUtil.setPosition(layer.canvas, mapPanePosition.multiplyBy(-1));
                layer.canvas.style.transform = layer.canvas.style.transform.replace(/\s*scale\([^)]*\)/, "");
                layer.gl.clearColor(0, 0, 0, 0);
                layer.gl.clear(
                  layer.gl.COLOR_BUFFER_BIT |
                  layer.gl.DEPTH_BUFFER_BIT |
                  layer.gl.STENCIL_BUFFER_BIT
                );
                layer.renderer.render(new this._allmapsRender.Viewport(
                  [size.x, size.y],
                  [projectedCenter.x, projectedCenter.y],
                  projectedUnitsPerPixel,
                  {
                    devicePixelRatio: window.devicePixelRatio,
                    rotation: layer._map._bearing
                  }
                ));
              };
              layer._update = function () {
                renderHistoricMap();
                return this.container;
              };
              layer._animateZoom = function (event) {
                renderHistoricMap(event);
              };
              this._map.addLayer(layer);
              layer.addImageInfos(imageInfos);
              layer.addGeoreferenceAnnotation({ ...annotation, items });
              return layer;
            });
          } else {
            this._warpedLayers.forEach((layer) => {
              if (!this._map.hasLayer(layer)) this._map.addLayer(layer);
            });
          }
          if (loadRequest !== this._loadRequest || !this._map) return;
          this._warpedLayers.forEach((layer) => layer.setOpacity(this._opacity));
          this.bringToBack();
        } catch (error) {
          console.error(`Could not load the ${this._label} historic map layer.`, error);
          if (loadRequest === this._loadRequest && this._map) {
            window.alert(`The ${this._label} historic map layer could not be loaded. Please try again.`);
          }
        }
      }
    });
    const historicMapDefinitions = [
      { label: "1884 Jacksonville", slug: "historic1884", aliases: ["jacksonville1884", "sanborn1884"], itemId: "sanborn01286_001", annotationUrl: "/data/historic-maps/jacksonville-sanborn-1884-georeference.json", bounds: [[30.323807908372586, -81.6642101], [30.3315704, -81.6514076150357]], localIiifPattern: /(01286_1884-\d{4})(?:\/info\.json)?\/?$/ },
      { label: "1887 Jacksonville", slug: "historic1887", aliases: ["jacksonville1887", "sanborn1887"], itemId: "sanborn01286_002", annotationUrl: "/data/historic-maps/annotations/sanborn01286_002.json" },
      { label: "1891 Jacksonville", slug: "historic1891", aliases: ["jacksonville1891", "sanborn1891"], itemId: "sanborn01286_003", annotationUrl: "/data/historic-maps/annotations/sanborn01286_003.json" },
      { label: "1897 Jacksonville", slug: "historic1897", aliases: ["jacksonville1897", "sanborn1897"], itemId: "sanborn01286_004", annotationUrl: "/data/historic-maps/annotations/sanborn01286_004.json" },
      {
        label: "Great Fire of 1901",
        slug: "historic1901fire",
        aliases: ["greatfire1901", "jacksonvillefire1901", "historic1925fire"],
        sourceUrl: "https://libapps.s3.amazonaws.com/accounts/29813/images/1925_Map_of_District_Burned_May_3_1901_-_TFD.jpg",
        attributionLabel: "T. Frederick Davis, Map of district burned May 3, 1901",
        annotationUrl: "/data/historic-maps/annotations/great-fire-1901-map.json",
        localIiifPattern: /(great-fire-1901-map)(?:\/info\.json)?\/?$/,
        bounds: [[30.3188515, -81.6770424], [30.3442707, -81.6368008]],
        rectangularImageUrl: "/data/historic-maps/images/1925-great-fire-district-map.jpg",
        placementEditorEnabled: false,
        placement: {
          topLeft: [30.3442707, -81.6718571],
          topRight: [30.3366681, -81.6368008],
          bottomRight: [30.3188515, -81.6419861],
          bottomLeft: [30.3264555, -81.6770424]
        },
        georeferenceCredit: "Ray Hollister"
      },
      { label: "1903 Jacksonville", slug: "historic1903", aliases: ["jacksonville1903", "sanborn1903"], itemId: "sanborn01286_005", annotationUrl: "/data/historic-maps/annotations/sanborn01286_005.json" },
      { label: "1903 Pablo Beach", slug: "historic1903pablobeach", aliases: ["pablobeach1903"], itemId: "sanborn01324_001", annotationUrl: "/data/historic-maps/annotations/sanborn01324_001.json", coastal: true },
      { label: "1909 Pablo Beach", slug: "historic1909pablobeach", aliases: ["pablobeach1909"], itemId: "sanborn01324_002", annotationUrl: "/data/historic-maps/annotations/sanborn01324_002.json", coastal: true },
      { label: "1913 Jacksonville — Volume 1", slug: "historic1913v1", aliases: ["jacksonville1913v1", "sanborn1913v1"], itemId: "sanborn01286_006", annotationUrl: "/data/historic-maps/annotations/sanborn01286_006.json" },
      { label: "1913 Jacksonville — Volume 2", slug: "historic1913v2", aliases: ["jacksonville1913v2", "sanborn1913v2"], itemId: "sanborn01286_007", annotationUrl: "/data/historic-maps/annotations/sanborn01286_007.json" },
      { label: "1917 Pablo Beach", slug: "historic1917pablobeach", aliases: ["pablobeach1917"], itemId: "sanborn01324_003", annotationUrl: "/data/historic-maps/annotations/sanborn01324_003.json", coastal: true },
      { label: "1921 Mayport", slug: "historic1921mayport", aliases: ["mayport1921"], itemId: "sanborn01307_002", annotationUrl: "/data/historic-maps/annotations/sanborn01307_002.json", mayport: true },
      { label: "1924 Pablo Beach", slug: "historic1924pablobeach", aliases: ["pablobeach1924"], itemId: "sanborn01324_004", annotationUrl: "/data/historic-maps/annotations/sanborn01324_004.json", coastal: true },
      { label: "1949 Jacksonville — Volume 1A", slug: "historic1949v1a", aliases: ["jacksonville1949v1a", "sanborn1949v1a"], itemId: "sanborn01286_008", annotationUrl: "/data/historic-maps/annotations/sanborn01286_008.json" },
      { label: "1949 Jacksonville — Volume 4", slug: "historic1949v4", aliases: ["jacksonville1949v4", "sanborn1949v4"], itemId: "sanborn01286_010", annotationUrl: "/data/historic-maps/annotations/sanborn01286_010.json" }
    ];
    historicMapDefinitions.forEach((definition) => {
      const bounds = definition.mayport
        ? [[30.37, -81.46], [30.43, -81.38]]
        : definition.coastal
          ? [[30.25, -81.45], [30.36, -81.35]]
          : definition.bounds || [[30.20, -81.85], [30.50, -81.45]];
      definition.layer = new HistoricMapLayer(definition.annotationUrl, bounds, {
        label: definition.label,
        sourceUrl: definition.sourceUrl || `https://www.loc.gov/item/${definition.itemId}/`,
        attributionLabel: definition.attributionLabel,
        localIiifPattern: definition.localIiifPattern,
        georeferenceCredit: definition.georeferenceCredit
      });
      if (definition.placement && definition.rectangularImageUrl) {
        definition.layer.setPlacement(definition.placement, definition.rectangularImageUrl);
      }
      if (definition.placementEditorEnabled) definition.layer.on("remove", stopHistoricMapPlacementEditor);
    });
    const historicMapLayers = historicMapDefinitions.map((definition) => definition.layer);
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
    const votingPrecinctFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "votingPrecinct"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "votingPrecinct")
    });
    const votingPrecinctBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "votingPrecinct"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "votingPrecinct")
    });
    const pollingLocationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getPollingLocationStyle()),
      onEachFeature: (feature, layer) => addPollingLocationInteractivity(feature, layer)
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
    const usSenateFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "usSenate"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "usSenate")
    });
    const usSenateBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "usSenate"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "usSenate")
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
    const elevationWmsUrl = "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer";
    const elevationImageServerUrl = "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage";
    const elevationAttribution = '<a href="https://www.usgs.gov/programs/national-geospatial-program/national-map" target="_blank" rel="noopener">USGS The National Map</a> · <a href="https://www.usgs.gov/3d-elevation-program" target="_blank" rel="noopener">3DEP</a>';
    let resolveRegionalElevationMask;
    let regionalElevationMaskFeatures = [];
    const regionalElevationMaskReady = new Promise((resolve) => {
      resolveRegionalElevationMask = resolve;
    });
    const elevationColorRenderingRule = JSON.stringify({
      rasterFunction: "Colormap",
      rasterFunctionArguments: {
        Colormap: [
          [0, 49, 130, 189],
          [1, 107, 174, 214],
          [2, 166, 219, 160],
          [3, 255, 255, 179],
          [4, 254, 204, 92],
          [5, 253, 141, 60],
          [6, 244, 109, 67],
          [7, 215, 48, 39],
          [8, 165, 0, 38],
          [9, 103, 0, 31]
        ],
        Raster: {
          rasterFunction: "Remap",
          rasterFunctionArguments: {
            InputRanges: [-1000, 0, 0, 1.524, 1.524, 3.048, 3.048, 6.096, 6.096, 9.144, 9.144, 15.24, 15.24, 18.288, 18.288, 24.384, 24.384, 36.576, 36.576, 1000],
            OutputValues: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            Raster: "$$"
          }
        }
      }
    });
    function getSquaredSegmentDistance(point, start, end) {
      let x = start[0];
      let y = start[1];
      let dx = end[0] - x;
      let dy = end[1] - y;
      if (dx !== 0 || dy !== 0) {
        const offset = ((point[0] - x) * dx + (point[1] - y) * dy) / (dx * dx + dy * dy);
        if (offset > 1) {
          x = end[0];
          y = end[1];
        } else if (offset > 0) {
          x += dx * offset;
          y += dy * offset;
        }
      }
      dx = point[0] - x;
      dy = point[1] - y;
      return dx * dx + dy * dy;
    }

    function simplifyRegionalMaskRing(points, tolerance) {
      if (!points || points.length <= 4) return points || [];
      const openPoints = points.slice(0, -1);
      const squaredTolerance = tolerance * tolerance;
      const markers = new Uint8Array(openPoints.length);
      const stack = [[0, openPoints.length - 1]];
      markers[0] = 1;
      markers[openPoints.length - 1] = 1;
      while (stack.length) {
        const [first, last] = stack.pop();
        let maximumDistance = squaredTolerance;
        let index = 0;
        for (let pointIndex = first + 1; pointIndex < last; pointIndex += 1) {
          const distance = getSquaredSegmentDistance(openPoints[pointIndex], openPoints[first], openPoints[last]);
          if (distance > maximumDistance) {
            index = pointIndex;
            maximumDistance = distance;
          }
        }
        if (index) {
          markers[index] = 1;
          stack.push([first, index], [index, last]);
        }
      }
      const simplified = openPoints.filter((point, index) => markers[index]);
      simplified.push(simplified[0]);
      return simplified;
    }

    function setRegionalElevationMask(geojson) {
      regionalElevationMaskFeatures = (geojson.features || []).map((feature) => ({
        type: feature.geometry.type,
        coordinates: feature.geometry.coordinates.map((polygonOrRing) => {
          if (feature.geometry.type === "Polygon") {
            return simplifyRegionalMaskRing(polygonOrRing, 0.0005);
          }
          return polygonOrRing.map((ring) => simplifyRegionalMaskRing(ring, 0.0005));
        })
      }));
      resolveRegionalElevationMask();
      elevationColorLayer.redraw();
      elevationContoursOverviewLayer.redraw();
      elevationContoursDetailLayer.redraw();
    }

    function appendRegionalElevationMaskPath(context, coords, tileSize) {
      const tileOrigin = L.point(coords.x * tileSize.x, coords.y * tileSize.y);
      const appendRing = (ring) => {
        ring.forEach(([longitude, latitude], index) => {
          const point = map.project(L.latLng(latitude, longitude), coords.z).subtract(tileOrigin);
          if (index === 0) context.moveTo(point.x, point.y);
          else context.lineTo(point.x, point.y);
        });
        context.closePath();
      };
      regionalElevationMaskFeatures.forEach((geometry) => {
        if (geometry.type === "Polygon") geometry.coordinates.forEach(appendRing);
        else geometry.coordinates.forEach((polygon) => polygon.forEach(appendRing));
      });
    }

    const RegionalElevationGridLayer = L.GridLayer.extend({
      createTile: function (coords, done) {
        const tile = document.createElement("canvas");
        const tileSize = this.getTileSize();
        tile.width = tileSize.x;
        tile.height = tileSize.y;
        regionalElevationMaskReady.then(() => {
          const image = new Image();
          image.crossOrigin = "anonymous";
          image.onload = () => {
            const context = tile.getContext("2d");
            context.beginPath();
            appendRegionalElevationMaskPath(context, coords, tileSize);
            context.clip("evenodd");
            context.drawImage(image, 0, 0, tileSize.x, tileSize.y);
            done(null, tile);
          };
          image.onerror = (error) => done(error, tile);
          image.src = this.options.getImageUrl.call(this, coords, tileSize);
        });
        return tile;
      }
    });

    function getRegionalElevationTileBounds(layer, coords) {
      const bounds = layer._tileCoordsToBounds(coords);
      const northWest = map.options.crs.project(bounds.getNorthWest());
      const southEast = map.options.crs.project(bounds.getSouthEast());
      return `${northWest.x},${southEast.y},${southEast.x},${northWest.y}`;
    }

    function getElevationColorImageUrl(coords, tileSize) {
      const params = new URLSearchParams({
        bbox: getRegionalElevationTileBounds(this, coords),
        bboxSR: "3857",
        f: "image",
        format: "png32",
        imageSR: "3857",
        renderingRule: elevationColorRenderingRule,
        size: `${tileSize.x},${tileSize.y}`,
        transparent: "true"
      });
      return `${elevationImageServerUrl}?${params}`;
    }

    function getElevationContourImageUrl(layerName, coords, tileSize) {
      const params = new URLSearchParams({
        bbox: getRegionalElevationTileBounds(this, coords),
        crs: "EPSG:3857",
        format: "image/png",
        height: String(tileSize.y),
        layers: layerName,
        request: "GetMap",
        service: "WMS",
        styles: "default",
        transparent: "true",
        version: "1.3.0",
        width: String(tileSize.x)
      });
      return `${elevationWmsUrl}?${params}`;
    }

    const elevationColorLayer = new RegionalElevationGridLayer({
      attribution: elevationAttribution,
      getImageUrl: getElevationColorImageUrl,
      keepBuffer: 4,
      opacity: 0.35,
      pane: "elevationPane",
      updateWhenIdle: false,
      updateWhenZooming: true
    });
    const elevationContoursOverviewLayer = new RegionalElevationGridLayer({
      attribution: elevationAttribution,
      getImageUrl: function (coords, tileSize) {
        return getElevationContourImageUrl.call(this, "3DEPElevation:Preset 10ft Contour Interval", coords, tileSize);
      },
      keepBuffer: 4,
      maxZoom: 12,
      opacity: 0.35,
      pane: "elevationPane",
      updateWhenIdle: false,
      updateWhenZooming: true
    });
    const elevationContoursDetailLayer = new RegionalElevationGridLayer({
      attribution: elevationAttribution,
      getImageUrl: function (coords, tileSize) {
        return getElevationContourImageUrl.call(this, "3DEPElevation:Preset 5ft Contour Interval", coords, tileSize);
      },
      keepBuffer: 4,
      minZoom: 13,
      opacity: 0.35,
      pane: "elevationPane",
      updateWhenIdle: false,
      updateWhenZooming: true
    });
    const elevationContoursLayer = L.layerGroup([
      elevationContoursOverviewLayer,
      elevationContoursDetailLayer
    ]);
    const floodZoneFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "floodZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "floodZone")
    });
    const floodZoneBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "floodZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "floodZone")
    });
    const evacuationZoneFillLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "fill", "evacuationZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "fill", "evacuationZone")
    });
    const evacuationZoneBorderLayer = L.geoJSON(null, {
      style: (feature) => getBoundaryStyle(feature, "border", "evacuationZone"),
      onEachFeature: (feature, layer) => addBoundaryInteractivity(feature, layer, "border", "evacuationZone")
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
    const skywayRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addTransitRouteInteractivity(feature, layer, "skywayRoute")
    });
    const ferryRouteLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addTransitRouteInteractivity(feature, layer, "ferryRoute")
    });
    const interstateRouteNumbers = ["4", "10", "75", "95", "110", "175", "195", "275", "295", "375", "395", "595"];
    const interstateLayersByRouteNumber = new Map(interstateRouteNumbers.map((routeNumber) => [
      routeNumber,
      L.geoJSON(null, {
        style: () => getInterstateStyle(),
        onEachFeature: (feature, layer) => addInterstateInteractivity(feature, layer)
      })
    ]));
    const duvalInterstatesLayer = L.geoJSON(null, {
      style: () => getInterstateStyle(),
      onEachFeature: (feature, layer) => addInterstateInteractivity(feature, layer)
    });
    const northeastFloridaInterstatesLayer = L.geoJSON(null, {
      style: () => getInterstateStyle(),
      onEachFeature: (feature, layer) => addInterstateInteractivity(feature, layer)
    });
    const trainTracksLayer = L.geoJSON(null, {
      style: () => getTrainTrackStyle(),
      onEachFeature: (feature, layer) => addTrainTrackInteractivity(feature, layer)
    });
    const amtrakRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addRailRouteInteractivity(feature, layer, "amtrakRoute")
    });
    const brightlineRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addRailRouteInteractivity(feature, layer, "brightlineRoute")
    });
    const sunrailRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addRailRouteInteractivity(feature, layer, "sunrailRoute")
    });
    const triRailRoutesLayer = L.geoJSON(null, {
      style: (feature) => getBusRouteStyle(feature),
      onEachFeature: (feature, layer) => addRailRouteInteractivity(feature, layer, "triRailRoute")
    });
    const busStopsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getBusStopStyle()),
      onEachFeature: (feature, layer) => addBusStopInteractivity(feature, layer)
    });
    const skywayStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getSkywayStationStyle()),
      onEachFeature: (feature, layer) => addTransitStopInteractivity(feature, layer, "skywayStation")
    });
    const ferryLandingsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getFerryLandingStyle()),
      onEachFeature: (feature, layer) => addTransitStopInteractivity(feature, layer, "ferryLanding")
    });
    const trainStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getTrainStationStyle()),
      onEachFeature: (feature, layer) => addTrainStationInteractivity(feature, layer)
    });
    const brightlineStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getTrainStationStyle("#5F6A73")),
      onEachFeature: (feature, layer) => addTrainStationInteractivity(feature, layer)
    });
    const sunrailStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getTrainStationStyle("#ed1c24")),
      onEachFeature: (feature, layer) => addTrainStationInteractivity(feature, layer)
    });
    const triRailStationsLayer = L.geoJSON(null, {
      pointToLayer: (feature, latlng) => L.circleMarker(latlng, getTrainStationStyle("#009bdb")),
      onEachFeature: (feature, layer) => addTrainStationInteractivity(feature, layer)
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
    const jsonDataPromises = new Map();
    const boundaryLayerStackItemsByLayer = new Map();
    const boundaryLayerStackOrder = [];
    const defaultGovernmentOverlayOpacity = 0.35;
    let governmentLayerMode = "fill";
    let governmentOverlayOpacity = defaultGovernmentOverlayOpacity;
    let governmentLayerOpacityInput;
    let governmentLayerOpacityLabel;
    const busRouteBoundaryToleranceMeters = 100;
    let mapInteractionMode = "browse";
    let focusToggleButton;
    let focusedBoundary;
    let votingPrecinctPollingPointer;
    let votingPrecinctPollingPointerPrecinct = "";
    const focusLayerStates = new Map();
    let compareModeEnabled = false;
    let compareToggleButton;
    let pinnedCardPanel;
    let pinnedCardBody;
    let mapContextMenuElement;
    let historicMapPlacementEditor;
    const pinnedBoundaryCards = [];
    let pendingMapDataLoads = 0;
    let initialVisibleLayerFitComplete = hasRequestedMapCoordinates;
    let initialVisibleLayerFitTimeout;
    const busRouteLayersByRouteId = new Map();
    const busRouteMetadataByRouteId = new Map();
    const selectedBusRouteIds = new Set();
    const busRouteFilterInputs = new Map();
    const trimmedBusRouteLayerStates = new Map();
    const trimmedTrainTrackLayerStates = new Map();
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

    function registerBoundaryLayerStack(layers) {
      const stackItem = {
        layers: layers.filter(Boolean)
      };
      stackItem.layers.forEach((layer) => {
        boundaryLayerStackItemsByLayer.set(layer, stackItem);
      });
      return stackItem;
    }

    function isBoundaryLayerStackItemActive(stackItem) {
      return stackItem && stackItem.layers.some((layer) => map.hasLayer(layer));
    }

    function pruneBoundaryLayerStackOrder() {
      for (let index = boundaryLayerStackOrder.length - 1; index >= 0; index -= 1) {
        if (!isBoundaryLayerStackItemActive(boundaryLayerStackOrder[index])) {
          boundaryLayerStackOrder.splice(index, 1);
        }
      }
    }

    function trackBoundaryLayerStackSelection(layer) {
      const stackItem = boundaryLayerStackItemsByLayer.get(layer);
      if (!stackItem) return;
      pruneBoundaryLayerStackOrder();
      if (!boundaryLayerStackOrder.includes(stackItem)) {
        boundaryLayerStackOrder.push(stackItem);
      }
    }

    function orderMapLayers() {
      const defaultPolygonLayers = [
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
        votingPrecinctFillLayer,
        votingPrecinctBorderLayer,
        votingPrecinctFillLayer,
        votingPrecinctBorderLayer,
        neighborhoodFillLayer,
        neighborhoodBorderLayer,
        cpacFillLayer,
        cpacBorderLayer,
        floridaHouseFillLayer,
        floridaHouseBorderLayer,
        floridaSenateFillLayer,
        floridaSenateBorderLayer,
        usSenateFillLayer,
        usSenateBorderLayer,
        zipCodeFillLayer,
        zipCodeBorderLayer,
        congressionalDistrictFillLayer,
        congressionalDistrictBorderLayer,
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        floodZoneFillLayer,
        floodZoneBorderLayer,
        evacuationZoneFillLayer,
        evacuationZoneBorderLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer
      ];
      pruneBoundaryLayerStackOrder();
      const stackedPolygonLayers = boundaryLayerStackOrder
        .flatMap((stackItem) => stackItem.layers)
        .filter((layer, index, layers) => map.hasLayer(layer) && layers.indexOf(layer) === index);
      const unstackedPolygonLayers = defaultPolygonLayers
        .filter((layer) => map.hasLayer(layer) && !stackedPolygonLayers.includes(layer));
      const polygonLayers = stackedPolygonLayers.concat(unstackedPolygonLayers);
      const lineLayers = [
        busRoutesLayer,
        skywayRoutesLayer,
        ferryRouteLayer,
        duvalInterstatesLayer,
        northeastFloridaInterstatesLayer,
        ...interstateLayersByRouteNumber.values(),
        trainTracksLayer,
        amtrakRoutesLayer,
        brightlineRoutesLayer,
        sunrailRoutesLayer,
        triRailRoutesLayer
      ];
      const pointLayers = [
        leadershipJaxLocationsLayer,
        activePlaceLayer,
        archivedPlaceLayer,
        jsoPoliceStationsLayer,
        neighborhoodOrganizationsLayer,
        pollingLocationsLayer,
        pollingLocationsLayer,
        busStopsLayer,
        skywayStationsLayer,
        ferryLandingsLayer,
        trainStationsLayer,
        brightlineStationsLayer,
        sunrailStationsLayer,
        triRailStationsLayer,
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
      historicMapLayers.forEach((layer) => {
        if (map.hasLayer(layer)) layer.bringToBack();
      });
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
        usSenateFillLayer,
        usSenateBorderLayer,
        zipCodeFillLayer,
        zipCodeBorderLayer,
        congressionalDistrictFillLayer,
        congressionalDistrictBorderLayer,
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        floodZoneFillLayer,
        floodZoneBorderLayer,
        evacuationZoneFillLayer,
        evacuationZoneBorderLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer,
        neighborhoodOrganizationsLayer,
        jsoPoliceStationsLayer,
        busRoutesLayer,
        busStopsLayer,
        skywayRoutesLayer,
        skywayStationsLayer,
        ferryRouteLayer,
        ferryLandingsLayer,
        duvalInterstatesLayer,
        northeastFloridaInterstatesLayer,
        ...interstateLayersByRouteNumber.values(),
        trainTracksLayer,
        amtrakRoutesLayer,
        brightlineRoutesLayer,
        sunrailRoutesLayer,
        triRailRoutesLayer,
        trainStationsLayer,
        brightlineStationsLayer,
        sunrailStationsLayer,
        triRailStationsLayer,
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

    function getFeatureBounds(feature) {
      if (!feature || !feature.geometry) return null;
      try {
        const layer = L.geoJSON(feature);
        const bounds = layer.getBounds();
        return bounds && bounds.isValid && bounds.isValid() ? bounds : null;
      } catch (error) {
        return null;
      }
    }

    function fitFeatureInMapView(feature) {
      const bounds = getFeatureBounds(feature);
      if (!bounds) return;
      map.fitBounds(bounds, { padding: [32, 32] });
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
      updateYouAreHereCard();
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
        usSenateFillLayer,
        usSenateBorderLayer,
        zipCodeFillLayer,
        zipCodeBorderLayer,
        congressionalDistrictFillLayer,
        congressionalDistrictBorderLayer,
        healthZoneFillLayer,
        healthZoneBorderLayer,
        healthZoneByZipCodeLayer,
        floodZoneFillLayer,
        floodZoneBorderLayer,
        evacuationZoneFillLayer,
        evacuationZoneBorderLayer,
        jsoDistrictFillLayer,
        jsoDistrictBorderLayer,
        jsoSubsectionFillLayer,
        jsoSubsectionBorderLayer,
        neighborhoodOrganizationsLayer,
        jsoPoliceStationsLayer,
        trainTracksLayer,
        busStopsLayer,
        skywayRoutesLayer,
        skywayStationsLayer,
        ferryRouteLayer,
        ferryLandingsLayer,
        duvalInterstatesLayer,
        northeastFloridaInterstatesLayer,
        ...interstateLayersByRouteNumber.values(),
        amtrakRoutesLayer,
        brightlineRoutesLayer,
        sunrailRoutesLayer,
        triRailRoutesLayer,
        trainStationsLayer,
        brightlineStationsLayer,
        sunrailStationsLayer,
        triRailStationsLayer,
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
        usSenateFillLayer,
        zipCodeFillLayer,
        congressionalDistrictFillLayer,
        healthZoneFillLayer,
        healthZoneByZipCodeLayer,
        floodZoneFillLayer,
        evacuationZoneFillLayer,
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

    function cloneLayerLatLngs(latLngs) {
      return (latLngs || []).map((item) => {
        if (Array.isArray(item)) return cloneLayerLatLngs(item);
        return [item.lat, item.lng];
      });
    }

    function coordinatesToLatLngs(coordinates) {
      return (coordinates || []).map((coordinate) => [coordinate[1], coordinate[0]]);
    }

    function clippedGeometryToLatLngs(geometry) {
      if (!geometry || !geometry.coordinates) return [];
      if (geometry.type === "LineString") {
        return coordinatesToLatLngs(geometry.coordinates);
      }
      if (geometry.type === "MultiLineString") {
        return (geometry.coordinates || []).map((coordinates) => coordinatesToLatLngs(coordinates));
      }
      return [];
    }

    function clearTrimmedBusRoutes() {
      if (!trimmedBusRouteLayerStates.size) return;
      trimmedBusRouteLayerStates.forEach((state, layer) => {
        if (layer.setLatLngs) {
          layer.setLatLngs(state.latLngs);
        }
        if (state.wasVisible && !busRoutesLayer.hasLayer(layer)) {
          busRoutesLayer.addLayer(layer);
        } else if (!state.wasVisible && busRoutesLayer.hasLayer(layer)) {
          busRoutesLayer.removeLayer(layer);
        }
      });
      trimmedBusRouteLayerStates.clear();
      orderMapLayers();
    }

    function clearTrimmedTrainTracks() {
      if (!trimmedTrainTrackLayerStates.size) return;
      trimmedTrainTrackLayerStates.forEach((state, layer) => {
        if (layer.setLatLngs) {
          layer.setLatLngs(state.latLngs);
        }
        if (state.wasVisible && !trainTracksLayer.hasLayer(layer)) {
          trainTracksLayer.addLayer(layer);
        } else if (!state.wasVisible && trainTracksLayer.hasLayer(layer)) {
          trainTracksLayer.removeLayer(layer);
        }
      });
      trimmedTrainTrackLayerStates.clear();
      orderMapLayers();
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
      clearTrimmedBusRoutes();
      clearTrimmedTrainTracks();
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

      clearTrimmedBusRoutes();
      clearTrimmedTrainTracks();
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

    function getTextLineCount(element) {
      const range = document.createRange();
      range.selectNodeContents(element);
      const lineCount = Array.from(range.getClientRects()).filter((rect) => {
        return rect.width > 0 && rect.height > 0;
      }).length;
      range.detach();
      return lineCount;
    }

    function expandPhotoPopupIfContactWraps(popup) {
      const container = popup && popup.getElement ? popup.getElement() : popup && popup._container;
      const content = container && container.querySelector(".leaflet-popup-content");
      if (!content || !content.querySelector(".maps-district-popup--with-photo")) return;

      content.classList.remove("maps-popup-content--contact-width");
      requestAnimationFrame(() => {
        const contactLinks = content.querySelectorAll(".maps-district-popup--with-photo .maps-contact-link");
        const hasWrappedContact = Array.from(contactLinks).some((element) => getTextLineCount(element) > 1);
        if (!hasWrappedContact) return;

        content.classList.add("maps-popup-content--contact-width");
        if (popup && popup.update) {
          requestAnimationFrame(() => popup.update());
        }
      });
    }

    function makePopupDraggable(popup) {
      const container = popup && popup.getElement ? popup.getElement() : popup && popup._container;
      if (!container || container.dataset.mapsDraggablePopup === "true") return;
      const handle = container.querySelector(".leaflet-popup-content-wrapper");
      if (!handle) return;
      let startX = 0;
      let startY = 0;
      let startTranslateX = 0;
      let startTranslateY = 0;
      let dragging = false;
      let mapDraggingWasEnabled = false;

      function endDrag() {
        if (!dragging) return;
        dragging = false;
        container.classList.remove("maps-popup-dragging");
        window.removeEventListener("pointermove", onPointerMove);
        window.removeEventListener("pointerup", endDrag);
        window.removeEventListener("pointercancel", endDrag);
        if (mapDraggingWasEnabled && map.dragging) {
          map.dragging.enable();
        }
      }

      function onPointerMove(event) {
        if (!dragging) return;
        event.preventDefault();
        const nextX = startTranslateX + event.clientX - startX;
        const nextY = startTranslateY + event.clientY - startY;
        container.dataset.mapsPopupTranslateX = String(nextX);
        container.dataset.mapsPopupTranslateY = String(nextY);
        container.style.translate = `${nextX}px ${nextY}px`;
      }

      handle.addEventListener("pointerdown", function (event) {
        if (event.button !== 0 || event.target.closest("a, button, input, label, select, textarea, .leaflet-popup-close-button")) {
          return;
        }
        event.preventDefault();
        event.stopPropagation();
        startX = event.clientX;
        startY = event.clientY;
        startTranslateX = Number(container.dataset.mapsPopupTranslateX || 0);
        startTranslateY = Number(container.dataset.mapsPopupTranslateY || 0);
        dragging = true;
        mapDraggingWasEnabled = Boolean(map.dragging && map.dragging.enabled && map.dragging.enabled());
        if (mapDraggingWasEnabled) {
          map.dragging.disable();
        }
        container.classList.add("maps-popup-dragging");
        window.addEventListener("pointermove", onPointerMove);
        window.addEventListener("pointerup", endDrag);
        window.addEventListener("pointercancel", endDrag);
      });

      container.classList.add("maps-draggable-popup");
      container.dataset.mapsDraggablePopup = "true";
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

    function getEditableHistoricMapDefinition() {
      return historicMapDefinitions.find((definition) => (
        definition.placementEditorEnabled && map.hasLayer(definition.layer)
      ));
    }

    function getInitialHistoricMapPlacement(definition) {
      if (!definition) return null;
      const savedPlacement = definition.layer.getPlacement();
      if (savedPlacement) return savedPlacement;
      const bounds = Leaflet.latLngBounds(definition.bounds);
      const south = bounds.getSouth();
      const west = bounds.getWest();
      const north = bounds.getNorth();
      const east = bounds.getEast();
      return {
        topLeft: Leaflet.latLng(north, west),
        topRight: Leaflet.latLng(north, east),
        bottomRight: Leaflet.latLng(south, east),
        bottomLeft: Leaflet.latLng(south, west)
      };
    }

    function formatHistoricMapPlacementCoordinates(definition, corners) {
      const coordinatePair = (latLng) => [
        Number(latLng.lng.toFixed(7)),
        Number(latLng.lat.toFixed(7))
      ];
      const topLeftPoint = map.latLngToLayerPoint(corners.topLeft);
      const topRightPoint = map.latLngToLayerPoint(corners.topRight);
      const rotation = Math.atan2(
        topRightPoint.y - topLeftPoint.y,
        topRightPoint.x - topLeftPoint.x
      ) * 180 / Math.PI;
      return JSON.stringify({
        layer: definition.slug,
        coordinateOrder: "longitude, latitude",
        rotationDegreesClockwise: Number(rotation.toFixed(3)),
        corners: {
          topLeft: coordinatePair(corners.topLeft),
          topRight: coordinatePair(corners.topRight),
          bottomRight: coordinatePair(corners.bottomRight),
          bottomLeft: coordinatePair(corners.bottomLeft)
        }
      }, null, 2);
    }

    function stopHistoricMapPlacementEditor() {
      if (!historicMapPlacementEditor) return;
      if (map.hasLayer(historicMapPlacementEditor.guideLayer)) {
        map.removeLayer(historicMapPlacementEditor.guideLayer);
      }
      historicMapPlacementEditor = undefined;
    }

    function startHistoricMapPlacementEditor(definition) {
      if (!definition || !map.hasLayer(definition.layer)) return;
      stopHistoricMapPlacementEditor();

      let placementCorners = getInitialHistoricMapPlacement(definition);
      definition.layer.setPlacement(placementCorners, definition.rectangularImageUrl);
      const guideLayer = Leaflet.layerGroup().addTo(map);
      const outline = Leaflet.polygon([], {
        color: "#0969da",
        dashArray: "6 5",
        fill: false,
        interactive: false,
        pane: "markerPane",
        weight: 2
      }).addTo(guideLayer);
      const rotationGuide = Leaflet.polyline([], {
        color: "#0969da",
        dashArray: "3 4",
        interactive: false,
        pane: "markerPane",
        weight: 1
      }).addTo(guideLayer);
      const cornerMarkers = {};
      const cornerIcon = Leaflet.divIcon({
        className: "",
        html: '<span class="maps-historic-placement-handle" aria-hidden="true"></span>',
        iconAnchor: [8, 8],
        iconSize: [16, 16]
      });
      const moveIcon = Leaflet.divIcon({
        className: "",
        html: '<span class="maps-historic-placement-handle maps-historic-placement-handle--move" aria-hidden="true">↕</span>',
        iconAnchor: [11, 11],
        iconSize: [22, 22]
      });
      const rotationIcon = Leaflet.divIcon({
        className: "",
        html: '<span class="maps-historic-placement-handle maps-historic-placement-handle--rotate" aria-hidden="true">↻</span>',
        iconAnchor: [11, 11],
        iconSize: [22, 22]
      });
      const moveMarker = Leaflet.marker([0, 0], {
        draggable: true,
        icon: moveIcon,
        keyboard: true,
        title: `Move ${definition.label}`
      }).addTo(guideLayer);
      const rotationMarker = Leaflet.marker([0, 0], {
        draggable: true,
        icon: rotationIcon,
        keyboard: true,
        title: `Rotate ${definition.label}`
      }).addTo(guideLayer);
      let mapDraggingWasEnabled = false;

      function getPlacementGeometry(corners) {
        const topLeft = map.latLngToLayerPoint(corners.topLeft);
        const topRight = map.latLngToLayerPoint(corners.topRight);
        const bottomLeft = map.latLngToLayerPoint(corners.bottomLeft);
        const center = topLeft.add(topRight).add(bottomLeft).add(
          topRight.subtract(topLeft).add(bottomLeft)
        ).divideBy(4);
        const horizontal = topRight.subtract(topLeft);
        const vertical = bottomLeft.subtract(topLeft);
        const width = Math.hypot(horizontal.x, horizontal.y) / 2;
        const height = Math.hypot(vertical.x, vertical.y) / 2;
        return {
          center,
          halfHeight: height,
          halfWidth: width,
          unitX: horizontal.divideBy(width * 2),
          unitY: vertical.divideBy(height * 2)
        };
      }

      function cornersFromGeometry(geometry) {
        const horizontal = geometry.unitX.multiplyBy(geometry.halfWidth);
        const vertical = geometry.unitY.multiplyBy(geometry.halfHeight);
        const toLatLng = (point) => map.layerPointToLatLng(point);
        return {
          topLeft: toLatLng(geometry.center.subtract(horizontal).subtract(vertical)),
          topRight: toLatLng(geometry.center.add(horizontal).subtract(vertical)),
          bottomRight: toLatLng(geometry.center.add(horizontal).add(vertical)),
          bottomLeft: toLatLng(geometry.center.subtract(horizontal).add(vertical))
        };
      }

      function startHandleDrag() {
        mapDraggingWasEnabled = Boolean(map.dragging && map.dragging.enabled());
        if (mapDraggingWasEnabled) map.dragging.disable();
      }

      function finishHandleDrag() {
        if (mapDraggingWasEnabled && map.dragging) map.dragging.enable();
        mapDraggingWasEnabled = false;
      }

      function refreshEditor(nextCorners, activeHandle) {
        placementCorners = nextCorners;
        definition.layer.setPlacement(placementCorners, definition.rectangularImageUrl);
        outline.setLatLngs([
          placementCorners.topLeft,
          placementCorners.topRight,
          placementCorners.bottomRight,
          placementCorners.bottomLeft
        ]);
        const geometry = getPlacementGeometry(placementCorners);
        const rotationHandlePoint = geometry.center
          .subtract(geometry.unitY.multiplyBy(geometry.halfHeight + 42));
        const topCenterPoint = geometry.center.subtract(geometry.unitY.multiplyBy(geometry.halfHeight));
        Object.entries(cornerMarkers).forEach(([name, marker]) => {
          if (name !== activeHandle) marker.setLatLng(placementCorners[name]);
        });
        if (activeHandle !== "move") moveMarker.setLatLng(map.layerPointToLatLng(geometry.center));
        if (activeHandle !== "rotate") rotationMarker.setLatLng(map.layerPointToLatLng(rotationHandlePoint));
        rotationGuide.setLatLngs([
          map.layerPointToLatLng(topCenterPoint),
          map.layerPointToLatLng(rotationHandlePoint)
        ]);
        historicMapPlacementEditor.corners = placementCorners;
      }

      const cornerSigns = {
        topLeft: [-1, -1],
        topRight: [1, -1],
        bottomRight: [1, 1],
        bottomLeft: [-1, 1]
      };
      Object.entries(placementCorners).forEach(([name, latLng]) => {
        const marker = Leaflet.marker(latLng, {
          draggable: true,
          icon: cornerIcon,
          keyboard: true,
          title: `Resize ${definition.label} from ${name}`
        }).addTo(guideLayer);
        cornerMarkers[name] = marker;
        let resizeStartGeometry;
        marker.on("dragstart", function () {
          startHandleDrag();
          resizeStartGeometry = getPlacementGeometry(placementCorners);
        });
        marker.on("drag", function (event) {
          const [horizontalSign, verticalSign] = cornerSigns[name];
          const opposite = resizeStartGeometry.center
            .subtract(resizeStartGeometry.unitX.multiplyBy(horizontalSign * resizeStartGeometry.halfWidth))
            .subtract(resizeStartGeometry.unitY.multiplyBy(verticalSign * resizeStartGeometry.halfHeight));
          const dragged = map.latLngToLayerPoint(event.target.getLatLng());
          const diagonal = dragged.subtract(opposite);
          const horizontalProjection = diagonal.x * resizeStartGeometry.unitX.x + diagonal.y * resizeStartGeometry.unitX.y;
          const verticalProjection = diagonal.x * resizeStartGeometry.unitY.x + diagonal.y * resizeStartGeometry.unitY.y;
          const halfWidth = Math.max(8, horizontalSign * horizontalProjection / 2);
          const halfHeight = Math.max(8, verticalSign * verticalProjection / 2);
          refreshEditor(cornersFromGeometry({
            center: opposite.add(dragged).divideBy(2),
            halfHeight,
            halfWidth,
            unitX: resizeStartGeometry.unitX,
            unitY: resizeStartGeometry.unitY
          }), name);
        });
        marker.on("dragend", function () {
          finishHandleDrag();
          refreshEditor(placementCorners);
        });
      });

      let moveStartPoint;
      let moveStartGeometry;
      moveMarker.on("dragstart", function () {
        startHandleDrag();
        moveStartPoint = map.latLngToLayerPoint(moveMarker.getLatLng());
        moveStartGeometry = getPlacementGeometry(placementCorners);
      });
      moveMarker.on("drag", function (event) {
        const nextPoint = map.latLngToLayerPoint(event.target.getLatLng());
        refreshEditor(cornersFromGeometry({
          ...moveStartGeometry,
          center: moveStartGeometry.center.add(nextPoint.subtract(moveStartPoint))
        }), "move");
      });
      moveMarker.on("dragend", function () {
        finishHandleDrag();
        refreshEditor(placementCorners);
      });

      let rotateStartGeometry;
      rotationMarker.on("dragstart", function () {
        startHandleDrag();
        rotateStartGeometry = getPlacementGeometry(placementCorners);
      });
      rotationMarker.on("drag", function (event) {
        const pointer = map.latLngToLayerPoint(event.target.getLatLng());
        const outward = pointer.subtract(rotateStartGeometry.center);
        const distance = Math.max(1, Math.hypot(outward.x, outward.y));
        const unitY = outward.divideBy(-distance);
        const unitX = Leaflet.point(unitY.y, -unitY.x);
        refreshEditor(cornersFromGeometry({
          ...rotateStartGeometry,
          unitX,
          unitY
        }), "rotate");
      });
      rotationMarker.on("dragend", function () {
        finishHandleDrag();
        refreshEditor(placementCorners);
      });

      historicMapPlacementEditor = {
        definition,
        corners: placementCorners,
        cornerMarkers,
        guideLayer,
        moveMarker,
        outline,
        rotationGuide,
        rotationMarker
      };
      refreshEditor(placementCorners);
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

    function trimVisibleBusRoutesToFeature(polygonFeature) {
      if (!map.hasLayer(busRoutesLayer) || !polygonFeature || !polygonFeature.geometry) return 0;
      clearTrimmedBusRoutes();
      let trimmedCount = 0;

      busRouteLayersByRouteId.forEach((layers, routeId) => {
        if (!selectedBusRouteIds.has(routeId)) return;
        layers.forEach((layer) => {
          if (!busRoutesLayer.hasLayer(layer) || !layer.setLatLngs || !layer.feature) return;
          const clippedGeometry = clipLineGeometryToFeature(layer.feature.geometry, polygonFeature);
          trimmedBusRouteLayerStates.set(layer, {
            latLngs: cloneLayerLatLngs(layer.getLatLngs ? layer.getLatLngs() : []),
            wasVisible: true
          });

          if (clippedGeometry) {
            layer.setLatLngs(clippedGeometryToLatLngs(clippedGeometry));
            trimmedCount += 1;
          } else {
            busRoutesLayer.removeLayer(layer);
          }
        });
      });

      orderMapLayers();
      return trimmedCount;
    }

    function trimVisibleTrainTracksToFeature(polygonFeature) {
      if (!map.hasLayer(trainTracksLayer) || !polygonFeature || !polygonFeature.geometry) return 0;
      clearTrimmedTrainTracks();
      let trimmedCount = 0;

      trainTracksLayer.eachLayer((layer) => {
        if (!trainTracksLayer.hasLayer(layer) || !layer.setLatLngs || !layer.feature) return;
        const clippedGeometry = clipLineGeometryToFeature(layer.feature.geometry, polygonFeature);
        trimmedTrainTrackLayerStates.set(layer, {
          latLngs: cloneLayerLatLngs(layer.getLatLngs ? layer.getLatLngs() : []),
          wasVisible: true
        });

        if (clippedGeometry) {
          layer.setLatLngs(clippedGeometryToLatLngs(clippedGeometry));
          trimmedCount += 1;
        } else {
          trainTracksLayer.removeLayer(layer);
        }
      });

      orderMapLayers();
      return trimmedCount;
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

      const editableHistoricMapDefinition = getEditableHistoricMapDefinition();
      if (editableHistoricMapDefinition) {
        mapContextMenuElement.appendChild(createContextMenuButton(
          historicMapPlacementEditor ? "Finish positioning" : "Move, resize and rotate",
          historicMapPlacementEditor
            ? `Hide the ${editableHistoricMapDefinition.label} placement handles`
            : `Show handles for moving, independently resizing, and rotating ${editableHistoricMapDefinition.label}`,
          () => {
            if (historicMapPlacementEditor) {
              stopHistoricMapPlacementEditor();
            } else {
              startHistoricMapPlacementEditor(editableHistoricMapDefinition);
            }
            hideMapContextMenu();
          }
        ));
        mapContextMenuElement.appendChild(createContextMenuButton(
          "Copy coordinates",
          "Copy the rectangular bounds and four corner coordinates",
          (button) => {
            const placementCorners = historicMapPlacementEditor
              ? historicMapPlacementEditor.corners
              : getInitialHistoricMapPlacement(editableHistoricMapDefinition);
            copyTextToClipboard(formatHistoricMapPlacementCoordinates(editableHistoricMapDefinition, placementCorners))
              .then(() => {
                button.textContent = "Placement coordinates copied";
                window.setTimeout(hideMapContextMenu, 650);
              })
              .catch(() => {
                button.textContent = "Copy failed";
              });
          }
        ));
      }

      if (featureContext && featureContext.feature && featureContext.layer) {
        const contextTitle = getComparableFeatureTitle(featureContext.feature, featureContext.layerType);
        const isPolygonContext = featureContext.feature.geometry &&
          (featureContext.feature.geometry.type === "Polygon" || featureContext.feature.geometry.type === "MultiPolygon");
        if (isPolygonContext && featureContext.layerType !== "busRoute") {
          mapContextMenuElement.appendChild(createContextMenuButton(
            "Focus",
            `Focus on ${contextTitle}`,
            () => {
              const focusFeature = getFocusGeometryFeature(featureContext.feature, featureContext.layerType);
              mapInteractionMode = "focus";
              focusBoundaryFeature(
                featureContext.feature,
                featureContext.layer,
                featureContext.mode,
                featureContext.layerType,
                { force: true }
              );
              fitFeatureInMapView(focusFeature);
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
        if (isPolygonContext && featureContext.layerType !== "busRoute" && mapInteractionMode === "focus" && map.hasLayer(busRoutesLayer)) {
          mapContextMenuElement.appendChild(createContextMenuButton(
            "Trim Bus Routes",
            `Trim visible bus routes to ${contextTitle}`,
            () => {
              const focusFeature = getFocusGeometryFeature(featureContext.feature, featureContext.layerType);
              focusBoundaryFeature(
                featureContext.feature,
                featureContext.layer,
                featureContext.mode,
                featureContext.layerType,
                { force: true }
              );
              trimVisibleBusRoutesToFeature(focusFeature);
              fitFeatureInMapView(focusFeature);
              hideMapContextMenu();
            }
          ));
        }
        if (isPolygonContext && featureContext.layerType !== "trainTrack" && mapInteractionMode === "focus" && map.hasLayer(trainTracksLayer)) {
          mapContextMenuElement.appendChild(createContextMenuButton(
            "Trim Train Tracks",
            `Trim visible train tracks to ${contextTitle}`,
            () => {
              const focusFeature = getFocusGeometryFeature(featureContext.feature, featureContext.layerType);
              focusBoundaryFeature(
                featureContext.feature,
                featureContext.layer,
                featureContext.mode,
                featureContext.layerType,
                { force: true }
              );
              trimVisibleTrainTracksToFeature(focusFeature);
              fitFeatureInMapView(focusFeature);
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
        const councilDistrictQuerySlug = queryLayerSlugsByLayer.get(councilDistrictFillLayer);
        if (control.layer !== councilDistrictFillLayer &&
            map.hasLayer(councilDistrictFillLayer) &&
            !explicitQueryLayerSlugs.has(councilDistrictQuerySlug)) {
          map.removeLayer(councilDistrictFillLayer);
        }
        if (!map.hasLayer(control.layer)) map.addLayer(control.layer);
        restoreBoundaryLayerFeatures(control.layer);
        trackBoundaryLayerStackSelection(control.layer);
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
      if (settings.group === "boundaries" && !boundaryLayerStackItemsByLayer.has(layer)) {
        registerBoundaryLayerStack([layer].concat(settings.alternateLayers || []));
      }
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

    function activateHistoricMapOpacityQuery() {
      const params = new URLSearchParams(window.location.search);
      if (!params.has("hm-opacity")) return;
      const opacity = Number(params.get("hm-opacity"));
      if (!Number.isFinite(opacity)) return;
      setHistoricMapOpacity(opacity / 100);
    }

    function activateQueryLayers() {
      const tokens = getQueryLayerTokens();
      if (!tokens.length) return;

      const includesDefaultCouncilDistrict = tokens.some((token) => {
        const control = queryLayerControls.get(token);
        return control && control.layer === councilDistrictFillLayer;
      });
      const includesOtherLayer = tokens.some((token) => {
        const control = queryLayerControls.get(token);
        return control && control.layer !== councilDistrictFillLayer;
      });
      if (includesOtherLayer && !includesDefaultCouncilDistrict && map.hasLayer(councilDistrictFillLayer)) {
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

    function appendLayerLabelContents(labelElement, input, label, geometryType, options) {
      const settings = options || {};
      const text = settings.href ? document.createElement("a") : document.createElement("span");
      text.textContent = label;
      if (settings.href) {
        text.href = settings.href;
        text.className = "maps-layer-reference-link";
        text.target = "_blank";
        text.rel = "noopener";
        text.addEventListener("click", function (event) {
          event.stopPropagation();
        });
      }
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
      const control = {
        input,
        layer,
        group: settings.group || "",
        querySlug: settings.querySlug || queryLayerSlugsByLayer.get(layer) || ""
      };
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

    function createLocationInfoIcon() {
      const icon = document.createElement("span");
      icon.className = "maps-location-info-icon";
      icon.setAttribute("aria-hidden", "true");
      icon.innerHTML = '<svg viewBox="0 0 16 16" focusable="false"><path d="M8 1.5a4.5 4.5 0 0 0-4.5 4.5c0 3.2 4.5 8.5 4.5 8.5s4.5-5.3 4.5-8.5A4.5 4.5 0 0 0 8 1.5Zm0 6.4A1.9 1.9 0 1 1 8 4.1a1.9 1.9 0 0 1 0 3.8Z"/></svg>';
      return icon;
    }

    function createLocationInfoHeader() {
      const header = document.createElement("div");
      const spacer = document.createElement("span");
      const icon = createLocationInfoIcon();
      header.className = "maps-location-info-header";
      icon.title = "Show on You are here card";
      header.appendChild(spacer);
      header.appendChild(icon);
      return header;
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

    function createLayerAccordion(label, controls, open) {
      const details = document.createElement("details");
      const summary = document.createElement("summary");
      const body = document.createElement("div");

      details.className = "maps-layer-accordion";
      details.open = Boolean(open);
      summary.textContent = label;
      body.className = "maps-layer-accordion__body";
      appendLayerControls(body, controls);
      details.appendChild(summary);
      details.appendChild(body);
      return details;
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
      if (layerType === "skywayRoute" || layerType === "ferryRoute") {
        return [
          layerType,
          properties.route_id,
          properties.shape_id,
          getBusRouteTitle(feature)
        ].filter(Boolean).join("|");
      }
      if (layerType === "amtrakRoute" || layerType === "brightlineRoute" || layerType === "sunrailRoute" || layerType === "triRailRoute") {
        return [
          layerType,
          properties.route_id,
          properties.shape_id,
          properties.segment_index,
          getRailRouteTitle(feature)
        ].filter(Boolean).join("|");
      }
      if (layerType === "trainTrack") {
        return [
          layerType,
          properties.id,
          properties.name,
          properties.mtfcc
        ].filter(Boolean).join("|");
      }
      if (layerType === "trainStation") {
        return [
          layerType,
          properties.id,
          properties.name
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
      if (layerType === "skywayStation" || layerType === "ferryLanding") {
        return [
          layerType,
          properties.stop_id,
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
      if (layerType === "skywayRoute" || layerType === "ferryRoute") return getBusRouteTitle(feature);
      if (layerType === "amtrakRoute" || layerType === "brightlineRoute" || layerType === "sunrailRoute" || layerType === "triRailRoute") return getRailRouteTitle(feature);
      if (layerType === "trainTrack") return getTrainTrackTitle(feature);
      if (layerType === "trainStation") return getTrainStationTitle(feature);
      if (layerType === "busStop") return properties.stop_name || "JTA Bus Stop";
      if (layerType === "skywayStation") return properties.stop_name || "JTA Skyway Station";
      if (layerType === "ferryLanding") return properties.stop_name || "Ferry Landing";
      if (layerType === "policeStation") return properties.name || "JSO Substation";
      if (layerType === "neighborhoodOrganization") return properties.name || "Neighborhood Organization";
      if (layerType === "school") return getSchoolName(feature);
      if (layerType === "fldoeSchool") return getFldoeSchoolName(feature);
      if (layerType === "place") return properties.name || "Map location";
      return getBoundaryTitle(feature, layerType);
    }

    function createPinnedCardContent(card) {
      if (card.layerType === "userLocation") {
        return createYouAreHereCard();
      }
      if (card.layerType === "busRoute") {
        return createBusRoutePopup(card.feature);
      }
      if (card.layerType === "skywayRoute" || card.layerType === "ferryRoute") {
        return createBusRoutePopup(card.feature);
      }
      if (card.layerType === "amtrakRoute" || card.layerType === "brightlineRoute" || card.layerType === "sunrailRoute" || card.layerType === "triRailRoute") {
        return createRailRoutePopup(card.feature);
      }
      if (card.layerType === "trainTrack") {
        return createTrainTrackPopup(card.feature);
      }
      if (card.layerType === "trainStation") {
        return createTrainStationPopup(card.feature);
      }
      if (card.layerType === "busStop") {
        return createBusStopPopup(card.feature);
      }
      if (card.layerType === "skywayStation") {
        return createTransitStopPopup(card.feature, "JTA Skyway Station");
      }
      if (card.layerType === "ferryLanding") {
        return createTransitStopPopup(card.feature, "Ferry Landing");
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
      updateOpacityRangeVisual(governmentLayerOpacityInput, governmentLayerOpacityLabel, governmentOverlayOpacity, "Overlay opacity");
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
      elevationColorLayer.setOpacity(nextOpacity);
      elevationContoursOverviewLayer.setOpacity(nextOpacity);
      elevationContoursDetailLayer.setOpacity(nextOpacity);
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

    function appendGeographyLayerRow(parent, name, overlayLayer, borderLayer, options) {
      const row = document.createElement("div");
      const layerLabel = document.createElement("label");
      const layerInput = document.createElement("input");
      const locationLabel = document.createElement("label");
      const locationInput = document.createElement("input");
      const settings = options || {};
      const overlayControl = { layer: overlayLayer, group: "boundaries" };
      const borderControl = { layer: borderLayer, group: "boundaries" };
      const geographyControl = { overlayControl, borderControl };
      registerBoundaryLayerStack([overlayLayer, borderLayer]);
      let allowMultipleOnNextChange = false;

      row.className = "maps-layer-group-row";
      layerLabel.className = "maps-layer-group-row__name";
      layerInput.type = "checkbox";
      layerInput.className = "leaflet-control-layers-selector";
      appendLayerLabelContents(layerLabel, layerInput, name, "polygon", {
        href: settings.href
      });

      if (settings.locationLayerType) {
        locationLabel.className = "maps-location-info-column";
        locationInput.type = "checkbox";
        locationInput.className = "leaflet-control-layers-selector";
        locationInput.setAttribute("aria-label", `Show ${name} on You are here card`);
        locationInput.checked = selectedLocationInfoLayerTypes.has(settings.locationLayerType);
        locationInput.addEventListener("change", function () {
          if (locationInput.checked) {
            selectedLocationInfoLayerTypes.add(settings.locationLayerType);
          } else {
            selectedLocationInfoLayerTypes.delete(settings.locationLayerType);
          }
          updateYouAreHereCard();
        });
        locationLabel.appendChild(locationInput);
        locationInfoControls.push({
          input: locationInput,
          label: name.replace(/\*$/, ""),
          layer: overlayLayer,
          layerType: settings.locationLayerType
        });
      }

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
      if (map.hasLayer(overlayLayer) || map.hasLayer(borderLayer)) {
        trackBoundaryLayerStackSelection(overlayLayer);
      }
      row.appendChild(layerLabel);
      if (settings.locationLayerType) {
        row.appendChild(locationLabel);
      }
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
          layersControlElement = container;
          overlays.appendChild(createLocationInfoHeader());
          overlays.appendChild(createLayerHeading("Government"));
          appendGeographyLayerRow(overlays, "City Council District", councilDistrictFillLayer, councilDistrictBorderLayer, { locationLayerType: "district" });
          appendGeographyLayerRow(overlays, "City Council District At Large", councilAtLargeFillLayer, councilAtLargeBorderLayer, { locationLayerType: "atLarge" });
          appendGeographyLayerRow(overlays, "School Board Districts", schoolBoardDistrictFillLayer, schoolBoardDistrictBorderLayer, { locationLayerType: "schoolBoard" });
          appendGeographyLayerRow(overlays, "Florida House", floridaHouseFillLayer, floridaHouseBorderLayer, { locationLayerType: "floridaHouse" });
          appendGeographyLayerRow(overlays, "Florida Senate", floridaSenateFillLayer, floridaSenateBorderLayer, { locationLayerType: "floridaSenate" });
          appendGeographyLayerRow(overlays, "U.S. House", congressionalDistrictFillLayer, congressionalDistrictBorderLayer, { locationLayerType: "congressional" });
          appendGeographyLayerRow(overlays, "U.S. Senators", usSenateFillLayer, usSenateBorderLayer, { locationLayerType: "usSenate" });
          appendGeographyLayerRow(overlays, "Cities", cityFillLayer, cityBorderLayer, { locationLayerType: "city" });
          appendGeographyLayerRow(overlays, "Counties", countyFillLayer, countyBorderLayer, { locationLayerType: "county" });
          appendGeographyLayerRow(overlays, "Zip Codes", zipCodeFillLayer, zipCodeBorderLayer, { locationLayerType: "zipCode" });
          overlays.appendChild(createLayerSubheading("Elections"));
          appendGeographyLayerRow(overlays, "Voting Precincts", votingPrecinctFillLayer, votingPrecinctBorderLayer, { locationLayerType: "votingPrecinct" });
          appendLayerControls(overlays, [
            createBoundaryLayerInput("Polling Locations", pollingLocationsLayer)
          ]);
          overlays.appendChild(createLayerHeading("Neighborhood"));
          appendGeographyLayerRow(overlays, "Neighborhoods", neighborhoodFillLayer, neighborhoodBorderLayer, { locationLayerType: "neighborhood" });
          appendLayerControls(overlays, [
            createBoundaryLayerInput("Neighborhood Organizations", neighborhoodOrganizationsLayer)
          ]);
          appendGeographyLayerRow(overlays, "Citizens Planning Advisory Committee (CPACs)", cpacFillLayer, cpacBorderLayer, { locationLayerType: "cpac" });
          overlays.appendChild(createLayerHeading("Jacksonville Sheriff's Office"));
          appendGeographyLayerRow(overlays, "JSO Districts", jsoDistrictFillLayer, jsoDistrictBorderLayer, { locationLayerType: "jsoDistrict" });
          appendGeographyLayerRow(overlays, "JSO Subsections", jsoSubsectionFillLayer, jsoSubsectionBorderLayer, { locationLayerType: "jsoSubsector" });
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JSO Substations", jsoPoliceStationsLayer)
          ]);
          const terrainHazardsHeading = createLayerHeading("Terrain & Hazards");
          terrainHazardsHeading.classList.add("maps-layer-heading--terrain-hazards");
          overlays.appendChild(terrainHazardsHeading);
          appendLayerControls(overlays, [
            createBoundaryLayerInput("Elevation (Color)", elevationColorLayer, {
              countable: false,
              geometryType: "polygon"
            }),
            createBoundaryLayerInput("Elevation Contours", elevationContoursLayer, {
              countable: false,
              geometryType: "line"
            })
          ]);
          appendGeographyLayerRow(overlays, "Flood Zones", floodZoneFillLayer, floodZoneBorderLayer, {
            locationLayerType: "floodZone"
          });
          appendGeographyLayerRow(overlays, "Evacuation Zones", evacuationZoneFillLayer, evacuationZoneBorderLayer, {
            locationLayerType: "evacuationZone"
          });
          overlays.appendChild(createLayerHeading("Transportation"));
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JTA Bus Routes", busRoutesLayer, { geometryType: "line" })
          ]);
          overlays.appendChild(createBusRouteFilterSection());
          appendLayerControls(overlays, [
            createBoundaryLayerInput("JTA Bus Stops", busStopsLayer, { countLabel: "JTA Bus Stops" }),
            createBoundaryLayerInput("JTA Skyway Routes", skywayRoutesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("JTA Skyway Stations", skywayStationsLayer, { countLabel: "JTA Skyway Stations" }),
            createBoundaryLayerInput("St. Johns River Ferry", ferryRouteLayer, { geometryType: "line" }),
            createBoundaryLayerInput("Ferry Landings", ferryLandingsLayer, { countLabel: "Ferry Landings" })
          ]);
          const interstateControls = interstateRouteNumbers.map((routeNumber) => (
            createBoundaryLayerInput(`I-${routeNumber}`, interstateLayersByRouteNumber.get(routeNumber), { geometryType: "line" })
          ));
          const allInterstateControls = [
            createLayerGroupToggle("All Interstates", interstateControls),
            createBoundaryLayerInput("Duval Interstates", duvalInterstatesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("NE FL Interstates", northeastFloridaInterstatesLayer, { geometryType: "line" }),
            ...interstateControls
          ];
          overlays.appendChild(createLayerAccordion("Interstates", allInterstateControls, false));
          const trainControls = [
            createBoundaryLayerInput("Train Tracks", trainTracksLayer, { geometryType: "line" }),
            createBoundaryLayerInput("Amtrak Routes", amtrakRoutesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("Amtrak Stations", trainStationsLayer, { countLabel: "Amtrak Stations" }),
            createBoundaryLayerInput("Brightline Routes", brightlineRoutesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("Brightline Stations", brightlineStationsLayer, { countLabel: "Brightline Stations" }),
            createBoundaryLayerInput("SunRail Routes", sunrailRoutesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("SunRail Stations", sunrailStationsLayer, { countLabel: "SunRail Stations" }),
            createBoundaryLayerInput("Tri-Rail Routes", triRailRoutesLayer, { geometryType: "line" }),
            createBoundaryLayerInput("Tri-Rail Stations", triRailStationsLayer, { countLabel: "Tri-Rail Stations" })
          ];
          overlays.appendChild(createLayerAccordion("Trains", trainControls, false));
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
          overlays.appendChild(createLayerHeading("Health"));
          appendGeographyLayerRow(overlays, "Health Zones*", healthZoneFillLayer, healthZoneBorderLayer, {
            href: "/maps/references/#health",
            locationLayerType: "healthZone"
          });
          const layerHeaderActions = createLayerHeaderActions();
          layersControlApi = setupCollapsibleMapControl(container, "Layers", list, {
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

    function addElevationClickHandler() {
      let elevationRequestId = 0;

      map.on("click", async function (event) {
        if (!map.hasLayer(elevationColorLayer) && !map.hasLayer(elevationContoursLayer)) return;
        const target = event.originalEvent && event.originalEvent.target;
        if (target && target.closest && target.closest(".leaflet-interactive, .leaflet-marker-icon, .leaflet-control")) return;

        const requestId = ++elevationRequestId;
        const popup = L.popup({ maxWidth: 260 })
          .setLatLng(event.latlng)
          .setContent("Looking up elevation…")
          .openOn(map);
        const params = new URLSearchParams({
          includeDate: "false",
          units: "Feet",
          wkid: "4326",
          x: String(event.latlng.lng),
          y: String(event.latlng.lat)
        });

        try {
          const response = await fetch(`https://epqs.nationalmap.gov/v1/json?${params}`);
          if (!response.ok) throw new Error(`Elevation query returned ${response.status}`);
          const result = await response.json();
          if (requestId !== elevationRequestId || popup !== map._popup) return;
          const elevation = Number(result && result.value);
          if (!Number.isFinite(elevation)) throw new Error("Elevation query returned no value");

          const content = document.createElement("div");
          const heading = document.createElement("strong");
          const value = document.createElement("div");
          const note = document.createElement("small");
          heading.textContent = "Approximate elevation";
          value.textContent = `${elevation.toFixed(1)} feet`;
          note.textContent = "USGS 3DEP interpolated ground elevation; not a surveyed measurement.";
          content.append(heading, value, note);
          popup.setContent(content).update();
        } catch (error) {
          if (requestId !== elevationRequestId || popup !== map._popup) return;
          popup.setContent("Elevation is temporarily unavailable.").update();
          console.warn(error);
        }
      });
    }

    function addElevationLegend() {
      const legendItems = [
        ["rgb(49 130 189)", "Below 0 ft"],
        ["rgb(107 174 214)", "0–5 ft"],
        ["rgb(166 219 160)", "5–10 ft"],
        ["rgb(255 255 179)", "10–20 ft"],
        ["rgb(254 204 92)", "20–30 ft"],
        ["rgb(253 141 60)", "30–50 ft"],
        ["rgb(244 109 67)", "50–60 ft"],
        ["rgb(215 48 39)", "60–80 ft"],
        ["rgb(165 0 38)", "80–120 ft"],
        ["rgb(103 0 31)", "120+ ft"]
      ];
      const ElevationLegendControl = L.Control.extend({
        options: { position: "bottomleft" },
        onAdd: function () {
          const container = L.DomUtil.create("div", "maps-elevation-legend");
          const heading = document.createElement("strong");
          heading.textContent = "Approximate elevation";
          container.appendChild(heading);
          legendItems.forEach(([color, label]) => {
            const row = document.createElement("div");
            const swatch = document.createElement("span");
            const text = document.createElement("span");
            row.className = "maps-elevation-legend__row";
            swatch.className = "maps-elevation-legend__swatch";
            swatch.style.background = color;
            text.textContent = label;
            row.append(swatch, text);
            container.appendChild(row);
          });
          this._container = container;
          return container;
        },
        update: function () {
          if (this._container) {
            this._container.classList.toggle("is-visible", map.hasLayer(elevationColorLayer));
          }
        }
      });
      const legend = new ElevationLegendControl();
      legend.addTo(map);
      map.on("layeradd layerremove", () => legend.update());
      legend.update();
    }

    function addMapContextMenuHandlers() {
      map.on("contextmenu", function (event) {
        if (event.originalEvent && event.originalEvent._mapsContextMenuHandled) return;
        showMapContextMenu(event);
      });
      map.on("click movestart zoomstart popupopen", hideMapContextMenu);
      map.on("popupopen", function (event) {
        expandPhotoPopupIfContactWraps(event.popup);
        makePopupDraggable(event.popup);
      });
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
      historicMapDefinitions.forEach((definition) => {
        registerQueryLayer([definition.slug].concat(definition.aliases), definition.layer, { slug: definition.slug });
      });
      registerQueryLayer(["councildistrict", "councildistricts", "citycouncildistrict", "citycouncildistricts"], councilDistrictFillLayer, { group: "boundaries", slug: "citycouncildistrict", alternateLayers: [councilDistrictBorderLayer] });
      registerQueryLayer(["councilatlarge", "councildistrictatlarge", "citycouncilatlarge", "citycouncildistrictatlarge"], councilAtLargeFillLayer, { group: "boundaries", slug: "citycouncilatlarge", alternateLayers: [councilAtLargeBorderLayer] });
      registerQueryLayer(["schoolboard", "schoolboarddistrict", "schoolboarddistricts"], schoolBoardDistrictFillLayer, { group: "boundaries", slug: "schoolboarddistricts", alternateLayers: [schoolBoardDistrictBorderLayer] });
      registerQueryLayer(["cities", "cityboundaries"], cityFillLayer, { group: "boundaries", slug: "cities", alternateLayers: [cityBorderLayer] });
      registerQueryLayer(["county", "counties", "countyboundaries", "duvalcounty", "duvalcountyboundary", "countyboundary"], countyFillLayer, { group: "boundaries", slug: "counties", alternateLayers: [countyBorderLayer] });
      registerQueryLayer(["votingprecinct", "votingprecincts", "precinct", "precincts"], votingPrecinctFillLayer, { group: "boundaries", slug: "votingprecincts", alternateLayers: [votingPrecinctBorderLayer] });
      registerQueryLayer(["pollinglocation", "pollinglocations", "polls"], pollingLocationsLayer, { slug: "pollinglocations" });
      registerQueryLayer(["floridahouse", "house", "statehouse"], floridaHouseFillLayer, { group: "boundaries", slug: "floridahouse", alternateLayers: [floridaHouseBorderLayer] });
      registerQueryLayer(["floridasenate", "senate", "statesenate"], floridaSenateFillLayer, { group: "boundaries", slug: "floridasenate", alternateLayers: [floridaSenateBorderLayer] });
      registerQueryLayer(["zip", "zips", "zipcode", "zipcodes", "zcta", "zctas"], zipCodeFillLayer, { group: "boundaries", slug: "zipcodes", alternateLayers: [zipCodeBorderLayer] });
      registerQueryLayer(["ushouse", "congress", "congressional", "congressionaldistrict", "congressionaldistricts"], congressionalDistrictFillLayer, { group: "boundaries", slug: "ushouse", alternateLayers: [congressionalDistrictBorderLayer] });
      registerQueryLayer(["ussenate", "ussenators", "floridaussenators", "floridasenators"], usSenateFillLayer, { group: "boundaries", slug: "ussenators", alternateLayers: [usSenateBorderLayer] });
      registerQueryLayer(["neighborhood", "neighborhoods"], neighborhoodFillLayer, { group: "boundaries", slug: "neighborhoods", alternateLayers: [neighborhoodBorderLayer] });
      registerQueryLayer(["cpac", "cpacs", "planningdistricts"], cpacFillLayer, { group: "boundaries", slug: "cpacs", alternateLayers: [cpacBorderLayer] });
      registerQueryLayer(["health", "healthzone", "healthzones"], healthZoneFillLayer, { group: "boundaries", slug: "healthzones", alternateLayers: [healthZoneBorderLayer] });
      registerQueryLayer(["healthzones-byzipcodes", "healthzonesbyzipcodes", "healthzonesbyzip", "healthzoneslistedzips"], healthZoneByZipCodeLayer, { group: "boundaries", slug: "healthzones-byzipcodes" });
      registerQueryLayer(["elevation", "elevationcolor", "terrain", "tintedhillshade", "3dep"], elevationColorLayer, { slug: "elevation" });
      registerQueryLayer(["elevationcontours", "contours", "5ftcontours", "terraincontours"], elevationContoursLayer, { slug: "elevationcontours" });
      registerQueryLayer(["flood", "floodzone", "floodzones", "fema"], floodZoneFillLayer, { group: "boundaries", slug: "floodzones", alternateLayers: [floodZoneBorderLayer] });
      registerQueryLayer(["evacuation", "evacuationzone", "evacuationzones", "evaczones"], evacuationZoneFillLayer, { group: "boundaries", slug: "evacuationzones", alternateLayers: [evacuationZoneBorderLayer] });
      registerQueryLayer(["jsodistrict", "jsodistricts", "sheriffdistricts"], jsoDistrictFillLayer, { group: "boundaries", slug: "jsodistricts", alternateLayers: [jsoDistrictBorderLayer] });
      registerQueryLayer(["jsosubsection", "jsosubsections", "jsosubsector", "jsosubsectors"], jsoSubsectionFillLayer, { group: "boundaries", slug: "jsosubsections", alternateLayers: [jsoSubsectionBorderLayer] });
      registerQueryLayer(["neighborhoodorganizations", "neighborhoodorgs", "neighborhoodpoints"], neighborhoodOrganizationsLayer, { slug: "neighborhoodorganizations" });
      registerQueryLayer(["substations", "jsosubstations", "policestations"], jsoPoliceStationsLayer, { slug: "substations" });
      interstateRouteNumbers.forEach((routeNumber) => {
        registerQueryLayer(
          [`i${routeNumber}`, `interstate${routeNumber}`],
          interstateLayersByRouteNumber.get(routeNumber),
          { slug: `i${routeNumber}` }
        );
      });
      registerQueryLayer(["duvalinterstates", "duvalhighways"], duvalInterstatesLayer, { slug: "duvalinterstates" });
      registerQueryLayer(["neflinterstates", "northeastfloridainterstates"], northeastFloridaInterstatesLayer, { slug: "neflinterstates" });
      registerQueryLayer(["traintracks", "railroads", "railroad", "rails"], trainTracksLayer, { slug: "traintracks" });
      registerQueryLayer(["amtrakstations", "trainstations", "railroadstations", "railstations", "stations"], trainStationsLayer, { slug: "amtrakstations" });
      registerQueryLayer(["amtrakroutes", "amtrak"], amtrakRoutesLayer, { slug: "amtrakroutes" });
      registerQueryLayer(["brightlineroutes", "brightline"], brightlineRoutesLayer, { slug: "brightlineroutes" });
      registerQueryLayer(["brightlinestations"], brightlineStationsLayer, { slug: "brightlinestations" });
      registerQueryLayer(["sunrailroutes", "sunrail"], sunrailRoutesLayer, { slug: "sunrailroutes" });
      registerQueryLayer(["sunrailstations"], sunrailStationsLayer, { slug: "sunrailstations" });
      registerQueryLayer(["trirailroutes", "tri-railroutes", "trirail", "tri-rail"], triRailRoutesLayer, { slug: "trirailroutes" });
      registerQueryLayer(["trirailstations", "tri-railstations"], triRailStationsLayer, { slug: "trirailstations" });
      registerQueryLayer(["busroutes", "jtabusroutes", "routes"], busRoutesLayer, { slug: "busroutes" });
      registerQueryLayer(["busstops", "jtabusstops", "stops"], busStopsLayer, { slug: "busstops" });
      registerQueryLayer(["skywayroutes", "jtaskywayroutes", "skyway"], skywayRoutesLayer, { slug: "skywayroutes" });
      registerQueryLayer(["skywaystations", "jtaskywaystations"], skywayStationsLayer, { slug: "skywaystations" });
      registerQueryLayer(["ferry", "stjohnsriverferry", "stjohnsferry"], ferryRouteLayer, { slug: "ferry" });
      registerQueryLayer(["ferrylandings", "mayportferrylanding", "fortgeorgeferrylanding"], ferryLandingsLayer, { slug: "ferrylandings" });
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
      if (layerType === "votingPrecinct") {
        return getStringColorNumber(String(properties.GEOID || "").replace(/^12031-/, ""));
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
      if (layerType === "usSenate") {
        return getStringColorNumber(properties.state_geoid || properties.state_abbr || properties.label || "U.S. Senators");
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
      const properties = feature.properties || {};
      if (layerType === "floodZone") {
        const zone = String(properties.FLD_ZONE || "").trim().toUpperCase();
        if (zone === "VE") return "#d7191c";
        if (zone === "A" || zone === "AE") return "#2c7bb6";
        if (zone === "AH" || zone === "AO") return "#00a6ca";
        if (zone.startsWith("0.2 PCT")) return "#fdae61";
        if (zone === "OPEN WATER") return "#74add1";
        return "#abd9e9";
      }
      if (layerType === "evacuationZone") {
        const colorsByZone = {
          "ZONE A": "#ff0000",
          "ZONE B": "#ffaa00",
          "ZONE C": "#ffff00",
          "ZONE D": "#55ff00",
          "ZONE E": "#c500ff",
          "ZONE F": "#ffbee8"
        };
        return colorsByZone[String(properties.EVAC_TYPE || "").trim().toUpperCase()] || "#ffbee8";
      }
      if (layerType === "healthZone" && properties.excluded_health_zone) {
        return "#000000";
      }
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
      if (layerType === "votingPrecinct") {
        return mode === "border" ? votingPrecinctBorderLayer : votingPrecinctFillLayer;
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
      if (layerType === "usSenate") {
        return mode === "border" ? usSenateBorderLayer : usSenateFillLayer;
      }
      if (layerType === "healthZone") {
        return mode === "border" ? healthZoneBorderLayer : healthZoneFillLayer;
      }
      if (layerType === "floodZone") {
        return mode === "border" ? floodZoneBorderLayer : floodZoneFillLayer;
      }
      if (layerType === "evacuationZone") {
        return mode === "border" ? evacuationZoneBorderLayer : evacuationZoneFillLayer;
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
      if (layerType === "votingPrecinct") {
        const precinct = String(properties.GEOID || "").replace(/^12031-/, "");
        return precinct ? `Voting Precinct ${precinct}` : "Voting Precinct";
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
      if (layerType === "usSenate") {
        return properties.label || "Florida U.S. Senators";
      }
      if (layerType === "healthZone") {
        if (properties.excluded_health_zone) {
          return properties.label || "Excluded from Health Zones";
        }
        return properties.label || (properties.health_zone ? `Health Zone ${properties.health_zone}` : "Health Zone");
      }
      if (layerType === "floodZone") {
        const zone = String(properties.FLD_ZONE || "").trim();
        return zone ? `Flood Zone ${zone}` : "Flood Zone";
      }
      if (layerType === "evacuationZone") {
        const zone = String(properties.EVAC_TYPE || "").trim();
        return zone ? `Evacuation ${zone.replace(/^ZONE\s+/i, "Zone ")}` : "Evacuation Zone";
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
        return formatNameWithParty(
          properties.council_member_name || properties.C_NAME || "",
          properties.council_member_party
        );
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
        return formatNameWithParty(
          properties.state_house_member_name || properties.HSE_NAME || properties.DELEGATES || "",
          properties.state_house_member_party
        );
      }
      if (layerType === "floridaSenate") {
        return formatNameWithParty(
          properties.state_senate_member_name || properties.SEN_NAME || "",
          properties.state_senate_member_party
        );
      }
      if (layerType === "zipCode") {
        return "";
      }
      if (layerType === "congressional") {
        return formatNameWithParty(
          properties.congressional_member_name || "",
          properties.congressional_member_party
        );
      }
      if (layerType === "usSenate") {
        return "";
      }
      if (layerType === "healthZone") {
        if (properties.excluded_health_zone) {
          return properties.excluded_group_label || "Excluded from Health Zones";
        }
        return properties.zip_codes_label ? `ZIP Codes: ${properties.zip_codes_label}` : "";
      }
      if (layerType === "floodZone") {
        const subtype = String(properties.ZONE_SUBTY || "").trim();
        return subtype && subtype !== String(properties.FLD_ZONE || "").trim() ? subtype : "FEMA flood hazard area";
      }
      if (layerType === "evacuationZone") {
        return "Duval County hurricane evacuation zone";
      }
      if (layerType === "jsoDistrict") {
        return "Jacksonville Sheriff's Office";
      }
      if (layerType === "jsoSubsector") {
        return [properties.SECTOR ? `Sector ${properties.SECTOR}` : "", properties.DISTRICT ? `District ${properties.DISTRICT}` : ""].filter(Boolean).join(" / ");
      }
      return properties.MEMBER_NAM || "";
    }

    function getPartyAbbreviation(party) {
      const value = String(party || "").trim();
      const normalized = value.toLowerCase();
      const abbreviations = {
        democratic: "D",
        democrat: "D",
        republican: "R",
        independent: "I",
        nonpartisan: "NP"
      };
      if (!value) return "";
      if (value.length <= 3) return value.toUpperCase();
      return abbreviations[normalized] || value;
    }

    function formatNameWithParty(name, party) {
      const displayName = String(name || "").trim();
      const abbreviation = getPartyAbbreviation(party);
      if (!displayName) return abbreviation ? `(${abbreviation})` : "";
      return abbreviation ? `${displayName} (${abbreviation})` : displayName;
    }

    function getPhoneHref(phone) {
      const digits = String(phone || "").replace(/\D/g, "");
      if (!digits) return "";
      if (digits.length === 10) return `tel:+1${digits}`;
      if (digits.length === 11 && digits.startsWith("1")) return `tel:+${digits}`;
      return `tel:${digits}`;
    }

    function formatPhoneNumber(phone) {
      const digits = String(phone || "").replace(/\D/g, "");
      if (digits.length === 10) {
        return `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
      }
      if (digits.length === 11 && digits.startsWith("1")) {
        return `(${digits.slice(1, 4)}) ${digits.slice(4, 7)}-${digits.slice(7)}`;
      }
      return phone;
    }

    function appendContactLink(popup, text, href) {
      if (!text || !href) return;
      const link = document.createElement("a");
      link.href = href;
      link.textContent = text;
      if (/^(mailto|tel):/.test(href)) {
        link.classList.add("maps-contact-link");
      }
      if (/^https?:\/\//.test(href)) {
        link.target = "_blank";
        link.rel = "noopener";
      }
      popup.appendChild(link);
    }

    function appendContactLine(popup, phone, email) {
      appendContactLink(popup, formatPhoneNumber(phone), getPhoneHref(phone));
      appendContactLink(popup, email, email ? `mailto:${email}` : "");
    }

    function formatOneDecimal(value) {
      return value.toLocaleString(undefined, {
        maximumFractionDigits: 1,
        minimumFractionDigits: 1
      });
    }

    function appendCensusReporterLine(popup, label, value) {
      const line = document.createElement("span");
      line.textContent = `${label}: ${value}`;
      popup.appendChild(line);
    }

    function getCensusReporterGeography(geoid) {
      if (!geoid) return Promise.resolve(null);
      if (!censusReporterGeographyPromises.has(geoid)) {
        censusReporterGeographyPromises.set(
          geoid,
          fetchJsonData(`https://api.censusreporter.org/1.0/geo/latest/${geoid}`, `Census Reporter ${geoid}`)
        );
      }
      return censusReporterGeographyPromises.get(geoid);
    }

    function appendCensusReporterStats(popup, geoid) {
      getCensusReporterGeography(geoid)
        .then((geography) => {
          const properties = (geography && geography.properties) || {};
          const population = Number(properties.population);
          const landArea = Number(properties.aland);
          const squareMiles = landArea / squareMetersPerSquareMile;
          if (Number.isFinite(population)) {
            appendCensusReporterLine(popup, "Population", population.toLocaleString());
          }
          if (Number.isFinite(squareMiles) && squareMiles > 0) {
            appendCensusReporterLine(popup, "Square mileage", formatOneDecimal(squareMiles));
            if (Number.isFinite(population)) {
              appendCensusReporterLine(popup, "People per square mile", Math.round(population / squareMiles).toLocaleString());
            }
          }
        })
        .catch((error) => {
          console.warn(error);
        });
    }

    function appendSchoolBoardMemberPopupDetails(popup, properties) {
      if (properties.member_image_url) {
        const image = document.createElement("img");
        popup.classList.add("maps-district-popup--with-photo");
        image.src = properties.member_image_url;
        image.alt = properties.member_name || "School Board member";
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      appendContactLine(popup, properties.member_phone, properties.member_email);

      [
        properties.member_role === "Board Member" ? "" : properties.member_role
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
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
        return properties.congressional_member_website_url || "";
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
      if (layerType === "schoolBoard") {
        return properties.member_source_url || "";
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

    function getLineSegmentIntersection(segmentStart, segmentEnd, boundaryStart, boundaryEnd) {
      const segmentX = segmentEnd[0] - segmentStart[0];
      const segmentY = segmentEnd[1] - segmentStart[1];
      const boundaryX = boundaryEnd[0] - boundaryStart[0];
      const boundaryY = boundaryEnd[1] - boundaryStart[1];
      const denominator = (segmentX * boundaryY) - (segmentY * boundaryX);
      if (Math.abs(denominator) < 1e-12) return null;

      const startX = boundaryStart[0] - segmentStart[0];
      const startY = boundaryStart[1] - segmentStart[1];
      const segmentPosition = ((startX * boundaryY) - (startY * boundaryX)) / denominator;
      const boundaryPosition = ((startX * segmentY) - (startY * segmentX)) / denominator;
      if (segmentPosition < -1e-10 || segmentPosition > 1 + 1e-10) return null;
      if (boundaryPosition < -1e-10 || boundaryPosition > 1 + 1e-10) return null;

      const clampedPosition = Math.max(0, Math.min(1, segmentPosition));
      return {
        position: clampedPosition,
        point: [
          segmentStart[0] + (segmentX * clampedPosition),
          segmentStart[1] + (segmentY * clampedPosition)
        ]
      };
    }

    function areCoordinatesEqual(first, second) {
      return first && second &&
        Math.abs(first[0] - second[0]) < 1e-10 &&
        Math.abs(first[1] - second[1]) < 1e-10;
    }

    function appendCoordinate(coordinates, coordinate) {
      if (!coordinates.length || !areCoordinatesEqual(coordinates[coordinates.length - 1], coordinate)) {
        coordinates.push(coordinate);
      }
    }

    function getSegmentBoundaryIntersections(segmentStart, segmentEnd, rings) {
      const intersections = [];
      rings.forEach((ring) => {
        for (let index = 1; index < ring.length; index += 1) {
          const intersection = getLineSegmentIntersection(segmentStart, segmentEnd, ring[index - 1], ring[index]);
          if (!intersection) continue;
          if (intersections.some((item) => Math.abs(item.position - intersection.position) < 1e-10)) continue;
          intersections.push(intersection);
        }
      });
      return intersections.sort((first, second) => first.position - second.position);
    }

    function clipLineCoordinateSequenceToFeature(coordinates, polygonFeature) {
      const geometry = polygonFeature.geometry || {};
      const rings = getPolygonRingsFromFeatureGeometry(geometry);
      const clippedSequences = [];
      let currentSequence = [];
      if (!coordinates || coordinates.length < 2 || !rings.length) return clippedSequences;

      for (let index = 1; index < coordinates.length; index += 1) {
        const segmentStart = coordinates[index - 1];
        const segmentEnd = coordinates[index];
        const splitPoints = [
          { position: 0, point: segmentStart },
          ...getSegmentBoundaryIntersections(segmentStart, segmentEnd, rings),
          { position: 1, point: segmentEnd }
        ];

        for (let splitIndex = 1; splitIndex < splitPoints.length; splitIndex += 1) {
          const start = splitPoints[splitIndex - 1].point;
          const end = splitPoints[splitIndex].point;
          if (areCoordinatesEqual(start, end)) continue;
          const midpoint = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2];
          const keepSegment = isPointInFeatureGeometry(midpoint, geometry) ||
            isPointInFeatureGeometry(start, geometry) ||
            isPointInFeatureGeometry(end, geometry);

          if (keepSegment) {
            appendCoordinate(currentSequence, start);
            appendCoordinate(currentSequence, end);
          } else if (currentSequence.length > 1) {
            clippedSequences.push(currentSequence);
            currentSequence = [];
          } else {
            currentSequence = [];
          }
        }
      }

      if (currentSequence.length > 1) {
        clippedSequences.push(currentSequence);
      }
      return clippedSequences;
    }

    function clipLineGeometryToFeature(lineGeometry, polygonFeature) {
      if (!lineGeometry || !lineGeometry.coordinates || !polygonFeature || !polygonFeature.geometry) return null;
      const sourceSequences = lineGeometry.type === "LineString"
        ? [lineGeometry.coordinates]
        : lineGeometry.type === "MultiLineString"
          ? lineGeometry.coordinates || []
          : [];
      const clippedSequences = sourceSequences.flatMap((coordinates) => {
        return clipLineCoordinateSequenceToFeature(coordinates, polygonFeature);
      });

      if (!clippedSequences.length) return null;
      if (clippedSequences.length === 1) {
        return { type: "LineString", coordinates: clippedSequences[0] };
      }
      return { type: "MultiLineString", coordinates: clippedSequences };
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

    function appendActivePointCounts(popup, feature, boundaryTitle, excludedLayers) {
      const excluded = excludedLayers || [];
      const activeCounts = countablePointLayers
        .filter((pointLayer) => (
          pointLayer.layer !== pollingLocationsLayer &&
          map.hasLayer(pointLayer.layer) &&
          !excluded.includes(pointLayer.layer)
        ))
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

    function getVotingPrecinctNumber(feature) {
      return String((feature.properties || {}).GEOID || "").replace(/^12031-/, "");
    }

    function findPollingLocationForPrecinct(feature) {
      const precinct = getVotingPrecinctNumber(feature);
      let pollingFeature;
      if (!precinct) return pollingFeature;

      pollingLocationsLayer.eachLayer((layer) => {
        const candidate = layer.feature;
        const candidatePrecincts = String((candidate && candidate.properties || {}).precinct || "")
          .split(",")
          .map((value) => value.trim());
        if (!pollingFeature && candidatePrecincts.includes(precinct)) {
          pollingFeature = candidate;
        }
      });
      return pollingFeature;
    }

    function clearVotingPrecinctPollingPointer(precinct) {
      if (precinct && precinct !== votingPrecinctPollingPointerPrecinct) return;
      if (votingPrecinctPollingPointer) {
        map.removeLayer(votingPrecinctPollingPointer);
      }
      votingPrecinctPollingPointer = undefined;
      votingPrecinctPollingPointerPrecinct = "";
    }

    function showVotingPrecinctPollingPointer(feature) {
      const pollingFeature = findPollingLocationForPrecinct(feature);
      const coordinates = pollingFeature && pollingFeature.geometry && pollingFeature.geometry.coordinates;
      clearVotingPrecinctPollingPointer();
      if (!coordinates || coordinates.length < 2) return;

      const pointerIcon = L.divIcon({
        className: "maps-polling-location-pointer-icon",
        html: '<span class="maps-polling-location-pointer" aria-hidden="true"></span>',
        iconAnchor: [14, 36],
        iconSize: [28, 28]
      });
      votingPrecinctPollingPointer = L.marker([coordinates[1], coordinates[0]], {
        icon: pointerIcon,
        interactive: false,
        keyboard: false,
        pane: "pollingLocationPointerPane",
        zIndexOffset: 1000
      }).addTo(map);
      votingPrecinctPollingPointerPrecinct = getVotingPrecinctNumber(feature);
    }

    function appendVotingPrecinctPollingLocation(popup, feature) {
      const precinct = getVotingPrecinctNumber(feature);
      const pollingFeature = findPollingLocationForPrecinct(feature);
      if (!precinct) return;

      const heading = document.createElement("strong");
      heading.textContent = "Polling location:";
      popup.appendChild(heading);

      if (!pollingFeature) {
        const unavailable = document.createElement("span");
        unavailable.textContent = "No current polling location is listed for this precinct.";
        popup.appendChild(unavailable);
        return;
      }

      const properties = pollingFeature.properties || {};
      [properties.name, properties.address].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
      if (properties.source_url) {
        const sourceLink = document.createElement("a");
        sourceLink.href = "https://www.duvalelections.gov/204/Polling-Location-Finder";
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = "Verify polling location";
        popup.appendChild(sourceLink);
      }
    }

    function createBoundaryPopup(feature, layerType) {
      const popup = document.createElement("div");
      const titleUrl = getBoundaryTitleUrl(feature, layerType);
      const title = titleUrl ? document.createElement("a") : document.createElement("strong");
      const subtitle = getBoundarySubtitle(feature, layerType);
      const pointCountFeature = getPointCountFeature(feature, layerType);
      const boundaryTitle = getBoundaryTitle(feature, layerType);

      popup.className = "maps-district-popup";
      title.className = "maps-popup-title";
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

      if (layerType === "congressional") {
        appendCongressionalPopupDetails(popup, feature.properties || {});
      }

      if (layerType === "usSenate") {
        appendUsSenatorsPopupDetails(popup, feature.properties || {});
      }

      if (layerType === "healthZone") {
        appendHealthZonePopupDetails(popup, feature.properties || {});
      }

      if (layerType === "county") {
        appendCountyCensusReporterDetails(popup, feature.properties || {});
      }

      if (layerType === "zipCode") {
        appendZipCodePopupDetails(popup, feature.properties || {});
      }

      if (layerType === "votingPrecinct") {
        appendVotingPrecinctPollingLocation(popup, feature);
      }

      if (layerType !== "zipCode") {
        appendActivePointCounts(
          popup,
          pointCountFeature,
          boundaryTitle,
          layerType === "votingPrecinct" ? [pollingLocationsLayer] : []
        );
      }

      return popup;
    }

    function appendCensusReporterProfileLink(popup, href) {
      const censusReporterLink = document.createElement("a");
      censusReporterLink.href = href;
      censusReporterLink.target = "_blank";
      censusReporterLink.rel = "noopener";
      censusReporterLink.textContent = "View Census Reporter profile";
      popup.appendChild(censusReporterLink);
    }

    function appendCountyCensusReporterDetails(popup, properties) {
      const countyGeoid = properties.geoid || properties.GEOID || "";
      if (!countyGeoid) return;
      const censusReporterGeoid = `05000US${countyGeoid}`;
      appendCensusReporterProfileLink(popup, `https://censusreporter.org/profiles/${censusReporterGeoid}/`);
      appendCensusReporterStats(popup, censusReporterGeoid);
    }

    function appendZipCodePopupDetails(popup, properties) {
      const zipCode = properties.ZIPCODE || properties.ZCTA5CE20 || properties.GEOID20 || "";
      if (!zipCode) return;
      const censusReporterGeoid = `86000US${zipCode}`;
      appendCensusReporterProfileLink(popup, `https://censusreporter.org/profiles/${censusReporterGeoid}-${zipCode}/`);
      appendCensusReporterStats(popup, censusReporterGeoid);
    }

    function appendHealthZonePopupDetails(popup, properties) {
      [
        properties.exclusion_note,
        properties.assumption_note,
        properties.missing_geometry_note
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
    }

    function appendCongressionalPopupDetails(popup, properties) {
      if (properties.congressional_member_photo_url) {
        const image = document.createElement("img");
        popup.classList.add("maps-district-popup--with-photo");
        image.src = properties.congressional_member_photo_url;
        image.alt = properties.congressional_member_name || "Congressional representative";
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      appendContactLine(popup, properties.congressional_member_phone, properties.congressional_member_email);
      if (properties.congressional_member_contact_url && !properties.congressional_member_email) {
        appendContactLink(popup, "Contact form", properties.congressional_member_contact_url);
      }
    }

    function appendUsSenatorsPopupDetails(popup, properties) {
      createUsSenatorCards(properties).forEach((card) => popup.appendChild(card));
    }

    function createUsSenatorCards(properties, options) {
      const senators = Array.isArray(properties.senators) ? properties.senators : [];
      if (!senators.length) {
        const card = document.createElement("div");
        const line = document.createElement("span");
        card.className = "maps-district-popup";
        line.textContent = "U.S. Senator information unavailable";
        card.appendChild(line);
        return [card];
      }
      return senators.map((senator) => createUsSenatorCard(senator, options));
    }

    function createUsSenatorCard(senator, options) {
      const card = document.createElement("div");
      const title = document.createElement(senator.website_url ? "a" : "strong");
      const name = formatNameWithParty(senator.name, senator.party);
      const displayName = name && options && options.prefixTitle ? `${options.prefixTitle} ${name}` : name;

      card.className = "maps-district-popup maps-district-popup--with-photo maps-senator-card";

      if (senator.photo_url) {
        const image = document.createElement("img");
        image.src = senator.photo_url;
        image.alt = senator.name ? `Photo of Senator ${senator.name}` : "U.S. Senator";
        image.loading = "lazy";
        card.appendChild(image);
      } else {
        card.classList.remove("maps-district-popup--with-photo");
      }

      title.className = "maps-popup-title";
      title.textContent = displayName || "U.S. Senator";
      if (senator.website_url) {
        title.href = senator.website_url;
        title.target = "_blank";
        title.rel = "noopener";
      }
      card.appendChild(title);

      if (senator.class) {
        const classLine = document.createElement("span");
        classLine.textContent = senator.class;
        card.appendChild(classLine);
      }

      appendContactLine(card, senator.phone, senator.email);
      if (senator.contact_url && !senator.email) {
        appendContactLink(card, "Contact form", senator.contact_url);
      }

      return card;
    }

    function appendStateLegislatorPopupDetails(popup, properties, prefix, fallbackLabel) {
      const name = properties[`${prefix}_member_name`] || "";
      const leadershipRole = properties[`${prefix}_member_leadership_role`] || "";
      const photoUrl = properties[`${prefix}_member_photo_url`] || "";

      if (photoUrl) {
        const image = document.createElement("img");
        popup.classList.add("maps-district-popup--with-photo");
        image.src = photoUrl;
        image.alt = name || fallbackLabel;
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      appendContactLine(popup, properties[`${prefix}_member_phone`], properties[`${prefix}_member_email`]);

      [
        leadershipRole
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
    }

    function appendCityCouncilMemberPopupDetails(popup, properties) {
      if (properties.council_member_photo_url) {
        const image = document.createElement("img");
        popup.classList.add("maps-district-popup--with-photo");
        image.src = properties.council_member_photo_url;
        image.alt = properties.council_member_name || "City Council member";
        image.loading = "lazy";
        popup.insertBefore(image, popup.firstChild);
      }

      appendContactLine(popup, properties.council_member_phone, properties.council_member_email);

      [
        properties.council_member_leadership_role
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
    }

    function createCouncilDistrictPopup(feature) {
      const properties = feature.properties || {};
      const district = properties.CC || properties.DISTRICT_N || properties.DISTRICT || "";
      const member = properties.council_member_name || properties.MEMBER_NAM || "";
      const popup = document.createElement("div");
      popup.className = "maps-district-popup";

      const memberUrl = getCityCouncilMemberUrl(properties);
      const title = memberUrl ? document.createElement("a") : document.createElement("strong");
      title.className = "maps-popup-title";
      title.textContent = district ? `City Council District ${district}` : "City Council District";
      if (memberUrl) {
        title.href = memberUrl;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      if (member) {
        const memberLine = document.createElement("span");
        memberLine.textContent = formatNameWithParty(member, properties.council_member_party);
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
      layer.bindPopup(() => createCouncilDistrictPopup(feature), { maxWidth: 10000 });
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
      layer.bindPopup(() => createBoundaryPopup(feature, layerType), { maxWidth: 10000 });
      layer.on("click", function () {
        if (layerType === "votingPrecinct") {
          showVotingPrecinctPollingPointer(feature);
        }
        if (mapInteractionMode === "focus") {
          focusBoundaryFeature(feature, layer, mode, layerType);
        }
        if (compareModeEnabled) {
          pinBoundaryFeature(feature, layerType);
        }
      });
      layer.on("popupclose", function () {
        if (layerType === "votingPrecinct") {
          clearVotingPrecinctPollingPointer(getVotingPrecinctNumber(feature));
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

    function getTrainTrackStyle() {
      return {
        color: "#525252",
        opacity: 0.9,
        weight: 2.25
      };
    }

    function getInterstateStyle() {
      return {
        color: "#1d4ed8",
        opacity: 0.9,
        weight: 4
      };
    }

    function getTrainStationStyle(fillColor) {
      return {
        color: "#ffffff",
        fillColor: fillColor || "#00263A",
        fillOpacity: 0.95,
        opacity: 1,
        radius: 5,
        weight: 1.5
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

    function getSkywayStationStyle() {
      return {
        color: "#ffffff",
        fillColor: "#dc2626",
        fillOpacity: 0.95,
        opacity: 1,
        radius: 5,
        weight: 1.5
      };
    }

    function getFerryLandingStyle() {
      return {
        color: "#ffffff",
        fillColor: "#0369a1",
        fillOpacity: 0.95,
        opacity: 1,
        radius: 5,
        weight: 1.5
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

    function getPollingLocationStyle() {
      return {
        color: "#ffffff",
        fillColor: "#7c3aed",
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

    function getRailRouteTitle(feature) {
      const properties = feature.properties || {};
      const name = [properties.route_short_name, properties.route_long_name].filter(Boolean).join(" - ");
      return name || properties.name || `${properties.agency || "Rail"} Route`;
    }

    function getTrainTrackTitle(feature) {
      const properties = feature.properties || {};
      return properties.name || "Train Tracks";
    }

    function getInterstateTitle(feature) {
      const properties = feature.properties || {};
      return properties.name || (properties.route_number ? `I-${properties.route_number}` : "Interstate");
    }

    function getTrainStationTitle(feature) {
      const properties = feature.properties || {};
      return properties.name || "Train Station";
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

    function createTrainTrackPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = getTrainTrackTitle(feature);
      popup.appendChild(title);

      [
        properties.operator ? `Operator/owner: ${properties.operator}` : "",
        properties.subdivision ? `Subdivision: ${properties.subdivision}` : "",
        properties.trackage_rights ? `Trackage rights: ${properties.trackage_rights}` : "",
        properties.county ? `County: ${properties.county}` : "",
        properties.tracks ? `Tracks: ${properties.tracks}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      return popup;
    }

    function createInterstatePopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = getInterstateTitle(feature);
      popup.appendChild(title);

      [
        properties.county ? `County: ${properties.county}` : "",
        properties.fdot_district ? `FDOT district: ${properties.fdot_district}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      return popup;
    }

    function createRailRoutePopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement(properties.route_url ? "a" : "strong");

      popup.className = "maps-district-popup";
      title.className = "maps-popup-title";
      title.textContent = getRailRouteTitle(feature);
      if (properties.route_url) {
        title.href = properties.route_url;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      [
        properties.agency,
        properties.route_id ? `Route ${properties.route_id}` : "",
        properties.source ? `Source: ${properties.source}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

      return popup;
    }

    function createTrainStationPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement(properties.station_url ? "a" : "strong");

      popup.className = "maps-district-popup maps-train-station-card";
      title.className = "maps-popup-title";
      title.textContent = getTrainStationTitle(feature);
      if (properties.station_url) {
        title.href = properties.station_url;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      [
        properties.operator,
        properties.station_type,
        ...(Array.isArray(properties.address_lines) ? properties.address_lines : [])
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
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

    function createTransitStopPopup(feature, fallbackTitle) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");

      popup.className = "maps-district-popup";
      title.textContent = properties.stop_name || fallbackTitle;
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
      title.className = "maps-popup-title";
      title.textContent = properties.name || "JSO Substation";
      popup.appendChild(title);

      [
        properties.neighborhoods,
        properties.commander ? `District Commander ${properties.commander}` : "",
        properties.address,
        properties.located && properties.located_label ? `${properties.located_label}: ${properties.located}` : properties.located,
        properties.hours ? `Hours: ${properties.hours}` : ""
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });

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

    function createPollingLocationPopup(feature) {
      const properties = feature.properties || {};
      const popup = document.createElement("div");
      const title = document.createElement("strong");
      popup.className = "maps-district-popup";
      title.textContent = properties.name || "Polling Location";
      popup.appendChild(title);
      [
        properties.precinct ? `Precinct ${properties.precinct}` : "",
        properties.address
      ].filter(Boolean).forEach((value) => {
        const line = document.createElement("span");
        line.textContent = value;
        popup.appendChild(line);
      });
      if (properties.source_url) {
        const sourceLink = document.createElement("a");
        sourceLink.href = "https://www.duvalelections.gov/204/Polling-Location-Finder";
        sourceLink.target = "_blank";
        sourceLink.rel = "noopener";
        sourceLink.textContent = "Verify polling location";
        popup.appendChild(sourceLink);
      }
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

    function addTransitRouteInteractivity(feature, layer, layerType) {
      const name = getBusRouteTitle(feature);
      layer.bindPopup(createBusRoutePopup(feature));
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, layerType);
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType });
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

    function addRailRouteInteractivity(feature, layer, layerType) {
      const name = getRailRouteTitle(feature);
      layer.bindPopup(createRailRoutePopup(feature));
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, layerType);
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType });
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

    function addInterstateInteractivity(feature, layer) {
      const name = getInterstateTitle(feature);
      layer.bindPopup(createInterstatePopup(feature));
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
        });
        layer.on({
          mouseover: function () {
            layer.setStyle({
              opacity: 1,
              weight: 6
            });
          },
          mouseout: function () {
            layer.setStyle(getInterstateStyle());
          }
        });
      }
    }

    function addTrainTrackInteractivity(feature, layer) {
      const name = getTrainTrackTitle(feature);
      layer.bindPopup(createTrainTrackPopup(feature));
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
        });
      }
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "trainTrack");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "trainTrack" });
      });
      if (supportsPointerHover) {
        layer.on({
          mouseover: function () {
            layer.setStyle({
              opacity: 1,
              weight: 4
            });
          },
          mouseout: function () {
            layer.setStyle(getTrainTrackStyle());
          }
        });
      }
    }

    function addTrainStationInteractivity(feature, layer) {
      const name = getTrainStationTitle(feature);
      layer.bindPopup(createTrainStationPopup(feature));
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, "trainStation");
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "trainStation" });
      });
      if (name && supportsPointerHover) {
        layer.bindTooltip(name, {
          sticky: true
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

    function addTransitStopInteractivity(feature, layer, layerType) {
      const properties = feature.properties || {};
      const fallbackTitle = layerType === "ferryLanding" ? "Ferry Landing" : "JTA Skyway Station";
      layer.bindPopup(createTransitStopPopup(feature, fallbackTitle));
      layer.on("click", function () {
        if (compareModeEnabled) {
          pinComparableFeature(feature, layerType);
        }
      });
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType });
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

    function addPollingLocationInteractivity(feature, layer) {
      const properties = feature.properties || {};
      layer.bindPopup(createPollingLocationPopup(feature));
      layer.on("contextmenu", function (event) {
        showMapContextMenu(event, { feature, layer, layerType: "pollingLocation" });
      });
      if (supportsPointerHover) {
        layer.bindTooltip(properties.name || "Polling Location", { sticky: true });
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
      const title = properties.USER_URL ? document.createElement("a") : document.createElement("strong");
      const gradeLevel = properties.USER_School_Grade_Level || properties.USER_Grade_Level || "";
      const address = properties.USER_School_Address || properties.IN_SingleLine || properties.Match_addr || "";

      popup.className = "maps-district-popup";
      title.className = "maps-popup-title";
      title.textContent = getSchoolName(feature);
      if (properties.USER_URL) {
        title.href = properties.USER_URL;
        title.target = "_blank";
        title.rel = "noopener";
      }
      popup.appendChild(title);

      appendSchoolPopupLine(popup, gradeLevel);
      appendSchoolPopupLine(popup, address);

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
      title.className = "maps-popup-title";
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
      appendFldoePopupLine(popup, "Contact", properties.contact);
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

      if (!initialVisibleLayerFitComplete && visiblePlaces.length > 1) {
        initialVisibleLayerFitComplete = true;
        map.fitBounds(bounds, { padding: [24, 24] });
      } else if (!initialVisibleLayerFitComplete && visiblePlaces.length === 1) {
        initialVisibleLayerFitComplete = true;
        map.setView([visiblePlaces[0].lat, visiblePlaces[0].lng], visiblePlaces[0].zoom || 14);
      }
      updateZoomHomeDefaultBounds();
    }

    function loadCouncilDistricts() {
      beginMapDataLoad();
      Promise.all([
        fetchJsonData("/data/city-council-districts.geojson", "council districts"),
        fetchJsonData("/data/jacksonville-city-council-members.json", "Jacksonville City Council members")
      ])
        .then(([districts, members]) => {
          joinFeatureMetadata(districts, members, {
            featureKey: (properties) => properties.CC || properties.DISTRICT_N || properties.DISTRICT,
            metadataKey: (member) => member.type === "district" ? member.number : "",
            mapProperties: getCityCouncilMemberProperties
          });
          councilDistrictFillLayer.addData(districts);
          councilDistrictBorderLayer.addData(districts);
          orderMapLayers();
          updateZoomHomeDefaultBounds();
          if (!initialVisibleLayerFitComplete && !places.length && councilDistrictFillLayer.getLayers().length) {
            initialVisibleLayerFitComplete = true;
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

    function fetchJsonData(url, label) {
      if (!jsonDataPromises.has(url)) {
        jsonDataPromises.set(url, fetch(url)
          .then((response) => {
            if (!response.ok) {
              throw new Error(`Could not load ${label}: ${response.status}`);
            }
            return response.json();
          }));
      }
      return jsonDataPromises.get(url)
        .then((response) => {
          return response;
        });
    }

    function getNormalizedMetadataKey(value) {
      return String(value === undefined || value === null ? "" : value).trim().toLowerCase();
    }

    function joinFeatureMetadata(geojson, metadataRecords, options) {
      const settings = options || {};
      if (!geojson || !Array.isArray(geojson.features) || !Array.isArray(metadataRecords)) return geojson;

      const metadataByKey = new Map();
      metadataRecords.forEach((record) => {
        const key = getNormalizedMetadataKey(settings.metadataKey ? settings.metadataKey(record) : record.district);
        if (key) {
          metadataByKey.set(key, record);
        }
      });

      geojson.features.forEach((feature) => {
        const properties = feature.properties || {};
        const key = getNormalizedMetadataKey(settings.featureKey ? settings.featureKey(properties, feature) : properties.district);
        const metadata = metadataByKey.get(key);
        if (!metadata) return;
        feature.properties = Object.assign(properties, settings.mapProperties ? settings.mapProperties(metadata) : metadata);
      });
      return geojson;
    }

    function getCityCouncilMemberProperties(member) {
      return {
        council_member_id: member.id || "",
        council_member_name: member.name || "",
        council_member_role: member.role || "",
        council_member_leadership_role: member.leadership_role || "",
        council_member_phone: member.phone || "",
        council_member_email: member.email || "",
        council_member_assistant: member.assistant || "",
        council_member_party: member.party || "",
        council_member_photo_url: member.photo_url || "",
        council_member_source_url: member.source_url || ""
      };
    }

    function getSchoolBoardMemberProperties(member) {
      return {
        member_name: member.name || "",
        member_role: member.role || "",
        member_email: member.email || "",
        member_phone: member.phone || "",
        member_image_url: member.image_url || "",
        member_source_url: member.source_url || ""
      };
    }

    function getStateLegislatorProperties(member, prefix) {
      return {
        [`${prefix}_member_id`]: member.id || "",
        [`${prefix}_member_name`]: member.name || "",
        [`${prefix}_member_chamber`]: member.chamber || "",
        [`${prefix}_member_district`]: member.district || "",
        [`${prefix}_member_party`]: member.party || "",
        [`${prefix}_member_leadership_role`]: member.leadership_role || "",
        [`${prefix}_member_counties`]: member.counties || "",
        [`${prefix}_member_email`]: member.email || "",
        [`${prefix}_member_phone`]: member.phone || "",
        [`${prefix}_member_capitol_phone`]: member.capitol_phone || "",
        [`${prefix}_member_district_office`]: member.district_office || "",
        [`${prefix}_member_photo_url`]: member.photo_url || "",
        [`${prefix}_member_source_url`]: member.source_url || "",
        [`${prefix}_member_contact_url`]: member.contact_url || "",
        [`${prefix}_member_city_of_residence`]: member.city_of_residence || "",
        [`${prefix}_member_service`]: member.service || ""
      };
    }

    function loadBoundaryLayers(url, fillLayer, borderLayer, label, options) {
      const settings = options || {};
      beginMapDataLoad();
      const requests = [fetchJsonData(url, label)];
      if (settings.metadataUrl) {
        requests.push(fetchJsonData(settings.metadataUrl, settings.metadataLabel || `${label} metadata`));
      }

      Promise.all(requests)
        .then(([geojson, metadataRecords]) => {
          if (metadataRecords) {
            joinFeatureMetadata(geojson, metadataRecords, settings);
          }
          fillLayer.addData(geojson);
          borderLayer.addData(geojson);
          if (settings.onLoad) settings.onLoad(geojson);
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

    function addClippedInterstatesToLayer(geojson, countyFeatures, targetLayer) {
      (geojson.features || []).forEach((feature) => {
        countyFeatures.forEach((countyFeature) => {
          const clippedGeometry = clipLineGeometryToFeature(feature.geometry, countyFeature);
          if (!clippedGeometry) return;
          targetLayer.addData({
            ...feature,
            geometry: clippedGeometry
          });
        });
      });
    }

    function loadInterstateLayers(url) {
      const northeastFloridaCountyNames = new Set([
        "Baker County",
        "Clay County",
        "Duval County",
        "Flagler County",
        "Nassau County",
        "Putnam County",
        "St. Johns County"
      ]);
      beginMapDataLoad();
      Promise.all([
        fetchJsonData(url, "Florida interstates"),
        fetchJsonData("/data/counties.geojson", "county boundaries")
      ])
        .then(([geojson, countyGeojson]) => {
          (geojson.features || []).forEach((feature) => {
            const routeNumber = String((feature.properties || {}).route_number || "");
            const interstateLayer = interstateLayersByRouteNumber.get(routeNumber);
            if (interstateLayer) {
              interstateLayer.addData(feature);
            }
          });
          const countyFeatures = countyGeojson.features || [];
          const duvalCountyFeatures = countyFeatures.filter((feature) => (
            (feature.properties || {}).county_name === "Duval County"
          ));
          const northeastFloridaCountyFeatures = countyFeatures.filter((feature) => (
            northeastFloridaCountyNames.has((feature.properties || {}).county_name)
          ));
          addClippedInterstatesToLayer(geojson, duvalCountyFeatures, duvalInterstatesLayer);
          addClippedInterstatesToLayer(geojson, northeastFloridaCountyFeatures, northeastFloridaInterstatesLayer);
          orderMapLayers();
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
      "city council at-large districts",
      {
        metadataUrl: "/data/jacksonville-city-council-members.json",
        metadataLabel: "Jacksonville City Council members",
        featureKey: (properties) => properties.CCAL,
        metadataKey: (member) => member.type === "at_large" ? member.number : "",
        mapProperties: getCityCouncilMemberProperties
      }
    );
    loadBoundaryLayers(
      "/data/duval-county-school-board-districts.geojson",
      schoolBoardDistrictFillLayer,
      schoolBoardDistrictBorderLayer,
      "Duval County School Board districts",
      {
        metadataUrl: "/data/duval-school-board-members.json",
        metadataLabel: "Duval County School Board members",
        featureKey: (properties) => properties.school_board_district,
        metadataKey: (member) => member.district,
        mapProperties: getSchoolBoardMemberProperties
      }
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
      "county boundaries",
      { onLoad: setRegionalElevationMask }
    );
    loadBoundaryLayers(
      "/data/duval-voting-precincts.geojson",
      votingPrecinctFillLayer,
      votingPrecinctBorderLayer,
      "Duval County voting precincts"
    );
    loadGeoJsonLayer("/data/duval-polling-locations.geojson", pollingLocationsLayer, "Duval County polling locations");
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
      "Florida House districts",
      {
        metadataUrl: "/data/florida-house-members.json",
        metadataLabel: "Florida House members",
        featureKey: (properties) => properties.HSE,
        metadataKey: (member) => member.district,
        mapProperties: (member) => getStateLegislatorProperties(member, "state_house")
      }
    );
    loadBoundaryLayers(
      "/data/florida-senate-districts.geojson",
      floridaSenateFillLayer,
      floridaSenateBorderLayer,
      "Florida Senate districts",
      {
        metadataUrl: "/data/florida-senate-members.json",
        metadataLabel: "Florida Senate members",
        featureKey: (properties) => properties.SEN,
        metadataKey: (member) => member.district,
        mapProperties: (member) => getStateLegislatorProperties(member, "state_senate")
      }
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
      "/data/florida-us-senators.geojson",
      usSenateFillLayer,
      usSenateBorderLayer,
      "Florida U.S. Senators"
    );
    loadBoundaryLayers(
      "/data/duval-health-zones.geojson",
      healthZoneFillLayer,
      healthZoneBorderLayer,
      "Duval County health zones"
    );
    loadGeoJsonLayer("/data/duval-health-zones-by-zipcodes.geojson", healthZoneByZipCodeLayer, "Duval County health zones by listed ZIP codes");
    loadBoundaryLayers(
      "/data/duval-flood-zones.geojson",
      floodZoneFillLayer,
      floodZoneBorderLayer,
      "Duval County flood zones"
    );
    loadBoundaryLayers(
      "/data/duval-evacuation-zones.geojson",
      evacuationZoneFillLayer,
      evacuationZoneBorderLayer,
      "Duval County evacuation zones"
    );
    loadInterstateLayers("/data/florida-interstates.geojson");
    loadGeoJsonLayer("/data/train-tracks.geojson", trainTracksLayer, "train tracks");
    loadGeoJsonLayer("/data/jta-bus-routes.geojson", busRoutesLayer, "JTA bus routes");
    loadGeoJsonLayer("/data/jta-bus-stops.geojson", busStopsLayer, "JTA bus stops");
    loadGeoJsonLayer("/data/jta-skyway-routes.geojson", skywayRoutesLayer, "JTA Skyway routes");
    loadGeoJsonLayer("/data/jta-skyway-stations.geojson", skywayStationsLayer, "JTA Skyway stations");
    loadGeoJsonLayer("/data/st-johns-river-ferry.geojson", ferryRouteLayer, "St. Johns River Ferry");
    loadGeoJsonLayer("/data/st-johns-river-ferry-landings.geojson", ferryLandingsLayer, "St. Johns River Ferry landings");
    loadGeoJsonLayer("/data/amtrak-routes.geojson", amtrakRoutesLayer, "Amtrak routes");
    loadGeoJsonLayer("/data/amtrak-stations.geojson", trainStationsLayer, "Amtrak stations");
    loadGeoJsonLayer("/data/brightline-routes.geojson", brightlineRoutesLayer, "Brightline routes");
    loadGeoJsonLayer("/data/brightline-stations.geojson", brightlineStationsLayer, "Brightline stations");
    loadGeoJsonLayer("/data/sunrail-routes.geojson", sunrailRoutesLayer, "SunRail routes");
    loadGeoJsonLayer("/data/sunrail-stations.geojson", sunrailStationsLayer, "SunRail stations");
    loadGeoJsonLayer("/data/tri-rail-routes.geojson", triRailRoutesLayer, "Tri-Rail routes");
    loadGeoJsonLayer("/data/tri-rail-stations.geojson", triRailStationsLayer, "Tri-Rail stations");
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
    addLeadershipJaxLocationsControl();
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
    addElevationClickHandler();
    addElevationLegend();
    addCompareKeyboardShortcut();
    addMapContextMenuHandlers();
    addModifierDragRotation();
    registerMapQueryLayers();
    activateOpacityQuery();
    activateHistoricMapOpacityQuery();
    activateQueryLayers();
    addBaseMapControl();
    addLocateControl();
    activateLocateQuery();
    map.rotateControl.setPosition("topleft");

    function addTopLeftMenuToggle() {
      const TopLeftMenuToggleControl = L.Control.extend({
        options: {
          position: "topleft"
        },
        onAdd: function () {
          const container = L.DomUtil.create("div", "leaflet-bar leaflet-control maps-top-left-menu-toggle");
          const button = L.DomUtil.create("button", "", container);

          button.type = "button";
          button.textContent = "☰";
          button.title = "Open map controls";
          button.setAttribute("aria-label", "Open map controls");
          button.setAttribute("aria-expanded", "false");

          function setOpen(open) {
            const corner = container.parentElement;
            if (!corner) return;
            corner.classList.toggle("is-open", open);
            button.textContent = open ? "×" : "☰";
            button.title = open ? "Close map controls" : "Open map controls";
            button.setAttribute("aria-label", open ? "Close map controls" : "Open map controls");
            button.setAttribute("aria-expanded", String(open));
          }

          button.addEventListener("click", function () {
            setOpen(!container.parentElement.classList.contains("is-open"));
          });
          map.on("click", function () {
            setOpen(false);
          });
          document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") setOpen(false);
          });
          L.DomEvent.disableClickPropagation(container);
          L.DomEvent.disableScrollPropagation(container);
          return container;
        }
      });

      const toggleControl = new TopLeftMenuToggleControl();
      map.addControl(toggleControl);
      const corner = toggleControl.getContainer().parentElement;
      corner.classList.add("maps-top-left-menu");
      corner.insertBefore(toggleControl.getContainer(), corner.firstChild);

      const layersControl = corner.querySelector(".maps-layers-control");
      const baseMapControl = corner.querySelector(".maps-basemap-control");
      if (layersControl && baseMapControl) {
        corner.insertBefore(baseMapControl, layersControl.nextSibling);
      }

      const attributionToggle = corner.querySelector(".maps-attribution-toggle");
      if (attributionToggle) {
        corner.appendChild(attributionToggle);
      }

    }

    addTopLeftMenuToggle();
    
    setBaseMap(getBaseMapQueryKey(), { quiet: true, updateUrl: false });

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
