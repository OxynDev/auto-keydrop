from core import battle, account, giveaway, daily


class Keydrop:
    def __init__(self, browser_name: str = 'chrome') -> None:
        
        self.user = account.User( browser_name = browser_name )
        
        self.token = self.user.token

    def start_battle(self):
        
        battle.Battle(
            mode = 'free',
            user = self.user
            )
    
    def start_giveaway_joiner(self):
        print(giveaway.Giveaway(self.user).join_loop())

    def open_daily_chest(self):
        print(daily.Daily(self.user).open_dialy_case())


res = Keydrop().start_battle()

print(res)


