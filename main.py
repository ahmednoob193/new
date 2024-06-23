import os; os.system("python3 webserver.py & >/dev/null")
import requests
import time



playload = {

    'content': 'طيب' # < < الرساله


}

headerst = {

    'authorization': 'MTA3MTQ2MzEwNjQ5NDA3OTA3Ng.G93bJU.yFPaCtwBlVOYB6uYOf4KrYX8oukIxlR76-nIZk' # < < توكن الحساب الاول

}

headerst1 = {

    'authorization': '' # < < توكن الحساب الثاني

}
headerst2 = {

    'authorization': '' # < < توكن الحساب الثالث

}

channel = '970724217614139423' # < < ايدي الروم

url = f'https://discord.com/api/v8/channels/{channel}/messages'


while True:
    requests.post(url, data=playload, headers=headerst, )
    requests.post(url, data=playload, headers=headerst1, )
    requests.post(url, data=playload, headers=headerst2, )
    time.sleep(60) # < < كم رساله في الثانيه


