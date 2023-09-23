import time
from core import untils
import tls_client


class Giveaway:
    def __init__(self, 
                 user,
                 ):
        
        self.user = user
        self.session = tls_client.Session(
            client_identifier="chrome114",
            random_tls_extension_order=True

        )

    def get_list(self) -> dict:

        headers = {
            'authority': 'wss-2061.key-drop.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'cache-control': 'no-cache',
            'origin': 'https://key-drop.com',
            'pragma': 'no-cache',
            'referer': 'https://key-drop.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-currency': 'PLN',
        }

        params = {
            'type': 'active',
            'page': '0',
            'perPage': '5',
            'status': 'active',
            'sort': 'latest',
        }

        response = self.session.get('https://wss-2061.key-drop.com/v1/giveaway//list', params=params, headers=headers)
        try:
            return response.json()['data']
        except:
            return False
    

    def join(self, id: str):

        headers = {
            'authority': 'wss-3002.key-drop.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'authorization': 'Bearer ' + self.user.token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://key-drop.com',
            'pragma': 'no-cache',
            'referer': 'https://key-drop.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }


        response = self.session.put('https://wss-3002.key-drop.com/v1/giveaway//joinGiveaway/'+id, headers=headers)
        print(response.text)

    def join_loop(self):
        print("GIVE AWAY JOINER STARTED")
        while True:
            giveaway_list = self.get_list()
            if giveaway_list == False:
                time.sleep(100)
            else:
                for i in reversed(giveaway_list):
                    id = i['id']
                    joined = i['haveIJoined']
                    title = i['prizes'][0]['title']

                    if joined == False:
                        print("JOINING: " + title)
                        self.join(id)
                        time.sleep(10)

            time.sleep(900)
            print("Waiting 15 min")