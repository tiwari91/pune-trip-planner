"""Fetch today's state-wise petrol prices and write fuel.json for the planner.

Source: goodreturns.in petrol price page (state table). Run daily by GitHub Actions.
"""
import datetime
import html
import json
import re
import sys
import urllib.request

URL = "https://www.goodreturns.in/petrol-price.html"
ALIASES = {
	"Chhatisgarh": "Chhattisgarh",
	"Pondicherry": "Puducherry",
	"Jammu & Kashmir": "Jammu and Kashmir",
	"Andaman & Nicobar": "Andaman and Nicobar Islands",
}
METROS = {"New Delhi", "Kolkata", "Mumbai", "Chennai", "Gurgaon", "Noida", "Bangalore", "Bhubaneswar",
	"Chandigarh", "Hyderabad", "Jaipur", "Lucknow", "Patna", "Thiruvananthapuram"}


def main():
	req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (pune-trip-planner fuel updater)"})
	page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
	states, cities = {}, {}
	seen_metro_block = set()
	for row in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
		cells = [html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c))).strip()
			for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
		if len(cells) < 2 or not cells[1].startswith("₹"):
			continue
		name, price = cells[0], float(cells[1].replace("₹", "").replace(",", ""))
		if name in METROS and name not in seen_metro_block:
			seen_metro_block.add(name)
			cities[name] = price
			continue
		states[ALIASES.get(name, name)] = price
	if len(states) < 25:
		sys.exit(f"Only {len(states)} states parsed; page layout may have changed. Not writing fuel.json.")
	data = {
		"updated": datetime.date.today().isoformat(),
		"source": URL,
		"states": dict(sorted(states.items())),
		"cities": cities,
	}
	with open("fuel.json", "w") as f:
		json.dump(data, f, indent=1, ensure_ascii=False)
		f.write("\n")
	print(f"Wrote {len(states)} states, {len(cities)} cities")


if __name__ == "__main__":
	main()
