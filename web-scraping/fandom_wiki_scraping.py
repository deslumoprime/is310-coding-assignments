import json
import time
from urllib.parse import urljoin

import cloudscraper
from bs4 import BeautifulSoup

BASE_URL = "https://clashofclans.fandom.com"
CATEGORY_URL = "https://clashofclans.fandom.com/wiki/Category:Troops"
OUTPUT_FILE = "clash_of_clans_troops.json"


def get_soup(scraper, url):
    response = scraper.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_troop_links(category_soup):
    troop_links = []

    # Fandom category pages sometimes contain article links under "category-page__member-link"
    for a_tag in category_soup.select("a.category-page__member-link"):
        title = a_tag.get_text(strip=True)
        href = a_tag.get("href")

        if title and href:
            full_url = urljoin(BASE_URL, href)
            troop_links.append({
                "name": title,
                "url": full_url
            })

    # Remove duplicates while preserving order
    seen = set()
    unique_links = []
    for troop in troop_links:
        if troop["url"] not in seen:
            seen.add(troop["url"])
            unique_links.append(troop)

    return unique_links


def extract_summary(page_soup):
    # find main content area first
    content = page_soup.select_one(".mw-parser-output")
    if content:
        for p_tag in content.find_all("p"):
            text = p_tag.get_text(" ", strip=True)
            if text:
                return text

    # first nonempty paragraph
    for p_tag in page_soup.find_all("p"):
        text = p_tag.get_text(" ", strip=True)
        if text:
            return text

    return "No summary found."


def scrape_troop_data():
    scraper = cloudscraper.create_scraper(
        browser={
            "browser": "chrome",
            "platform": "windows",
            "mobile": False
        }
    )

    print("Opening category page...")
    category_soup = get_soup(scraper, CATEGORY_URL)

    troops = extract_troop_links(category_soup)
    print(f"Found {len(troops)} troop links.")

    results = []

    for i, troop in enumerate(troops, start=1):
        print(f"[{i}/{len(troops)}] Scraping: {troop['name']}")
        try:
            troop_soup = get_soup(scraper, troop["url"])
            summary = extract_summary(troop_soup)

            results.append({
                "name": troop["name"],
                "url": troop["url"],
                "summary": summary
            })

        except Exception as e:
            print(f"Error scraping {troop['name']}: {e}")
            results.append({
                "name": troop["name"],
                "url": troop["url"],
                "summary": "Error retrieving summary."
            })

    return results


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    troop_data = scrape_troop_data()
    save_to_json(troop_data, OUTPUT_FILE)
    print(f"Saved data to {OUTPUT_FILE}")