import requests
import pyjokes
import wikipedia

import errors

URL = "http://api.brainshop.ai/get"


brain = ""
apikey = ""
uiid = ""
msg = ""


def chatbotsetup(brainid = 0, apikeyuser = 0, uiiduser = "PythonChatbot"):
    global brain
    global apikey
    global uiid
    brain = brainid
    apikey = apikeyuser
    uiid = uiiduser
    
def getcreds():
    creds = {
        'bid': brain,
        'key': apikey,
        'uid': uiid,
    }
    return creds

def sendmsg(message1):
    msg = message1
    if 'jokes' in msg or 'joke' in msg :
        data = "Here is a joke : " + pyjokes.get_joke()
        return data
    if 'wikipedia' in msg:
        try:
            statement = msg.replace("wikipedia", "")
            r = wikipedia.search(statement)
            results = "According to Wikipedia :\n" + wikipedia.summary(r[0], sentences=3)
            return results
        except IndexError:
            return "No results found."
    PARAMS = {
        'bid': brain,
        'key': apikey,
        'uid': uiid,
        'msg': msg
    }
    if PARAMS['bid'] == 0 or PARAMS['key'] == 0 or PARAMS['uid'] == "":
        raise errors.BaseError("ChatBot not setup properly!")
    data = requests.get(url=URL, params=PARAMS).json()['cnt']
    
    return data


                                                                                                                                                                                                                                                              
