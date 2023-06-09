import os

# URLs
URL_EVENTLIST = 'http://ufcstats.com/statistics/events/completed?page=all'
URL_EVENT = 'http://ufcstats.com/event-details/'
URL_FIGHT = 'http://ufcstats.com/fight-details/'
URL_FIGHTER = 'http://ufcstats.com/fighter-details/'

# Crawler
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

FIGHT_TITLE_BOUT = 'Title Bout'

FEET_TO_CM_RATION = 30.48
INCH_TO_CM_RATION = 2.54
POUNDS_TO_KG_RATIO = 0.453592

# Mongo DB
MONGO_DB_URL = os.getenv('MONGO_DB_URL', 'mongodb://192.168.1.20:27017/')
MONGO_DB_NAME = 'tafp'
COLLECTION_FIGHT = 'fight'
COLLECTION_FIGHT_DETAIL = 'fight_detail'
COLLECTION_FIGHTER = 'fighter'
