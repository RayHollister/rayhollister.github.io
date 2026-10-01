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

- [City of Jacksonville My Neighborhood](https://maps.coj.net/myneighborhood/)
  - Florida House Overlays
  - Florida House Borders
  - Florida Senate Overlays
  - Florida Senate Borders
  - Zip Codes Overlays
  - Zip Codes Borders
  - City Council District Overlays
  - City Council District Borders
  - City Council District At Large Overlays
  - City Council District At Large Borders
  - Cities Overlays
  - Cities Borders
- [119th Congressional Districts](https://www.arcgis.com/home/item.html?id=56f9d1c5628349c684245185a020d18a&sublayer=0)
  - Congressional Districts Overlays
  - Congressional Districts Borders
- Congressional District reference links:
  - [Florida's 4th Congressional District](https://ballotpedia.org/Florida%27s_4th_Congressional_District)
  - [Florida's 5th Congressional District](https://ballotpedia.org/Florida%27s_5th_Congressional_District)
- City Council member page links: [City of Jacksonville City Council Members](https://www.jacksonville.gov/city-council/city-council-members)
- Neighborhood Overlays and Neighborhood Borders:
  - Source repository: [RayHollister/JacksonvilleNeighborhoods](https://github.com/RayHollister/JacksonvilleNeighborhoods)
  - Runtime data URL: [neighborhoods.geojson](https://raw.githubusercontent.com/RayHollister/JacksonvilleNeighborhoods/main/neighborhoods.geojson)
  - Note: Although this map was created by the City of Jacksonville, this is not an official neighborhood boundaries map. Many of these neighborhoods do not have "official" boundaries, as they have not been defined legally. Also, there are several typos in this file that have not all been fixed.

## Jacksonville Sheriff's Office

- [Jacksonville Sheriff's Office District and Subsector Lookup](https://experience.arcgis.com/experience/1a554e29e87c43869389dc46841e12f0)
  - Districts
  - Subsections
- [Jacksonville Sheriff's Office Your Neighborhood](https://www.jaxsheriff.org/Your-Neighborhood.aspx)
  - Substations

## Transportation

- [JTA GTFS Archive](https://ride.jtafla.com/gtfs-archive/)
  - JTA Bus Routes
  - JTA Bus Stops

## Educational Institutions

- [Florida Department of Education Know Your Schools Mapping](https://edudata.fldoe.org/ReportCards/Mapping.html)
  - Traditional Public Elementary
  - Traditional Public Middle
  - Traditional Public High
  - Traditional Public Combination
  - Traditional Public Magnet
  - Charter Public Elementary
  - Charter Public Middle
  - Charter Public High
  - Charter Public Combination
- [Florida Department of Education Private School Directory spreadsheet](https://www.floridaschoolchoice.org/information/privateschooldirectory/DownloadExcelFile.aspx)
  - Private Schools Elementary
  - Private Schools Middle
  - Private Schools High
  - Private Schools Combination
  - Treated as authoritative for private school names, addresses, contacts, participation fields, grade levels, and survey data.
- [University of Florida GeoPlan Center FGDL GEOPLAN_Points](https://sagittarius.at.geoplan.ufl.edu/arcgis/rest/services/fgdl/GEOPLAN_Points/MapServer)
  - [Schools - Private (Points)](https://sagittarius.at.geoplan.ufl.edu/arcgis/rest/services/fgdl/GEOPLAN_Points/MapServer/15), used for coordinates where records match the Florida Department of Education private school spreadsheet.
  - [Schools - Public and Post-Secondary (Points)](https://sagittarius.at.geoplan.ufl.edu/arcgis/rest/services/fgdl/GEOPLAN_Points/MapServer/14), used for Post-Secondary Schools.

## Duval County Public Schools Lookup Map

- [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Elementary Schools
  - Middle Schools
  - High Schools
  - Dedicated Magnet Schools
  - Used for DCPS school websites on matching Florida Department of Education school points.
