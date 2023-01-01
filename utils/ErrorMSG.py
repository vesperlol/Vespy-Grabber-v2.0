class ErrorMsg:

    def __init__(self):
        ctypes.windll.user32.MessageBoxW(None, 'Error code: 0x00127G94\nThe application was NOT launched due to internal error.', 'Fatal Error', 2)
