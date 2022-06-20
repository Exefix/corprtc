import time
import requests
from colorama import *

def LoadFromArray(array):
    sessions = []
    for acc in array:
        new_session = RBLXWild()
        new_session.username = acc["username"]
        new_session.authToken = acc["authToken"]
        new_session.session = acc["session"]
        new_session.useragent = acc["useragent"]

        sessions.append(new_session)
    
    return sessions

class RBLXWild:
    username = "25nv"
    authToken = "333cf1a0564bddf9786abb475bda9d6c030d776f33f0cdbb808f83c186e62221a93467c5b03fbe92a4578440f05f44b5bade8c247347eefc49edc4f90a8d116f"
    session = "s%3AMYRvzfA-qU_YXRUIxv_uXS2Z8OXWUKUG.vvrzYiUD1IKRYIh92iGDyJ5H6xuc4fSP1cB%2BGWkJq0A"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"


    # Join pot #
    def Join(self, potId, captchaToken):
        # Header data #
        headers = {
            "User-Agent": self.useragent,
            "Accept-Language": "en-US,en;q=0.5",
            "Authorization": self.authToken,
            "Origin": "https://rblxwild.com",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "TE": "trailers"
    }

        # Cookie data #
        cookies = {
            "session": self.session
        }

        # Post data #
        json = {
            "captchaToken": captchaToken, 
            "potId": potId, 
            "i1oveu": True
        }

        try:
            response = requests.post("https://rblxwild.com/api/events/rain/join", json=json, headers=headers, cookies=cookies)
        except Exception as e:
            print(Fore.RED + e)
            return False
        else:
            print('')