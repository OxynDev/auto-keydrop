


import time
from core import untils
import tls_client


class Daily:
    def __init__(self, 
                 user,
                 ):
        
        self.user = user
        self.session = tls_client.Session(
            client_identifier="chrome114",
            random_tls_extension_order=True

        )


    def open_dialy_case(self):

        headers = {
            'authority': 'key-drop.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0ehyVcsg4VxabF7Z',
            'origin': 'https://key-drop.com',
            'pragma': 'no-cache',
            'referer': 'https://key-drop.com/pl/daily-case',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }

        data = '------WebKitFormBoundary0ehyVcsg4VxabF7Z\r\nContent-Disposition: form-data; name="level"\r\n\r\n0\r\n------WebKitFormBoundary0ehyVcsg4VxabF7Z--\r\n'

        response = self.session.post('https://key-drop.com/pl/apiData/DailyFree/open', cookies=self.user.user_cookies, headers=headers, data=data)
        print(response.text)








