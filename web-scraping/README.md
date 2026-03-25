# Clash of Clans Fandom Wiki Scraping

## Website Chosen
I chose the Clash of Clans Fandom Wiki:
https://clashofclans.fandom.com/wiki/Clash_of_Clans_Wiki


## Why I Chose This Wiki
I chose this wiki because Clash of Clans is a very well known mobile game with a large player base and a long presence in culture and in the video game industry. Since the game is so recognizable, some niche gaming references and terminology might originate from this game. The wiki acts as a fan maintained knowledge base that documents these.

## Why This Data Could Be Useful
For this project, I scraped troop data from the Clash of Clans Fandom Wiki. And may be useful to researchers because it shows how fan communities organize information about games, including name, description, and category. Researchers in digital culture, game studies, or online communities could use this kind of data to study:

- how fan knowledge is structured
- how game terminology spreads
- how community-maintained documentation preserves cultural references over time


## What I Scraped
I scraped the Clash of Clans Troops category page and troop pages to collect the following information. Note that this is limited for the sake of a MVP, and that these variable may not be enough to be truly informative to researchers:

- troop name
- troop page URL
- short summary/description

## robots.txt / Terms Check
Note: Fandom's robots policy indicates general access is allowed for `User-agent: *`, while some named AI bots like Claude are disallowed.

## Python Libraries Used
- cloudscraper
- BeautifulSoup (bs4)
- json

## Output
Data is stored in:
`clash_of_clans_troops.json`