import sys
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'opr': 'pwdLogin', 'userName': '181270005', 'pwd': 'fWwFZZ)QY7NnNu', 'rememberPwd': '1'}

session = requests.Session()
session.trust_env = False  # bypass system proxy

try:
    session.post('http://2.2.2.2/ac_portal/login.php?tabs=pwd', headers = headers, data = payload)
except:
    sys.stdout.write("An exception occurred")
else:
    sys.stdout.write("Done!")
