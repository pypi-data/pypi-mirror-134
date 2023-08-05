import json
import time

import requests
import win32com.client


def trans(words):
    """
    Parameters pass into a string, translation, support Chinese and English translation.
    """
    API_URL = "https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}"
    api_res_data = requests.get(API_URL.format(words)).text
    return json.loads(api_res_data)["translateResult"][0][0]["tgt"]


def speak(words):
    """
    Enter the string as a parameter, and read aloud, with no return value.
    """
    SOUND = win32com.client.Dispatch("SAPI.SpVoice")
    SOUND.Speak(words)


def shows(words):
    """
    Enter the string as a parameter, show the result in console with colorful font.
    """
    API_URL = "https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}"
    api_res_data = requests.get(API_URL.format(words)).text
    result = json.loads(api_res_data)["translateResult"][0][0]["tgt"]
    print("\033[1;34m{} Made From Wristwaking\033[0m\n".format(format(time.strftime("%Y-%m-%d %H:%M:%S"))))
    print("\033[1;34mRESULT : {}\033[0m".format(result))
