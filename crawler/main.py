import logging.config
import argparse
import time

from crawler import crawlMain, crawlFight
from crawler import crawlEvent
from util import util, fight_util


def base_crawl():
    LOG.debug(f'Crawling Events...')
    event_ids_list = crawlMain.get_eventids_from_site()

    filepath = 'data/event_ids'
    LOG.debug(f'Writing event ids to {filepath}...')
    util.list_to_file(event_ids_list, filepath)
    LOG.debug(f'Done writing {len(event_ids_list)} event ids to {filepath}')

    fight_ids_list = []
    for event_id in event_ids_list:
        LOG.debug(f'Crawling fight for event id: {event_id} ...')
        fight_ids_list.extend(crawlEvent.get_fightid_from_event(event_id))

    filepath = 'data/fight_ids'
    LOG.debug(f'Writing fight ids to {filepath}...')
    util.list_to_file(fight_ids_list, filepath)
    LOG.debug(f'Done writing {len(fight_ids_list)} fight ids to {filepath}')

    return event_ids_list, fight_ids_list


if __name__ == '__main__':
    START_TIME = time.time()
    logging.config.fileConfig('logging.conf')
    LOG = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--event-source',
                        dest='event_source',
                        type=str, nargs='?',
                        default='file',
                        choices=['file', 'db'])
    args = parser.parse_args()

    if args.event_source == 'file':
        event_ids_list, fight_ids_list = base_crawl()
        # fight_ids_list = ['cb9654746447b934', '3638ee66c7d34fe0', '924f982f0d9d2142', '73700c8c5107f719', '12683e06369d1a83']
    else:
        with open('./data/fight_ids') as f:
            fight_ids_list = f.read().splitlines()
        #fight_ids_list = ['e3aad51099a23ba4']
        #fight_ids_list = ['e3aad51099a23ba4', 'cb9654746447b934', '3638ee66c7d34fe0', '924f982f0d9d2142', '73700c8c5107f719', '12683e06369d1a83']
        # get events_ids from db

    for fight_id in fight_ids_list:
        if fight_util.check_fight_id_in_db(fight_id):
            LOG.debug(f'Fight {fight_id} is already in DB')
            continue

        crawlFight.crawl_fight_with_id(fight_id)

    print('Done crawling!')
    print(f'Took {time.time() - START_TIME} seconds')
