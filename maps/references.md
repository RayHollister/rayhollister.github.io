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
- Neighborhood Overlays and Neighborhood Borders:
  - Source repository: [RayHollister/JacksonvilleNeighborhoods](https://github.com/RayHollister/JacksonvilleNeighborhoods)
  - Runtime data URL: [neighborhoods.geojson](https://raw.githubusercontent.com/RayHollister/JacksonvilleNeighborhoods/main/neighborhoods.geojson)
  - Note: Although this map was created by the City of Jacksonville, this is not an official neighborhood boundaries map. Many of these neighborhoods do not have "official" boundaries, as they have not been defined legally. Also, there are several typos in this file that have not all been fixed.

## Transportation

- [JTA GTFS Archive](https://ride.jtafla.com/gtfs-archive/)
  - JTA Bus Routes
  - JTA Bus Stops

## Duval County Public Schools Lookup Map

- [Duval County Public Schools lookup map](https://jacobs.maps.arcgis.com/apps/instant/lookup/index.html?appid=d9d3f3b133fb4c30b00886006f4aa0ed#find=30.306646122101068%2C-81.65127371701966)
  - Elementary Schools
  - Middle Schools
  - High Schools
  - Dedicated Magnet Schools
  - Used for DCPS school websites on matching Florida Department of Education school points.

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

## School Data Comparison Notes

The Florida Department of Education Traditional Public layers and the Duval County Public Schools lookup map were compared by school number. DCPS school numbers were matched to the first three digits of the FLDOE school number, so DCPS `#16` matches FLDOE `0161`.

Summary:

- DCPS lookup map unique schools: 134
- FLDOE Traditional Public unique schools: 146
- FLDOE Traditional Public records not present in the DCPS lookup map: 15
- DCPS lookup map records not present in FLDOE Traditional Public: 3
- Category/taxonomy differences among matched schools: 53
- Coordinate differences greater than 100 meters among matched schools: 43

FLDOE Traditional Public records not present in the DCPS lookup map:

- `#14` Grand Park Career Center
- `#17` The Bridge To Success Academy Middle School
- `#25` Springfield Middle School
- `#27` Grasp Academy At Don Brewer
- `#28` Oak Hill Academy
- `#29` The Bridge To Success Academy At W Jacksonville
- `#32` Marine Science Education Center
- `#49` Duval Regional Juvenile Detention Center
- `#81` Pace Center For Girls-jax
- `#156` Jacksonville Stem Academy At Eugene Butler
- `#170` Palm Avenue Excep. Student Center
- `#176` Pretrial Detention Facility
- `#181` Hospital And Homebound
- `#252` Alden Road Excep. Student Center
- `#702` Duval Virtual Instruction Academy

DCPS lookup map records not present in FLDOE Traditional Public:

- `#94` Windy Hill Elementary School
- `#214` Hyde Grove Elementary School
- `#228` Merrill Road Elementary School

Category/taxonomy differences:

- Many differences are because FLDOE treats magnet as a status that can be attached to Elementary, Middle, High, or Combination schools, while the DCPS lookup map includes a separate Dedicated Magnet layer.
- DCPS lists `#38` Baldwin Middle-High School in Middle and High; FLDOE lists it as Combination plus Magnet.
- DCPS lists `#154` John E. Ford Pre K-8 School in Dedicated Magnet and Elementary; FLDOE lists John E. Ford K-8 School as Combination plus Magnet.
- DCPS lists `#251` Twin Lakes Academy Elementary School in Dedicated Magnet and Elementary; FLDOE lists it as Elementary only.
- DCPS lists `#274` Westview K - 8 Elementary School in Elementary, Middle, and High; FLDOE lists Westview K-8 as Combination.

Largest coordinate differences between matched schools:

- `#68` Venetia Elementary School: about 7,034 meters
- `#64` Hogan-Spring Glen Elementary School: about 4,803 meters
- `#144` Jacksonville Beach Elementary School: about 1,247 meters
- `#78` Biltmore Elementary School: about 763 meters
- `#142` Chaffee Trail Elementary School: about 477 meters
- `#260` Mandarin High School: about 476 meters
- `#124` Northwestern Legends Elementary School: about 400 meters
- `#280` Frank H. Peterson Academies of Technology: about 396 meters
- `#207` Westside Middle School: about 326 meters
- `#96` Jean Ribault High School: about 309 meters
