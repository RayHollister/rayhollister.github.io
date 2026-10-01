---
layout: page
title: Maps References
permalink: /maps/references/
exclude: true
---

This page lists the source references used for the layers on the [Maps](/maps/) page.

## Disclaimer

This map is provided as is, with no guarantee of accuracy, completeness, or currentness. It is a personal passion project and should not be considered canonical information.

The information shown on the map is based on the sources listed below, using data available as of October 1, 2026. For official decisions, current boundaries, service eligibility, representation, routing, or public records, consult the original source material and the responsible agency directly.

If you appreciate this project, you can [buy me a coffee! ☕️](https://buymeacoffee.com/rayhollister).

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
  - City Council District Overlays
  - City Council District Borders
  - City Council District At Large Overlays
  - City Council District At Large Borders
  - School Board Districts Overlays
  - School Board Districts Borders
  - Cities Overlays
  - Cities Borders
- [Duval County Public Schools School Board](https://www.duvalschools.org/page/school-board/)
  - Current School Board member names, roles, email addresses, phone numbers, and photos for School Board District popups.
  - Citizens Planning Advisory Committee (CPACs) Overlays
  - Citizens Planning Advisory Committee (CPACs) Borders
- County boundaries:
  - Geometry source: [U.S. Census Bureau TIGERweb State/County boundary service](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1)
  - County records: Baker, Clay, Duval, Nassau, and St. Johns counties, Florida.
  - Counties Overlays
  - Counties Borders
- [119th Congressional Districts](https://www.arcgis.com/home/item.html?id=56f9d1c5628349c684245185a020d18a&sublayer=0)
  - Congressional Districts Overlays
  - Congressional Districts Borders
- Congressional District reference links:
  - [Florida's 4th Congressional District](https://ballotpedia.org/Florida%27s_4th_Congressional_District)
  - [Florida's 5th Congressional District](https://ballotpedia.org/Florida%27s_5th_Congressional_District)
- [City of Jacksonville City Council Members](https://www.jacksonville.gov/city-council/city-council-members)
  - Current District Council Member and At Large Council Member names, roles, email addresses, phone numbers, assistants, photos, and profile links for City Council District and City Council District At Large popups.
- [Florida House of Representatives](https://www.flhouse.gov/representatives)
  - Current representative names, parties, district-office phone numbers, office addresses, photos, contact links, and profile links for Florida House popups.
- [Florida Senate](https://www.flsenate.gov/Senators)
  - Current senator names, parties, email addresses, phone numbers, district-office addresses, photos, and profile links for Florida Senate popups.
- ZIP Code / ZCTA boundaries:
  - Geometry source: [U.S. Census Bureau TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
  - ZIP Code Tabulation Area geometry: 2024 TIGER/Line `ZCTA520`.
  - Duval County clip boundary: 2024 TIGER/Line County, Duval County, Florida (`STATEFP=12`, `COUNTYFP=031`).
  - Note: USPS is authoritative for ZIP Codes as mail-routing data, but USPS does not publish official ZIP Code polygon boundaries. The map uses Census ZIP Code Tabulation Areas (ZCTAs), which are public statistical approximations of USPS ZIP Code service areas, clipped to Duval County.
  - Zip Codes Overlays
  - Zip Codes Borders
- Neighborhood Overlays and Neighborhood Borders:
  - Source repository: [RayHollister/JacksonvilleNeighborhoods](https://github.com/RayHollister/JacksonvilleNeighborhoods)
  - Runtime data URL: [neighborhoods.geojson](https://raw.githubusercontent.com/RayHollister/JacksonvilleNeighborhoods/main/neighborhoods.geojson)
  - Note: Although this map was created by the City of Jacksonville, this is not an official neighborhood boundaries map. Many of these neighborhoods do not have "official" boundaries, as they have not been defined legally. Also, there are several typos in this file that have not all been fixed.
- [City of Jacksonville Neighborhood Organizations Directory](https://jaxnhorg.coj.net/#/orglist)
  - Neighborhood Organizations
  - Organization addresses normalized locally; Neighborhood organization point coordinates geocoded from the public organization addresses.
- [ArcGIS World Geocoding Service](https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer)
  - Used to geocode public Neighborhood organization addresses.
- [City of Jacksonville Citizen Planning Advisory Committees](https://www.jacksonville.gov/departments/neighborhoods/neighborhood-services-office/citizen-planning-advisory-committees-(cpacs))
  - CPAC district names and reference links

## Jacksonville Sheriff's Office

- [Jacksonville Sheriff's Office District and Subsector Lookup](https://experience.arcgis.com/experience/1a554e29e87c43869389dc46841e12f0)
  - Districts
  - Subsections
- [Jacksonville Sheriff's Office Your Neighborhood](https://www.jaxsheriff.org/Your-Neighborhood.aspx)
  - Substations

## Health

- Health Zones:
  - Source framework: Florida Department of Health in Duval County health-zone framework; ZIP breakdown from Health Planning Council of Northeast Florida Housing HIA report citing DOH-Duval community health planning materials.
  - Duval County is divided into six multi-ZIP-code health zones for regional health data tracking and community planning by the Florida Department of Health in Duval County.
  - The [Health Planning Council of Northeast Florida Housing Health Impact Assessment](https://hpcnef.org/wp-content/uploads/2016/02/Housing-HIA-Report_Final-6-7-17.pdf) lists the six health-zone ZIP-code groupings and cites the Florida Department of Health in Duval County Community Health Assessment and Community Health Improvement Plan as the source for the health-zone map.
  - The same report also identifies Florida Department of Health in Duval County as the data source for several health-zone indicators.
  - Health Zone 1 (Urban Core): 32202, 32204, 32206, 32208, 32209, 32254.
  - Health Zone 2 (Arlington / Greater Urban): 32207, 32211, 32216, 32224, 32225, 32246, 32277.
  - Health Zone 3 (Southside / Mandarin): 32217, 32223, 32256, 32257, 32258, 32259, 32081.
  - Health Zone 4 (Westside): 32205, 32210, 32212, 32214, 32215, 32221, 32222, 32244.
  - Health Zone 5 (Northside / Outer Rim): 32218, 32219, 32220, 32226, 32234.
  - Health Zone 6 (Beaches): 32227, 32228, 32233, 32250, 32266.
  - Current working assumption pending confirmation from Florida Department of Health in Duval County: health zones clip at the Duval County line, and 32259 and 32081 belong with Health Zone 3.
  - Geometry is built from the map's Census-based ZIP/ZCTA layer: [U.S. Census Bureau TIGER/Line 2024 ZCTA520](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html), clipped to the U.S. Census Bureau TIGER/Line 2024 Duval County boundary. 32215 is listed in the health-zone ZIP breakdown, but no polygon geometry is available in the Census-clipped ZIP/ZCTA layer.
  - ZCTAs are Census statistical approximations of USPS ZIP Code service areas; USPS does not publish official ZIP Code polygon boundaries.
  - Query-only alternate layer: `?layer=healthzones-byzipcodes` uses the listed Health Zone ZIP-code groups without adding 32081 or 32259 to Health Zone 3, and uses full Census ZCTA geometry, including the full 32234 ZCTA.

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
