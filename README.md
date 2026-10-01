# Pune Trip Planner

Road and rail trip plans from Pune for winter 2026 to 2027, with real costs.

Live: https://tiwari91.github.io/pune-trip-planner/

- **Plan any trip:** type any start and destination in India. It finds the road route (Google Maps or OpenStreetMap view), drive time, night stops and full cost, using today's petrol price for the start and end states, and compares it with train and flight.
- **Patna by car:** a three-day route via the Samruddhi expressway, Nagpur and Varanasi, December fog advice, and a drive cost calculator that compares the car with 3AC, 2AC and flights.
- **Tirupati:** a three-day train trip, darshan booking rules and costs.
- **Goa:** a four-day drive based in South Goa, with peak-season warnings.
- **Maharashtra:** four circuits, from Shirdi and Nashik to the Konkan coast into Goa.
- **When to go:** a suggested order for the season.

Prices were checked on 1 October 2026 from public sources listed on the page. Hotel and food lines are estimates. Check before you book.

Static site, no build step: `index.html`, `places.js` (popular places for instant search) and `fuel.json`.

`fuel.json` holds state-wise petrol prices. A GitHub Action (`.github/workflows/fuel.yml`) runs `scripts/update_fuel.py` every morning at 7:00 IST and commits the new prices. Place search uses Photon, routing uses the OSRM demo server, both on OpenStreetMap data.
