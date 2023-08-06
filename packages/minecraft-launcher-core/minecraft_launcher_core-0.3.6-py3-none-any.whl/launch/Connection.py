import requests

class Connect:
    def __init__(self,username,password,clientToken):
        self.a = {
   "agent": {
       "name": "Minecraft",
       "version": 1
   },
   "username": username,
   "password": password,
   "clientToken": clientToken,
}
    def login(self):
        r = requests.post('https://authserver.mojang.com',data=str(a),headers={'Content-Type':'application/json/authenticate'})
        if r.status_code == 500:
            return -1
        else:
            return eval(r.content.decode())['clientToken'],eval(r.content.decode())['accessToken']

if __name__ == '__main__':
    a = Connect('a','awdwadwa','00000000000000000000000')
    a.login()

