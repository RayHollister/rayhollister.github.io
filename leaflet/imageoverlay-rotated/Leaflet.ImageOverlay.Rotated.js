/*
 * Leaflet.ImageOverlay.Rotated
 * Copyright Iván Sánchez Ortega
 * Beer-Ware License: https://github.com/ivansanchez/Leaflet.ImageOverlay.Rotated
 */
L.RayRotatedImageOverlay = L.ImageOverlay.extend({
  initialize: function (image, topLeft, topRight, bottomLeft, options) {
    if (typeof image === "string") {
      this._url = image;
    } else {
      this._rawImage = image;
    }
    this._topLeft = L.latLng(topLeft);
    this._topRight = L.latLng(topRight);
    this._bottomLeft = L.latLng(bottomLeft);
    L.setOptions(this, options);
  },

  onAdd: function (map) {
    if (!this._image) {
      this._initImage();
      if (this.options.opacity < 1) this._updateOpacity();
    }
    map.on("zoomend resetview", this._reset, this);
    this.getPane().appendChild(this._image);
    this._reset();
  },

  onRemove: function (map) {
    map.off("zoomend resetview", this._reset, this);
    L.ImageOverlay.prototype.onRemove.call(this, map);
  },

  _initImage: function () {
    let image = this._rawImage;
    if (this._url) {
      image = L.DomUtil.create("img");
      image.style.display = "none";
      if (this.options.crossOrigin) image.crossOrigin = "";
      this._rawImage = image;
    }
    L.DomUtil.addClass(image, "leaflet-image-layer");
    const container = this._image = L.DomUtil.create(
      "div",
      `leaflet-image-layer ${this._zoomAnimated ? "leaflet-zoom-animated" : ""}`
    );
    this._updateZIndex();
    container.appendChild(image);
    container.onselectstart = L.Util.falseFn;
    container.onmousemove = L.Util.falseFn;
    image.onload = () => {
      this._reset();
      image.style.display = "block";
      this.fire("load");
    };
    image.alt = this.options.alt || "";
    if (this._url) image.src = this._url;
  },

  _reset: function () {
    if (!this._map) return;
    const topLeft = this._map.latLngToLayerPoint(this._topLeft);
    const topRight = this._map.latLngToLayerPoint(this._topRight);
    const bottomLeft = this._map.latLngToLayerPoint(this._bottomLeft);
    const bottomRight = topRight.subtract(topLeft).add(bottomLeft);
    const pixelBounds = L.bounds([topLeft, topRight, bottomLeft, bottomRight]);
    const size = pixelBounds.getSize();
    const topLeftInContainer = topLeft.subtract(pixelBounds.min);
    this._bounds = L.latLngBounds(
      this._map.layerPointToLatLng(pixelBounds.min),
      this._map.layerPointToLatLng(pixelBounds.max)
    );
    L.DomUtil.setPosition(this._image, pixelBounds.min);
    this._image.style.width = `${size.x}px`;
    this._image.style.height = `${size.y}px`;
    const imageWidth = this._rawImage.width;
    const imageHeight = this._rawImage.height;
    if (!imageWidth || !imageHeight) return;
    const horizontal = topRight.subtract(topLeft);
    const vertical = bottomLeft.subtract(topLeft);
    this._rawImage.style.transformOrigin = "0 0";
    this._rawImage.style.transform = `matrix(${horizontal.x / imageWidth}, ${horizontal.y / imageWidth}, ${vertical.x / imageHeight}, ${vertical.y / imageHeight}, ${topLeftInContainer.x}, ${topLeftInContainer.y})`;
  },

  reposition: function (topLeft, topRight, bottomLeft) {
    this._topLeft = L.latLng(topLeft);
    this._topRight = L.latLng(topRight);
    this._bottomLeft = L.latLng(bottomLeft);
    this._reset();
    return this;
  }
});

L.rayRotatedImageOverlay = function (image, topLeft, topRight, bottomLeft, options) {
  return new L.RayRotatedImageOverlay(image, topLeft, topRight, bottomLeft, options);
};
