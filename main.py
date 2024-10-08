import httpx
import os
import sys
import random
import threading
import time
import argparse
import pyfiglet
from loguru import logger
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestWebView
from pyrogram.raw.functions.messages import StartBot

from urllib.parse import unquote
from random import randint

from config import settings
from appconfig import AppURLS, request_headers

logger.remove()
logger.add(sink=sys.stdout, format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                   " | <level>{level: <8}</level>"
                                   " | <cyan><b>{module}:{line}</b></cyan>"
                                   " | <white><b>{message}</b></white>")
logger = logger.opt(colors=True)

if not os.path.exists('sessions'):
    os.mkdir('sessions')


class SimpleTap:

    def __init__(self, user_id: int, initData: str):
        self.user_id = user_id
        self.initData = initData

    def profile(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.PROFILE_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def activate(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.ACTIVATE_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def tap(self, count: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.TAP_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "count": count
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def get_task_list(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.GET_TASK_LIST_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "lang": "en",
                        "platform": 1,
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def start_task(self, type: int, id: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.START_TASK_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "type": type,
                        "id": id
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def check_task(self, type: int, id: int):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CHECK_TASK_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "type": type,
                        "id": id
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def claim(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CLAIM_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def friends(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.FRIENDS_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "skip": 0,
                        "take": 2000
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def claim_friends(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CLAIM_FRIENDS_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def get_spin_wheel(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.GET_SPIN_WHEEL_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def claim_spin(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CLAIM_SPIN_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "amount": 0,
                        "frontCoef": float(str(random.randint(65, 450)) + "." +
                                           str(random.randint(100000000000000, 999999999999999))[:14]),
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def get_mining_blocks(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.GET_MINING_BLOCKS_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "lang": "en"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def buy_mining_block(self, level, mineId):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.BUY_MINING_BLOCK_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "level": level,
                        "mineId": f"{mineId}"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def get_collections(self):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.GET_COLLECTIONS_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "lang": "en"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def get_collection_cards(self, collection_id):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.GET_COLLECTION_CARDS_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "collectionId": f"{collection_id}",
                        "lang": "en"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def card_claim(self, card_id, collection_id):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CARD_CLAIM_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "collectionId": f"{collection_id}",
                        "cardId": card_id,
                        "lang": "en"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

    def card_description(self, card_id):
        with httpx.Client() as session:
            try:
                r = session.post(
                    url=AppURLS.CARD_DESCRIPTION_URL,
                    json={
                        "userId": self.user_id,
                        "authData": self.initData,
                        "cardId": card_id,
                        "lang": "en"
                    },
                    headers=request_headers
                )
                return r.json()
            except:
                return None

def thread(user_id, initData, i, session):
    logger.info(f'Process thread №{i} for session "{session}" started!')
    api = SimpleTap(user_id=user_id, initData=initData)
    while True:
        profile_data = api.profile()
        if profile_data is not None:
            profile_data = profile_data["data"]
            logger.info(f'{session} | Current balance: <y>{profile_data["balance"]:,}</y> {profile_data["symbol"]}')
            # logger.info(f'{session} | Taps limit: <y>{profile_data["maxAvailableTaps"]:,}</y>. '
            #             f'{profile_data["symbol"]} per hour: <y>{profile_data["activeFarmingPerSec"] * 3600:,}</y>')

            if settings.SPIN_THE_WHEEL and profile_data["spinCount"] > 0:
                spins_count = profile_data["spinCount"]
                logger.info(f'{session} | Available wheel spins: <y>{spins_count}</y>')
                wheel_status = api.get_spin_wheel()
                if wheel_status is not None and wheel_status["result"] == 'OK':
                    spin_slices = wheel_status["data"]["slices"]
                    spin_rewards = {}
                    for slice in spin_slices:
                        spin_types = ['Tap Limit', 'Per Hour', 'Tap Size', 'Coins']
                        spin_rewards[slice["number"]] = f'+{slice["amount"]} {spin_types[slice["spinType"]]}'
                    for spin in range(spins_count):
                        spin_staus = api.claim_spin()
                        time.sleep(1)
                        if spin_staus is not None and spin_staus["result"] == 'OK':
                            logger.success(f'{session} | The wheel has been successfully spun! '
                                           f'Reward: <y>{spin_rewards[spin_staus["data"]["number"]]}</y>')
                            profile_data = api.profile()["data"]
                            logger.info(f'{session} | Current balance: <y>{profile_data["balance"]:,}</y>. '
                                        f'Taps limit: <y>{profile_data["maxAvailableTaps"]:,}</y> '
                                        f'{profile_data["symbol"]} per hour: '
                                        f'<y>{profile_data["activeFarmingPerSec"] * 3600:,}</y>')
                        time.sleep(2)

            if settings.CLAIM_REFERRALS_REWARD and profile_data["refBalance"] > 2000:
                friends_status = api.friends()
                if friends_status is not None:
                    logger.info(f'{session} | Total friends: {friends_status["count"]:,}. '
                                f'Reward: {profile_data["refBalance"]:,}')
                    claim_friends_status = api.claim_friends()
                    if claim_friends_status is not None and claim_friends_status["result"] == 'OK':
                        logger.success(f'{session} | Successfully claimed referrals reward '
                                       f'<y>{profile_data["refBalance"]:,}</y> '
                                       f'{profile_data["symbol"]}')

            if settings.CLAIM_COLLECTIONS_CARDS and profile_data['cardClaimCount'] > 0:
                collections = api.get_collections()
                if collections is not None and collections["result"] == 'OK':
                    collections_list = collections["data"]
                    unclaimed_collections = []
                    for collection in collections_list:
                        if collection["cards"]["cnt"] > 0:
                            unclaimed_collections.append(collection["id"])
                            logger.info(f'{session} | Unclaimed <g>{collection["cards"]["cnt"]}</g> '
                                        f'card(s) in collection <g>{collection["title"]}</g>')
                    for collection in unclaimed_collections:
                        collection_cards = api.get_collection_cards(collection_id=collection)["data"]
                        for card in collection_cards:
                            if card["status"] == 1:
                                claim_card = api.card_claim(card_id=card["id"], collection_id=collection)
                                if claim_card["result"] == 'OK':
                                    card_descr = api.card_description(card_id=card["id"])
                                    logger.success(f'{session} | Successfully claimed card '
                                                   f'<g>{claim_card["data"]["title"]}</g> - '
                                                   f'{card_descr["data"]}')

            if settings.UPGRADE_CARDS:
                mining_blocks = api.get_mining_blocks()
                if mining_blocks is not None and mining_blocks["result"] == 'OK':
                    cards = mining_blocks["data"]["mines"]
                    pass


            if profile_data['activeFarmingBalance'] == 0:
                activate_status = api.activate()
                if activate_status is not None:
                    if activate_status["result"] == 'OK':
                        logger.success(f'{session} | Tokens farming is activated.')
                    else:
                        logger.error(f'{session} | Tokens farming not activated.')
                else:
                    logger.error(f'{session} | Tokens get invalid response.')
            else:
                if profile_data['activeFarmingSeconds'] == profile_data['maxFarmingSecondSec']:
                    claim_status = api.claim()
                    if claim_status is not None:
                        if claim_status['result'] == 'OK':
                            logger.success(
                                f'{session} | Tokens claimed. <y>+{profile_data["activeFarmingBalance"]:,}</y>')
                        else:
                            logger.error(f'{session} | Tokens not claimed.')
                    else:
                        logger.error(f'{session} | Tokens get invalid response.')
                else:
                    pass

            task_list = api.get_task_list()
            if task_list is not None:
                for task in task_list['data']['social']:
                    if task['status'] == 1:
                        t1 = api.start_task(type=task['type'], id=task['id'])
                        if t1 is not None:
                            for tt1 in task_list['data']['social']:
                                if tt1['id'] == task['id']:
                                    if tt1['status'] == 2:
                                        logger.info(f'{session} | Started task with id <g>{tt1["id"]}</g>')

                        t2 = api.check_task(type=task['type'], id=task['id'])
                        if t2 is not None:
                            for tt2 in task_list['data']['social']:
                                if tt2['id'] == task['id']:
                                    if tt2['status'] == 3:
                                        logger.success(
                                            f'{session} | Completed task with id <g>{tt2["id"]}</g>. '
                                            f'Bonus: <y>+{tt2["bonus"]:,}</y>')

                        time.sleep(3)

            else:
                logger.error(f'{session} | Tasks get invalid response.')
            available_taps = profile_data["availableTaps"] // profile_data["tapSize"]
            random_taps = randint(
                settings.TAPS_AMOUNT[0],
                settings.TAPS_AMOUNT[1],
            )
            taps = int(min(available_taps, random_taps))
            if taps:
                tap_data = api.tap(count=int(taps * profile_data["tapSize"]))
                if tap_data is not None:
                    if tap_data['result'] == 'OK':
                        logger.success(f'{session} | Successfully tapped. '
                                       f'<y>+{taps * profile_data["tapSize"]:,}</y> {profile_data["symbol"]}')
                        random_sleep = randint(
                            settings.SLEEP_AFTER_TAP[0],
                            settings.SLEEP_AFTER_TAP[1],
                        )
                        time.sleep(random_sleep)

            else:
                sleep_time = randint(
                    settings.SLEEP_NOT_ENOUGH_TAPS[0],
                    settings.SLEEP_NOT_ENOUGH_TAPS[1],
                )
                logger.info(f'{session} | Not enough taps. Sleeping <y>{sleep_time:,}</y> seconds.')
                time.sleep(sleep_time)
        else:
            logger.error(f'{session} | Profile get invalid response.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', type=int, help='Action to perform')
    action = parser.parse_args().action
    pyfiglet.print_figlet('Simple Coin Bot')

    while True:
        if not action:
            print('''
                    1. Add session
                    2. Start proccess
                 ''')
            while True:
                action = input('\nChoose an action > ')

                if not action.isdigit():
                    logger.warning("Action must be number")
                elif action not in ['1', '2']:
                    logger.warning("Action must be 1 or 2")
                else:
                    break
        action = int(action)
        sessions = os.listdir('sessions')

        if action == 1:
            if len(sessions) > 0:
                logger.info(f'Found {len(sessions)} sessions: {sessions}')
            session_name = input('\nEnter session name>')
            if not os.path.exists(f'sessions/{session_name}.session'):
                try:
                    app = Client(
                        name=session_name,
                        api_id=settings.API_ID,
                        api_hash=settings.API_HASH,
                        workdir='sessions/'
                    )
                    with app:
                        me = app.get_me()
                        me.id
                        logger.success(f'Session with name "{session_name}" created!')
                except:
                    logger.error('Cannot add session.')
            else:
                logger.error('Session name is already used!')

        elif action == 2:
            if len(sessions) >= 1:
                for i, session in enumerate(sessions, start=1):
                    if session.endswith('.session'):
                        try:
                            app = Client(
                                name=session.replace('.session', ''),
                                api_id=settings.API_ID,
                                api_hash=settings.API_HASH,
                                workdir='sessions/'
                            )
                            app.start()

                            web_view = app.invoke(StartBot(
                                peer=app.resolve_peer('Simple_Tap_Bot'),
                                bot=app.resolve_peer('Simple_Tap_Bot'),
                                random_id=random.randint(1000, 9999),
                                start_param='1717785892732'
                            ))
                            web_view = app.invoke(RequestWebView(
                                peer=app.resolve_peer('Simple_Tap_Bot'),
                                bot=app.resolve_peer('Simple_Tap_Bot'),
                                platform='android',
                                from_bot_menu=False,
                                url='https://simpletap.app/'
                            ))

                            user_id = app.get_me().id
                            initData = unquote(string=unquote(string=
                                                              web_view.url.split('tgWebAppData=', maxsplit=1)[1].split(
                                                                  '&tgWebAppVersion', maxsplit=1)[0]))

                            threading.Thread(target=thread, args=(user_id, initData, i, app.name)).start()
                        except:
                            logger.error(f'Cannot start proccess thread with "{session}" session.')

            break


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, RuntimeError, RuntimeWarning) as _ex:
        logger.critical(f'Bot stopped! {repr(_ex)}')
