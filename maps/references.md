---
layout: page
title: Maps References
permalink: /maps/references/
exclude: true
---

This page lists the source references used for the layers on the [Maps](/maps/) page.

## Disclaimer

This map is provided as is, with no guarantee of accuracy, completeness, or currentness. It is a personal passion project and should not be considered canonical information.

The information shown on the map is based on the sources listed below, using data available as of October 8, 2026. For official decisions, current boundaries, service eligibility, representation, routing, or public records, consult the original source material and the responsible agency directly.

If you appreciate this project, you can [buy me a coffee! ☕️](https://buymeacoffee.com/rayhollister).

## Basemaps

- Positron: [OpenFreeMap Positron](https://tiles.openfreemap.org/styles/positron)
- Bright: [OpenFreeMap Bright](https://tiles.openfreemap.org/styles/bright)
- 3D: [OpenFreeMap Liberty](https://tiles.openfreemap.org/styles/liberty)
- OpenFreeMap project documentation: [OpenFreeMap quick start](https://openfreemap.org/quick_start/) and [hyperknot/openfreemap](https://github.com/hyperknot/openfreemap)
- Google Satellite: [Google satellite tile endpoint](https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z})

## Boundaries And Area Layers

- [City of Jacksonville My Neighborhood](https://maps.coj.net/myneighborhood/)
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
  - Population, square mileage, and people per square mile in county popups: [Census Reporter API](https://api.censusreporter.org/1.0/geo/latest/05000US12031), using land area for square mileage and density.
  - County records: Alachua, Baker, Bradford, Clay, Duval, Flagler, Nassau, Putnam, and St. Johns counties, Florida; and Camden and Charlton counties, Georgia.
  - Counties Overlays
  - Counties Borders
- [119th Congressional Districts](https://www.arcgis.com/home/item.html?id=56f9d1c5628349c684245185a020d18a&sublayer=0)
  - U.S. House Overlays
  - U.S. House Borders
- U.S. House reference links:
  - [Florida's 4th Congressional District](https://www.house.gov/htbin/findrep?ZIP=32202)
  - [Florida's 5th Congressional District](https://www.house.gov/htbin/findrep?ZIP=32207)
  - Congressional district popup phone numbers and contact-form links are sourced from the official member websites linked from the House lookup pages.
- U.S. Senators:
  - Senator names, party abbreviations, classes, phone numbers, websites, and contact-form links: [United States Senate contact information XML](https://www.senate.gov/general/contact_information/senators_cfm.xml)
  - Senator photos: [United States Senate Florida senators page](https://www.senate.gov/states/FL/intro.htm)
  - Florida state polygon geometry: [U.S. Census Bureau TIGERweb State boundary service](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/0)
- [City of Jacksonville City Council Members](https://www.jacksonville.gov/city-council/city-council-members)
  - Current District Council Member and At Large Council Member names, roles, email addresses, phone numbers, assistants, photos, and profile links for City Council District and City Council District At Large popups.
  - City Council party affiliations: [Jacksonville City Council party affiliation table](https://en.wikipedia.org/wiki/Jacksonville_City_Council#Party_affiliation)
- [Florida House of Representatives](https://www.flhouse.gov/representatives)
  - Current representative names, parties, email addresses, district-office phone numbers, office addresses, photos, contact links, and profile links for Florida House popups.
- Florida House Districts 2022, enacted February 3, 2022 as plan H000H8013:
  - Geometry source: [Florida Legislature Office of Economic & Demographic Research 2020 Redistricting shapefile](https://edr.state.fl.us/Content/redistricting/2020redistricting/H000H8013.zip)
  - Reference page: [Florida Legislature Office of Economic & Demographic Research 2020 Redistricting](https://edr.state.fl.us/Content/redistricting/2020redistricting/index.cfm)
  - Florida House Overlays
  - Florida House Borders
- [Florida Senate](https://www.flsenate.gov/Senators)
  - Current senator names, parties, email addresses, phone numbers, district-office addresses, photos, and profile links for Florida Senate popups.
- Florida Senate Districts 2022, enacted February 3, 2022 as plan S027S8058:
  - Geometry source: [Florida Legislature Office of Economic & Demographic Research 2020 Redistricting shapefile](https://edr.state.fl.us/Content/redistricting/2020redistricting/S027S8058.zip)
  - Reference page: [Florida Legislature Office of Economic & Demographic Research 2020 Redistricting](https://edr.state.fl.us/Content/redistricting/2020redistricting/index.cfm)
  - Senate plan reference: [Florida Senate Maps & Statistics - State Senate Plans](https://www.flsenate.gov/Session/Redistricting/MapsAndStats)
  - Florida Senate Overlays
  - Florida Senate Borders
- ZIP Code / ZCTA boundaries:
  - Geometry source: [U.S. Census Bureau TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
  - Population, square mileage, and people per square mile in ZIP Code popups: [Census Reporter API](https://api.censusreporter.org/1.0/geo/latest/86000US32208), using ZCTA land area for square mileage and density.
  - ZIP Code Tabulation Area geometry: 2024 TIGER/Line `ZCTA520`.
  - Duval County clip boundary: 2024 TIGER/Line County, Duval County, Florida (`STATEFP=12`, `COUNTYFP=031`).
  - Note: USPS is authoritative for ZIP Codes as mail-routing data, but USPS does not publish official ZIP Code polygon boundaries. The map uses Census ZIP Code Tabulation Areas (ZCTAs), which are public statistical approximations of USPS ZIP Code service areas, clipped to Duval County.
  - Zip Codes Overlays
  - Zip Codes Borders
- Census & Demographics:
  - Census tract and block-group geometry: [U.S. Census Bureau TIGERweb ACS 2024 service](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_ACS2024/MapServer), Census Tracts layer 8 and Census Block Groups layer 10, filtered to Duval County, Florida (`STATE=12`, `COUNTY=031`).
  - Demographic estimates: [Census Reporter API](https://api.censusreporter.org/1.0/data/show/latest) using ACS 2024 5-year estimates (`acs2024_5yr`, 2020-2024).
  - Generated assets: `/data/census-tracts.geojson`, `/data/census-block-groups.geojson`, and `/data/census-demographic-metrics.json`.
  - Regeneration script: `script/generate-census-demographics`.
  - Validation script: `script/validate-census-demographics`.
  - Initial supported measurements include total population, population density, median age, age 65 and older, median household income, poverty rate, unemployment rate, total housing units, homeownership rate, renter-occupied household rate, vacancy rate, median home value, median gross rent, bachelor's degree or higher rate, public transportation commute rate, long commute rate, households without vehicles, broadband subscription rate, no Internet subscription rate, no Internet access rate, and computer ownership rate.
  - ACS values are estimates and may have substantial margins of error at small geographies. Direct-estimate margins of error are retained where published; derived-rate margins of error are not calculated in this first implementation, so rate popups identify those as derived values rather than exact counts.
  - Census Tracts Overlays
  - Census Tracts Borders
  - Census Block Groups Overlays
  - Census Block Groups Borders
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

## Transportation

- Train Tracks:
  - Geometry source: [U.S. Census Bureau TIGERweb Transportation service, Railroads layer](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Transportation/MapServer/9), queried as GeoJSON for the current map county extent.
  - Train Tracks
- [JTA GTFS Archive](https://ride.jtafla.com/gtfs-archive/)
  - JTA Bus Routes
  - JTA Bus Stops
  - Route counts shown in polygon cards are calculated from GTFS stop-to-route data, not from route line geometry. A route is counted for a polygon when at least one bus stop served by that route is inside the polygon or within 100 meters of the polygon boundary. Routes are deduplicated by GTFS `route_id`, so multiple route shapes or trips for the same route count once.

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

## Health

- Health Zones:
  - There is no official map and no official ZIP-code list defining the Duval County Health Zones. Florida Department of Health in Duval County confirmed this directly in October 2026.
  - The Health Zone map was developed in 2008. Based on the geographic boundaries, Florida Department of Health in Duval County said it would be reasonable to consider Duval County residents within ZIP codes 32259 and 32081 as part of Health Zone 3, but those areas may not have been represented within Duval County at that time and their inclusion cannot be definitively confirmed.
  - Because there is no official definition and 32259 and 32081 cannot be confirmed, this map shows them in black as an excluded group rather than assigning them to Health Zone 3.
  - Source framework: Florida Department of Health in Duval County health-zone framework; ZIP breakdown from Health Planning Council of Northeast Florida Housing HIA report citing DOH-Duval community health planning materials.
  - The [Health Planning Council of Northeast Florida Housing Health Impact Assessment](https://hpcnef.org/wp-content/uploads/2016/02/Housing-HIA-Report_Final-6-7-17.pdf) lists six health-zone ZIP-code groupings and cites the Florida Department of Health in Duval County Community Health Assessment and Community Health Improvement Plan as the source for the health-zone map.
  - Health Zone 1 (Urban Core): 32202, 32204, 32206, 32208, 32209, 32254.
  - Health Zone 2 (Arlington / Greater Urban): 32207, 32211, 32216, 32224, 32225, 32246, 32277.
  - Health Zone 3 (Southside / Mandarin): 32217, 32223, 32256, 32257, 32258.
  - Excluded / unconfirmed ZIPs shown in black: 32259, 32081.
  - Health Zone 4 (Westside): 32205, 32210, 32212, 32214, 32215, 32221, 32222, 32244.
  - Health Zone 5 (Northside / Outer Rim): 32218, 32219, 32220, 32226, 32234.
  - Health Zone 6 (Beaches): 32227, 32228, 32233, 32250, 32266.
  - Geometry is built from the map's Census-based ZIP/ZCTA layer: [U.S. Census Bureau TIGER/Line 2024 ZCTA520](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html), clipped to the U.S. Census Bureau TIGER/Line 2024 Duval County boundary. 32215 is listed in the health-zone ZIP breakdown, but no polygon geometry is available in the Census-clipped ZIP/ZCTA layer.
  - ZCTAs are Census statistical approximations of USPS ZIP Code service areas; USPS does not publish official ZIP Code polygon boundaries.
  - Query-only alternate layer: `?layer=healthzones-byzipcodes` uses the listed Health Zone ZIP-code groups and full Census ZCTA geometry, including the full 32234 ZCTA.
