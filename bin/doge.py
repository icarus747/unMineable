#!/usr/bin/env python3
# By DangerZone
# Created 4/20/2021

from requests import session
import json
from datetime import datetime
import sys

def main(wallet, base_url):
    with session() as suffering_succotash:
        query = {
            'tz': '-6',
            'coin': 'DOGE'
        }
        body= {'run_time': str(datetime_1)}
        url = f'https://{base_url}/v3/stats/{wallet}?tz=-6&coin=DOGE'
        try:
            response = suffering_succotash.get(url=url)
            body.update(response.json())
            del body['data']['graph']
            del body['data']['payment_info']
            print(json.dumps(body))
            pass
        except:
            print("Som ting wong.")
    pass


if __name__ == '__main__':
    datetime_1 = datetime.now()
    wallets = [sys.argv[1]]
    for wallet in wallets:
        base_url = "api.unminable.com"
        main(wallet, base_url)

