from websocket import create_connection
import json, httpx, time, tls_client, traceback
from colorama import Fore


class Battle:
    def __init__(self, user, mode: str = 'free'):
        self.targets = ['KITTY', 'ONYX', 'ROCKET RACCON', 'SERENITY', 'MILSPEC', 'ICE BLAST', 'BEAST', 'TEETH', 'GUMMY', 'PROGRESS', 'ADVANCE', 'KICK']
       
        self.session = tls_client.Session(
            client_identifier="chrome114",
            random_tls_extension_order=True

        )
       
        self.user = user
        self.mode = mode
        self.start_socket()
        


    def join(self, data):
        try:
            print(Fore.BLUE + " [X] JOINING GAME " + str(data) + Fore.RESET)
            headers = {
                'authority': 'kdrp2.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
                'authorization': 'Bearer ' + self.user.token,
                'origin': 'https://key-drop.com',
                'referer': 'https://key-drop.com/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-currency': 'pln',
            }

            response = self.session.post('https://kdrp2.com/CaseBattle/joinCaseBattle/'+str(data[1])+'/1', headers=headers)
            print(response.text)
            response = response.json()
            try:
                if response['message'] == 'Unauthorized':
                    print(Fore.YELLOW + " [X] INVALID TOKEN" + Fore.RESET)
                    return True
            except:
                pass
            try:
                if response['success'] == False:
                    if response['errorCode'] == 'rateLimited':
                        print(Fore.YELLOW + " [X] RATE LIMITED" + Fore.RESET)
                        time.sleep(2)
                        return False
                    elif response['errorCode'] == 'notEnoughtMoney':
                        print(Fore.RED + " [X] TOO LESS MONEY" + Fore.RESET)
                        return False
                    elif response['errorCode'] == 'userHasToWaitBeforeJoiningFreeBattle':
                        print(Fore.YELLOW + " [!] WAIT FOR FREE BATTLE " + response['message'].split("You have to wait ")[1].split(" before you can ")[0] + Fore.RESET)
                        return True
                    else:
                        print(response)
            except:
                pass
        except:
            traceback.print_exc()
        
        return True


    def catch(self, ws):

        print(Fore.YELLOW + " [.] SOCKET CONNECTED" + Fore.RESET)

        while True:
            mess = ws.recv()
            if '42/case-battle,' in mess:
                json_data = json.loads(mess.split("case-battle,")[1])
                if json_data[0] == "BC_CREATE_V3":
                    battle_id = json_data[1][0]
                    public_check = json_data[1][5]
                    battle_data = json_data[1][7]
                    if public_check == 'public':
                        if len(battle_data) == 1:
                            name = battle_data[0][1]
                            if name in self.targets:
                                res = self.join([name, battle_id])
                                if res == True:
                                    break
                                time.sleep(2)

    def start_socket(self):

        while True:
            try:
                headers = {
                    'Pragma': 'no-cache',
                    'Origin': 'https://key-drop.com',
                    'Accept-Language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,zh-TW;q=0.6,zh;q=0.5',
                    'Sec-WebSocket-Key': 'UdaN6dVrvcfepgdCRPKseA==',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                    'Upgrade': 'websocket',
                    'Cache-Control': 'no-cache',
                    'Connection': 'Upgrade',
                    'Sec-WebSocket-Version': '13',
                    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
                }
                

                ws = create_connection('wss://kdrp3.com/socket.io/?connection=battle&EIO=4&transport=websocket',
                                    header=headers)
                ws.send('40/case-battle,{"token":""}')
                self.catch(ws)
            except:
                pass