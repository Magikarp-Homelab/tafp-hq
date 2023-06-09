from datetime import datetime

from util import util
from CONSTANTS import URL_EVENTLIST


def get_eventids_from_site():
    soup = util.get_soup(URL_EVENTLIST)

    link_elements = soup.findAll('i', 'b-statistics__table-content')
    link_ids = []

    for le in link_elements:
        event_id, event_date = __parse_id_and_date_from_parent(le)
        if event_date > datetime.now():
            continue
        link_ids.append(event_id)

    return link_ids


def __parse_id_and_date_from_parent(parent_element):
    parsed_id = parent_element.contents[1].attrs['href'].strip().split('/')[-1]
    parsed_date = parent_element.contents[3].text.strip()
    return parsed_id, util.string_to_date(parsed_date)



