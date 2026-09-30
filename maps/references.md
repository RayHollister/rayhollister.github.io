---
layout: page
title: Maps References
permalink: /maps/references/
exclude: true
---

This page lists the source references used for the layers on the [Maps](/maps/) page.

## Basemaps

- Positron: [OpenFreeMap Positron](https://tiles.openfreemap.org/styles/positron)
- Bright: [OpenFreeMap Bright](https://tiles.openfreemap.org/styles/bright)
- 3D: [OpenFreeMap Liberty](https://tiles.openfreemap.org/styles/liberty)
- OpenFreeMap project documentation: [OpenFreeMap quick start](https://openfreemap.org/quick_start/) and [hyperknot/openfreemap](https://github.com/hyperknot/openfreemap)
- Google Satellite: [Google satellite tile endpoint](https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z})

## Boundaries And Area Layers

- City Council District Overlays and City Council District Borders:
  - Source page: [City of Jacksonville Council District Search](https://maps.coj.net/councildistrictsearch/)
  - Site data: `/data/city-council-districts.geojson`
  - Confirmed against local file geodatabase: `/Volumes/TerraNVMe1-2TB/Downloads/councildistrict.gdb`
- City Council District At Large Overlays and City Council District At Large Borders:
  - Source file geodatabase: `/Volumes/TerraNVMe1-2TB/Downloads/councildistrictatlarge.gdb`
  - Site data: `/data/city-council-at-large-districts.geojson`
- Cities Overlays and Cities Borders:
  - Source file geodatabase: `/Volumes/TerraNVMe1-2TB/Downloads/cityboundaries.gdb`
  - Site data: `/data/city-boundaries.geojson`
- Neighborhood Overlays and Neighborhood Borders:
  - Source repository: [RayHollister/JacksonvilleNeighborhoods](https://github.com/RayHollister/JacksonvilleNeighborhoods)
  - Runtime data URL: [neighborhoods.geojson](https://raw.githubusercontent.com/RayHollister/JacksonvilleNeighborhoods/main/neighborhoods.geojson)

## Transportation

- JTA Bus Routes:
  - Source GTFS folder: `/Volumes/TerraNVMe1-2TB/Downloads/june15gtfsv2`
  - Site data: `/data/jta-bus-routes.geojson`
- JTA Bus Stops:
  - Source GTFS folder: `/Volumes/TerraNVMe1-2TB/Downloads/june15gtfsv2`
  - Site data: `/data/jta-bus-stops.geojson`

## Educational Institutions

- Elementary Schools:
  - Source page: [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Site data: `/data/elementary-schools.geojson`
- Middle Schools:
  - Source page: [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Site data: `/data/middle-schools.geojson`
- High Schools:
  - Source page: [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Site data: `/data/high-schools.geojson`
- Dedicated Magnet Schools:
  - Source page: [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Site data: `/data/dedicated-magnet-schools.geojson`
