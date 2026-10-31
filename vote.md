---
layout: page
title: Jacksonville Voting Precinct & Polling Place Finder
permalink: /vote/
description: "Find your Jacksonville and Duval County voting precinct, assigned polling place, City Council district, School Board district, and elected representatives using your current location."
image: /media/2026/10/jacksonville-voting-finder-social.png
exclude: true
---

<style>
  :root {
    --mobile-photo: 100px;
  }
  .vote-intro {
    max-width: 46rem;
    margin: 1rem 0;
    padding: 1.25rem;
    border: 1px solid rgba(127, 127, 127, 0.3);
    border-radius: 10px;
    background: rgba(127, 127, 127, 0.06);
  }
  .vote-intro > p:first-child {
    margin-top: 0;
    font-size: 1.1rem;
    font-weight: 600;
  }
  .vote-intro > p:last-of-type {
    margin-bottom: 0;
  }
  .vote-actions {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.75rem;
    max-width: 46rem;
    margin: 0 0 1rem;
    padding: 1rem;
    border: 1px solid rgba(9, 105, 218, 0.3);
    border-radius: 10px;
    background: rgba(9, 105, 218, 0.06);
  }
  .vote-locate {
    min-height: 44px;
    border: 1px solid #0969da;
    border-radius: 5px;
    background: #0969da;
    color: #fff;
    cursor: pointer;
    font: inherit;
    font-weight: 700;
    padding: 0.7rem 1rem;
  }
  .vote-locate:hover,
  .vote-locate:focus-visible {
    background: #0557b7;
  }
  .vote-locate:disabled {
    cursor: wait;
    opacity: 0.65;
  }
  .vote-status {
    flex: 1 1 16rem;
    margin: 0;
    padding: 0.65rem 0.8rem 0.65rem 2rem;
    border-radius: 5px;
    background: rgba(127, 127, 127, 0.1);
    color: #4b5563;
    font-size: 0.92rem;
    font-weight: 600;
    line-height: 1.4;
    position: relative;
  }
  .vote-status::before {
    width: 0.55rem;
    height: 0.55rem;
    border-radius: 50%;
    background: #0969da;
    content: "";
    left: 0.75rem;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
  }
  .vote-status[role="alert"] {
    color: #b42318;
    background: rgba(180, 35, 24, 0.08);
  }
  .vote-status[role="alert"]::before {
    background: #b42318;
  }
  .vote-results {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 46rem;
  }
  .vote-results > * {
    margin-block: 0;
  }
  .post-content .vote-results h2 {
    margin-top: 0;
  }
  .vote-card {
    min-width: 0;
    border: 1px solid rgba(127, 127, 127, 0.35);
    border-radius: 10px;
    background: rgba(127, 127, 127, 0.06);
    padding: 0.85rem 1rem;
    line-height: 1.3;
  }
  .vote-card--primary {
    border-color: #7c3aed;
    box-shadow: inset 0 0 0 1px #7c3aed;
  }
  .vote-card h2 {
    margin: 0 0 0.5rem;
    font-size: 1.12rem;
    line-height: 1.2;
  }
  .vote-card h3 {
    margin: 0.65rem 0 0.2rem;
    font-size: 1rem;
    line-height: 1.2;
  }
  .vote-person {
    align-items: start;
    column-gap: 1rem;
    display: grid;
    grid-template-columns: 115px minmax(0, 1fr);
    line-height: 1.25;
  }
  .vote-person + .vote-person {
    border-top: 1px solid rgba(127, 127, 127, 0.25);
    margin-top: 0.55rem;
    padding-top: 0.55rem;
  }
  .vote-person img {
    border-radius: 5px;
    grid-column: 1;
    grid-row: 1 / span 20;
    width: 115px;
    height: 115px;
    margin: 0;
    object-fit: cover;
  }
  .vote-person > :not(img) {
    grid-column: 2;
    min-width: 0;
  }
  .vote-person strong,
  .vote-card span,
  .vote-card address,
  .vote-card a {
    display: block;
  }
  .vote-person strong {
    line-height: 1.2;
  }
  .vote-card address {
    margin: 0;
    font-style: normal;
  }
  .vote-card a {
    overflow-wrap: anywhere;
    padding-block: 0.08rem;
  }
  .vote-note {
    font-size: 0.92rem;
  }
  .vote-section-heading {
    margin-block: 0;
  }
  @media screen and (max-width: 599px) {
    .post-header {
      margin-bottom: 1rem;
    }
    .post-title {
      font-size: clamp(1.75rem, 8vw, 2.25rem);
      line-height: 1.12;
    }
    .vote-intro {
      margin-inline: -0.35rem;
      padding: 1rem;
    }
    .vote-intro p {
      margin-bottom: 0.85rem;
      line-height: 1.5;
    }
    .vote-actions {
      align-items: stretch;
      display: grid;
      gap: 0.65rem;
      margin: 0 -0.35rem 1rem;
      padding: 1rem;
    }
    .vote-locate {
      width: 100%;
      min-height: 50px;
      padding: 0.8rem 1rem;
    }
    .vote-status {
      padding-block: 0.7rem;
    }
    .vote-card {
      padding: 0.8rem;
    }
    .vote-card--primary {
      border-width: 2px;
      box-shadow: none;
    }
    .vote-card h2 {
      font-size: 1.15rem;
      line-height: 1.2;
    }
    .vote-person {
      grid-template-columns: var(--mobile-photo) minmax(0, 1fr);
      column-gap: 0.7rem;
      font-size: 0.9rem;
    }
    .vote-person img {
      width: var(--mobile-photo);
      height: var(--mobile-photo);
    }
    .vote-card a {
      min-height: 24px;
    }
    .vote-note {
      padding-inline: 0.2rem;
      line-height: 1.45;
    }
    .vote-section-heading {
      font-size: 1.45rem;
      line-height: 1.25;
    }
  }
</style>

<div class="vote-actions">
  <button class="vote-locate" id="vote-locate" type="button">Find my voting information</button>
  <p class="vote-status" id="vote-status" aria-live="polite">Click the button to find your voting precinct, polling location and your current elected representatives.</p>
</div>

<section class="vote-results" id="vote-results" aria-label="Voting and representation information"></section>

<div class="vote-intro">
  <p>Find your Jacksonville voting precinct, assigned Duval County polling place, and elected representatives using your current location.</p>
  <p>The results include your Jacksonville City Council district, at-large council members, Duval County School Board district, Florida House and Senate districts, U.S. House district, and Florida’s U.S. senators.</p>
  <p>Your coordinates stay in your browser and are only compared with the local Jacksonville and Duval County boundary data used by <a href="https://jaxmaps.org/">JaxMaps</a>.</p>
</div>

<template id="vote-note-template">
  <p class="vote-note">Boundary and polling-place information can change. Always confirm your assignment with the <a href="https://www.duvalelections.gov/204/Polling-Location-Finder" target="_blank" rel="noopener">Duval County Supervisor of Elections polling-location finder</a>. See <a href="https://jaxmaps.org/references/">JaxMaps References</a> for sources and limitations.</p>
</template>

<script>
  (function () {
    "use strict";

    const locateButton = document.getElementById("vote-locate");
    const status = document.getElementById("vote-status");
    const results = document.getElementById("vote-results");
    const noteTemplate = document.getElementById("vote-note-template");
    const pollingFinderUrl = "https://www.duvalelections.gov/204/Polling-Location-Finder";
    const dataUrls = {
      precincts: "/data/duval-voting-precincts.geojson",
      pollingLocations: "/data/duval-polling-locations.geojson",
      councilDistricts: "/data/city-council-districts.geojson",
      councilMembers: "/data/jacksonville-city-council-members.json",
      schoolBoardDistricts: "/data/duval-county-school-board-districts.geojson",
      schoolBoardMembers: "/data/duval-school-board-members.json",
      floridaHouseDistricts: "/data/florida-house-districts.geojson",
      floridaHouseMembers: "/data/florida-house-members.json",
      floridaSenateDistricts: "/data/florida-senate-districts.geojson",
      floridaSenateMembers: "/data/florida-senate-members.json",
      congressionalDistricts: "/data/congressional-districts.geojson",
      usSenators: "/data/florida-us-senators.geojson"
    };
    let dataPromise;

    function setStatus(message, isError) {
      status.textContent = message;
      if (isError) {
        status.setAttribute("role", "alert");
      } else {
        status.removeAttribute("role");
      }
    }

    function fetchJson(url) {
      return fetch(url).then((response) => {
        if (!response.ok) throw new Error(`Could not load ${url}`);
        return response.json();
      });
    }

    function loadData() {
      if (!dataPromise) {
        dataPromise = Promise.all(Object.entries(dataUrls).map(([key, url]) => (
          fetchJson(url).then((value) => [key, value])
        ))).then((entries) => Object.fromEntries(entries));
      }
      return dataPromise;
    }

    function pointInRing(point, ring) {
      let inside = false;
      for (let index = 0, previous = ring.length - 1; index < ring.length; previous = index, index += 1) {
        const currentPoint = ring[index];
        const previousPoint = ring[previous];
        const intersects = ((currentPoint[1] > point[1]) !== (previousPoint[1] > point[1])) &&
          (point[0] < ((previousPoint[0] - currentPoint[0]) * (point[1] - currentPoint[1]) /
          (previousPoint[1] - currentPoint[1])) + currentPoint[0]);
        if (intersects) inside = !inside;
      }
      return inside;
    }

    function pointInPolygon(point, rings) {
      if (!rings || !rings.length || !pointInRing(point, rings[0])) return false;
      return !rings.slice(1).some((ring) => pointInRing(point, ring));
    }

    function containsPoint(feature, point) {
      const geometry = feature && feature.geometry;
      if (!geometry) return false;
      if (geometry.type === "Polygon") return pointInPolygon(point, geometry.coordinates);
      if (geometry.type === "MultiPolygon") {
        return geometry.coordinates.some((polygon) => pointInPolygon(point, polygon));
      }
      return false;
    }

    function findFeature(geojson, point) {
      return (geojson.features || []).find((feature) => containsPoint(feature, point));
    }

    function appendText(parent, text, tagName) {
      if (!text) return;
      const element = document.createElement(tagName || "span");
      element.textContent = text;
      parent.appendChild(element);
    }

    function appendLink(parent, label, href) {
      if (!href) return;
      const link = document.createElement("a");
      link.href = href;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = label;
      parent.appendChild(link);
    }

    function appendPollingDirections(card, pollingFeature) {
      const coordinates = pollingFeature && pollingFeature.geometry && pollingFeature.geometry.coordinates;
      if (!coordinates || coordinates.length < 2) return;
      const destination = `${coordinates[1]},${coordinates[0]}`;
      const heading = document.createElement("h3");
      heading.textContent = "Get directions";
      card.appendChild(heading);
      appendLink(card, "Google Maps", `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(destination)}`);
      appendLink(card, "Apple Maps", `https://maps.apple.com/?daddr=${encodeURIComponent(destination)}&dirflg=d`);
      appendLink(card, "Waze", `https://www.waze.com/ul?ll=${encodeURIComponent(destination)}&navigate=yes`);
    }

    function partyAbbreviation(party) {
      const normalized = String(party || "").toLowerCase();
      if (normalized === "republican" || normalized === "r") return "R";
      if (normalized === "democrat" || normalized === "democratic" || normalized === "d") return "D";
      return party || "";
    }

    function personName(person) {
      const party = partyAbbreviation(person.party);
      return `${person.name || "Representative"}${party ? ` (${party})` : ""}`;
    }

    function createCard(title, primary) {
      const card = document.createElement("article");
      const heading = document.createElement("h2");
      card.className = `vote-card${primary ? " vote-card--primary" : ""}`;
      heading.textContent = title;
      card.appendChild(heading);
      return card;
    }

    function appendPerson(card, person, titlePrefix) {
      if (!person) return;
      const wrapper = document.createElement("div");
      wrapper.className = "vote-person";
      if (person.photo_url || person.image_url) {
        const image = document.createElement("img");
        image.src = person.photo_url || person.image_url;
        image.alt = `Photo of ${person.name}`;
        image.loading = "lazy";
        wrapper.appendChild(image);
      }
      appendText(wrapper, `${titlePrefix || ""}${personName(person)}`, "strong");
      appendText(wrapper, person.leadership_role || person.role || person.class);
      if (person.phone) appendLink(wrapper, person.phone, `tel:${person.phone.replace(/[^+\d]/g, "")}`);
      if (person.email) appendLink(wrapper, person.email, `mailto:${person.email}`);
      if (person.contact_url && !person.email) appendLink(wrapper, "Contact form", person.contact_url);
      appendLink(wrapper, "Official page", person.source_url || person.website_url);
      card.appendChild(wrapper);
    }

    function findMember(members, key, value, type) {
      return (members || []).find((member) => (
        (!type || member.type === type) && String(member[key]) === String(value)
      ));
    }

    function renderResults(data, longitude, latitude) {
      const point = [longitude, latitude];
      const precinctFeature = findFeature(data.precincts, point);
      const councilFeature = findFeature(data.councilDistricts, point);
      const schoolFeature = findFeature(data.schoolBoardDistricts, point);
      const houseFeature = findFeature(data.floridaHouseDistricts, point);
      const senateFeature = findFeature(data.floridaSenateDistricts, point);
      const congressionalFeature = findFeature(data.congressionalDistricts, point);
      const senatorFeature = findFeature(data.usSenators, point);

      results.replaceChildren();
      if (!precinctFeature && !councilFeature) {
        setStatus("This location is outside the supported Jacksonville/Duval County area.", true);
        return;
      }

      if (precinctFeature) {
        const precinct = String((precinctFeature.properties || {}).GEOID || "").replace(/^12031-/, "");
        const pollingFeature = (data.pollingLocations.features || []).find((feature) => (
          String((feature.properties || {}).precinct || "").split(",").map((value) => value.trim()).includes(precinct)
        ));
        const card = createCard(`Voting Precinct ${precinct}`, true);
        const polling = pollingFeature && pollingFeature.properties || {};
        const pollingHeading = document.createElement("h3");
        pollingHeading.textContent = "Polling location";
        card.appendChild(pollingHeading);
        appendText(card, polling.name || "No current polling location is listed for this precinct.", "strong");
        if (polling.address) {
          const address = document.createElement("address");
          address.textContent = polling.address;
          card.appendChild(address);
        }
        appendLink(card, "Verify polling location", pollingFinderUrl);
        appendPollingDirections(card, pollingFeature);
        results.appendChild(card);
      }

      results.appendChild(noteTemplate.content.cloneNode(true));

      const representativesHeading = document.createElement("h2");
      representativesHeading.className = "vote-section-heading";
      representativesHeading.textContent = "Your elected representatives";
      results.appendChild(representativesHeading);

      if (councilFeature) {
        const district = (councilFeature.properties || {}).CC || (councilFeature.properties || {}).DISTRICT;
        const card = createCard(`City Council District ${district}`);
        appendPerson(card, findMember(data.councilMembers, "number", district, "district"));
        results.appendChild(card);
      }

      const atLargeCard = createCard("City Council At Large");
      (data.councilMembers || []).filter((member) => member.type === "at_large").forEach((member) => {
        appendPerson(atLargeCard, member, `Group ${member.number}: `);
      });
      results.appendChild(atLargeCard);

      if (schoolFeature) {
        const district = (schoolFeature.properties || {}).school_board_district;
        const card = createCard(`Duval County School Board District ${district}`);
        appendPerson(card, findMember(data.schoolBoardMembers, "district", district));
        results.appendChild(card);
      }

      if (houseFeature) {
        const district = (houseFeature.properties || {}).HSE;
        const card = createCard(`Florida House District ${district}`);
        appendPerson(card, findMember(data.floridaHouseMembers, "district", district));
        results.appendChild(card);
      }

      if (senateFeature) {
        const district = (senateFeature.properties || {}).SEN;
        const card = createCard(`Florida Senate District ${district}`);
        appendPerson(card, findMember(data.floridaSenateMembers, "district", district));
        results.appendChild(card);
      }

      if (congressionalFeature) {
        const properties = congressionalFeature.properties || {};
        const district = properties.BASENAME || "";
        const card = createCard(`Florida Congressional District ${district}`);
        appendPerson(card, {
          name: properties.congressional_member_name,
          party: properties.congressional_member_party,
          photo_url: properties.congressional_member_photo_url,
          phone: properties.congressional_member_phone,
          contact_url: properties.congressional_member_contact_url,
          website_url: properties.congressional_member_website_url
        });
        results.appendChild(card);
      }

      if (senatorFeature) {
        const card = createCard("Florida U.S. Senators");
        ((senatorFeature.properties || {}).senators || []).forEach((senator) => appendPerson(card, senator, "Senator "));
        results.appendChild(card);
      }

      setStatus("Voting and representation information found for your location.");
    }

    function locate() {
      if (!navigator.geolocation) {
        setStatus("This browser does not support location services.", true);
        return;
      }
      locateButton.disabled = true;
      locateButton.textContent = "Finding location…";
      setStatus("Requesting your location and loading civic data…");

      Promise.all([
        loadData(),
        new Promise((resolve, reject) => navigator.geolocation.getCurrentPosition(resolve, reject, {
          enableHighAccuracy: true,
          maximumAge: 30000,
          timeout: 20000
        }))
      ]).then(([data, position]) => {
        renderResults(data, position.coords.longitude, position.coords.latitude);
      }).catch((error) => {
        setStatus(error.message || "Could not determine your location.", true);
      }).finally(() => {
        locateButton.disabled = false;
      locateButton.textContent = "Find my voting information";
      });
    }

    locateButton.addEventListener("click", locate);
    const params = new URLSearchParams(window.location.search);
    if (String(params.get("locate") || "").trim().toLowerCase() === "yes") locate();
  })();
</script>
