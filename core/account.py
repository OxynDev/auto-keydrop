from core import untils
import tls_client, time


class User:
    def __init__(self, 
                 browser_name : str = 'chrome',
                 ):
        
        self.user_cookies = untils.get_cookie_browser(browser_name)
        self.session = tls_client.Session(
            client_identifier="chrome114",
            random_tls_extension_order=True

        )
        self.token = self.get_token()
        #self.balance = self.get_balance()

    def get_balance(self):

        headers = {
            'authority': 'key-drop.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'referer': 'https://key-drop.com/pl/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }

        params = {
            'battleTickets': '1',
        }

        response = self.session.get('https://key-drop.com/pl/balance', params=params, cookies=self.user_cookies, headers=headers).json()

        return response
    
    def get_token(self):

        headers = {
            'authority': 'key-drop.com',
            'accept': '*/*',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://key-drop.com/pl/case-battle/list',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="118", "Chromium";v="118"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

        params = {
            't': str(round(time.time()*1000)),
        }
        print(self.user_cookies)
        response = self.session.get('https://key-drop.com/pl/token', params=params, cookies=self.user_cookies, headers=headers)
        return response.text