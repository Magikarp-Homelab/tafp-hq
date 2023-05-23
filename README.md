# hl-tafp

Scrape data from http://ufcstats.com/

* go by event
* from event to fight
* from fight to fighter

## Flow
* Crawl main page for list of event ids
* crawl event for list of fight ids
* if fight id in db skip
* crawl fight for data, make list of fighter ids
* if fighter in db skip
* crawl fighter