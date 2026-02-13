---
layout: post
title: "How I Reverse-Engineered a Home Assistant Integration for the Homewerks Smart Bathroom Fan"
date: 2026-02-15T12:49:00-05:00
categories: 
  - Technology
  - AI
  - Home Automation
author: Ray Hollister
image: /media/2026/02/Integrating-My-Homewerks-Smart-Fan-With-Home-Assistant.jpg
image_alt: "A hand holding an iPhone displaying the Home Assistant app's Bathroom room with Light, Fan, Speaker, and temperature/humidity sensor entities, held up in front of the Homewerks 7148-01-AX smart fan mounted in the ceiling"
image_caption: "Now that I've spent all this time automating my bathroom fan, maybe I should spend five minutes dusting it."
reading-time: true
---
I love my Homewerks 7148-01-AX bathroom fan. It's got Alexa built in, Bluetooth speakers, an LED light with adjustable brightness and color temperature, and a surprisingly capable exhaust fan — all controlled from a sleek wall panel. For a bathroom fan, it punches way above its weight.

But it had one glaring problem: it didn't work with Home Assistant.

Every other smart device in my house — lights, locks, sensors, switches — lives happily inside Home Assistant, participating in automations, reporting state, and playing nicely with everything else. The Homewerks fan? It sat there on its own little island, reachable only through the Homewerks app or Alexa voice commands. Want to automatically turn on the fan when humidity spikes? Tough luck. Want to dim the light as part of a bedtime routine? Not happening.

So I did what any reasonable person would do. I contacted the manufacturer and asked for help. That went about as well as you'd expect.

## The Customer Service Experience

In January 2023, I submitted a request through the Homewerks website asking if they had any plans to add Home Assistant integration, or if they'd be willing to let me look at the source code so I could build one myself. Simple enough, right?

The first response asked if I was referring to "the Alexa home assistant." I clarified that no, I meant Home Assistant — the open-source home automation platform with almost 2,000 integrations and millions of users. I even included a link.

The next reply informed me that "this product is a Homewerks product that has Alexa technology built in. It is not an Alexa product first. So unfortunately, it cannot be connected to Home Assistant." They seemed to think I was asking how to pair it, not requesting a feature or offering to build one.

I tried once more, explaining that I was aware it couldn't currently connect to Home Assistant — that was the whole point of my request. I pointed out that creating a Home Assistant integration would increase the product's value to millions of potential customers who have passed on it specifically because it doesn't integrate with their setup.

The final response: "The Alexa fan model # 7148-01-AX was engineered to work with Alexa technology, exclusively, as a standalone product. Unfortunately, it cannot connect to the Apple Home assistant."

Apple Home assistant.

They thought I was asking about Apple HomeKit.

Three different customer service representatives across four emails, and not one of them understood what I was asking for. To be fair, Home Assistant isn't a household name outside of the smart home enthusiast community. But the unwillingness to even consider the request — or pass it along to someone technical — was frustrating.

So I decided to build it myself.

## Finding the Way In

The 7148-01-AX doesn't expose a documented API. There's no developer portal, no SDK, no MQTT broker to connect to. From the outside, it's a black box that talks to Alexa's cloud services and the Homewerks mobile app.

But it's still a device on my local network, and devices on local networks can be observed.

This is where Claude came in. I'd been using Claude for various development projects, and the idea of pointing an AI at raw network traffic to help reverse-engineer a proprietary protocol sounded like exactly the kind of problem it could accelerate.

The first step was reconnaissance. We scanned the device's open ports and found it listening on TCP port 8899 — a port commonly associated with Linkplay, a Chinese IoT module manufacturer that provides the WiFi and audio chipset for a huge number of smart speakers and IoT devices. We also found UPnP services on ports 49152 and 59152, which confirmed the Linkplay connection. The device's UPnP description identified itself as manufacturer "Linkplay" with model "MUZO Cobblestone."

Knowing it was Linkplay-based gave us a starting point. Linkplay devices use a custom binary protocol over TCP for UART passthrough — essentially a way for network commands to talk directly to the device's microcontroller. The frame format uses a specific four-byte header (`0x18 0x96 0x18 0x20`), followed by a little-endian payload length, twelve bytes of padding, and then a payload string in the format `MCU+PAS+{json}&`.

With Claude's help, I wrote Python scripts to connect to port 8899 and start probing. We tried dozens of different JSON command structures — `{"STA": "query"}`, `{"status": "get"}`, `{"get": "all"}` — watching for any response. Most commands disappeared into the void.

Then we discovered something crucial: sending a property key with an empty string value causes the device to report that property's current state. Send `{"fan_power": ""}` and you get back `{"fan_power": "OFF"}`. Send `{"light_power": ""}` and you get `{"light_power": "ON"}`. Send `{"percentage": ""}` and you get `{"percentage": 255}` — which told us the device uses a 0-255 brightness range internally rather than the 0-100 that Home Assistant expects.

From there, it was a matter of mapping out the full command vocabulary. We discovered commands for turning the fan on and off, controlling the light, setting brightness, and even interacting with the built-in speaker as a media player. Each discovery built on the last, and Claude helped me iterate through possibilities in minutes that would have taken me hours of manual trial and error.

## Building the Integration

With the protocol mapped out, the actual Home Assistant integration came together relatively quickly. The architecture is straightforward:

A persistent TCP connection to port 8899 listens for state changes pushed by the device (when someone uses the wall panel or Alexa voice commands), while also providing the ability to send commands back. The integration exposes three entity types in Home Assistant: a fan entity for the exhaust fan, a light entity with brightness control, and a media player entity for the Bluetooth speaker.

The tricky parts were the ones you don't think about until they bite you. The device only allows one TCP connection at a time, so the integration has to be careful about connection management. State updates from the device sometimes arrive as multiple JSON frames concatenated in a single TCP read, so the parser has to handle splitting those apart. And if the connection drops — which happens, because IoT devices on WiFi are flaky — the integration needs to reconnect automatically with exponential backoff rather than dying silently and requiring a full Home Assistant restart.

That last problem — silent connection death — was one we didn't catch until the integration had been running for a while. The fan would work fine for days, then suddenly stop responding to commands and stop reflecting state changes. Restarting Home Assistant fixed it every time, which is the classic symptom of a lost network connection with no reconnection logic.

The fix involved adding connection health monitoring (a keepalive check if no data arrives for three minutes), automatic reconnection with backoff from one second up to sixty seconds, entity availability tracking so Home Assistant shows the fan as unavailable rather than just frozen in its last known state, and an initial state query on every connect and reconnect so entities start with accurate values instead of defaulting to off.

## What Would Have Taken Weeks Took Hours

I want to be honest about Claude's role in this project, because I think it illustrates something important about where AI assistance is genuinely transformative versus where it's just convenient.

The protocol reverse-engineering phase — scanning ports, probing command structures, interpreting binary frame formats, iterating through possible JSON payloads — is the kind of work that traditionally takes a dedicated reverse engineer dozens to hundreds of hours. You're staring at hex dumps, cross-referencing with known protocols, writing and rewriting test scripts, and doing a lot of educated guessing. It's fascinating work if you have the time, but I have a full-time job and a nonprofit to run.

With Claude, that phase took a few short hours instead of weeks. I could describe what I was seeing on the wire, and Claude would suggest what it might mean based on its knowledge of Linkplay protocols, IoT communication patterns, and binary frame formats. When a probe came back with an unexpected response, we could immediately adjust our approach. When we hit a dead end, we could pivot to a completely different strategy without the cognitive overhead of context-switching.

The integration code itself was also dramatically faster to write. Claude understands Home Assistant's integration architecture — config flows, entity platforms, the coordinator pattern, async patterns — and could generate working scaffolding that I then refined and tested against the actual device. The back-and-forth of "try this, it didn't work, here's what happened" was natural and productive.

But the key insight is this: Claude didn't replace me. It accelerated me. I still had to make every architectural decision, test every change against the real hardware, debug the weird edge cases that only show up after days of runtime, and maintain the project going forward. The AI made the tedious parts fast and the hard parts approachable, but it couldn't have done any of this without someone who understood the goal and could evaluate whether the results were actually correct.

## The Result

The [Homewerks Smart Fan Integration](https://github.com/RayHollister/homewerks-smart-fan-integration/) is available on GitHub as a HACS custom component. It provides local control of the 7148-01-AX's fan, LED light, and speaker — no cloud services required, no Alexa dependency for basic operations.

My bathroom fan now participates in humidity-based automations. The light dims as part of my evening routine. The speaker shows up as a media player in Home Assistant's media controls. And it all works reliably, reconnecting automatically when the WiFi hiccups, reporting accurate state even when controlled from the wall panel.

It's the integration Homewerks wouldn't build, built by the customer they wouldn't listen to, reverse-engineered from the protocol they wouldn't document, and developed in hours instead of months thanks to an AI that actually understood the question I was asking.

## What's Next

The integration works. But "works" and "done" are two very different things.

The day after publishing the initial release, I started using it in earnest — and the cracks appeared almost immediately. The fan entity would show the correct state for a day or two, then quietly stop updating. Home Assistant would still show the fan as "off" while it was roaring away above me in a steam-filled bathroom. The TCP connection to the device had silently died, and without reconnection logic, the integration was deaf to any state changes until I restarted Home Assistant entirely. That became [Issue #3](https://github.com/RayHollister/homewerks-smart-fan-integration/issues/3).

Fixing it meant going back to the protocol and making a discovery we'd missed the first time around: the device doesn't respond to status query commands in any documented format. No `{"status": "get"}`, no `{"STA": "query"}`. Nothing. But Claude and I found that sending a property key with an empty string value — `{"fan_power": ""}` — causes the device to report that property's current state. It was an undocumented quirk hiding in plain sight. We also discovered that the device sends multiple JSON frames concatenated in a single TCP read, which our parser had been silently dropping. And that the device reports brightness on a 0-255 scale while Home Assistant expects 0-100, so half the brightness values were wrong. The fix added automatic reconnection with exponential backoff, periodic polling as a safety net, connection health monitoring, and proper state queries on every connect. Version 1.2.1 turned a fragile proof of concept into something I could actually trust.

Then came [Issue #1](https://github.com/RayHollister/homewerks-smart-fan-integration/issues/1) — the one that bit us during our own debugging session. Claude and I were trying to probe the device for protocol details, connecting Python scripts to port 8899, and getting nothing back. The device wasn't even responding to pings. Turns out the fan had gotten a new IP address from my router, and the integration was still trying to talk to the old one. *Issue #1 demonstrated itself while we were trying to fix Issue #3.* The irony wasn't lost on me. We probed the device's UPnP description and found it carries a unique device identifier — a UUID that stays constant even when the IP changes. The plan is to use that UUID to scan the local network when the connection fails, so even if the IP changes, the integration can find the fan again on its own. No more deleting and re-adding the integration every time your router decides to shuffle addresses.

And then there was [Issue #2](https://github.com/RayHollister/homewerks-smart-fan-integration/issues/2) — a user asked if the microphone mute could be toggled through the integration. Unfortunately, the wall panel connects to the fan unit through standard romex wiring with no data bus, and the mute signal never surfaces on the TCP protocol. That one was a dead end, but fun to investigate as I sat in the bathroom pressing the mute button like a detective desperately buzzing a suspect's apartment, while Claude staked out the packet capture waiting for a signal that never came.
All of these fixes and features probably took less combined time than it took to write this article, thanks to Claude. 

People complain about AI a lot lately, and I get it. There are legitimate concerns about the energy consumption and water usage required to run these massive data centers. And when the most visible use case is your social media feed full of "Create a caricature of me and my job based on everything you know about me" posts, it's easy to look at that and wonder if all that energy and water is worth it. But AI can also be used to build powerful tools that provide long-lasting value — tools that add real functionality to hardware you've already paid for, that solve problems the manufacturer won't solve, and that turn a closed ecosystem into an open one. A generated selfie disappears from your feed in a day. A working Home Assistant integration makes your home smarter for years.

If you have a Homewerks 7148-01-AX and run Home Assistant, check out the [GitHub repo](https://github.com/RayHollister/homewerks-smart-fan-integration/). And if you work at Homewerks and you're reading this — it's Home Assistant. Not Apple Home assistant. Not the Alexa home assistant. [Home Assistant](https://www.home-assistant.io/). You should check it out. Your customers are asking for it.