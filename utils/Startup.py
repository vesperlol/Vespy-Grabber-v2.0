import winreg as reg
import os	
import sys
class Startup:

    def __init__(self):
        self.file = sys.argv[0]
        self._startup()
    
    def _startup(self):
        try:
                fp = os.path.dirname(os.path.realpath(__file__))
                file_name = sys.argv[0].split('\\')[-1]
                new_file_path = fp + '\\' + file_name
                keyVal = r'Software\\Microsoft\Windows\\CurrentVersion\\Run'
                key2change = reg.OpenKey(reg.HKEY_CURRENT_USER, keyVal, 0, reg.KEY_ALL_ACCESS)
                reg.SetValueEx(key2change, 'CustomProgramName', 0, reg.REG_SZ,new_file_path)
        except:pass
