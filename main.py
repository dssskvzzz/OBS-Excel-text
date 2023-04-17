import obswebsocket
from obswebsocket import requests
import pandas as pd
import time

#REPLACE!!
excel_file = r"replace IT"

authorname_list_one = []
authorname_list_two = []
authorname_list_three = []
all_list = []
obs = obswebsocket.obsws("localhost", 4455, "password")
obs.connect()


def obs_one(nick):
    nickname = ''
    for el in nick:
        nickname += str(el)+"\n"
    obs.call(requests.SetSourceSettings("One", {"text": str(nickname)+"\n"}))

def obs_two(nick):
    nickname = ''
    for el in nick:
        nickname += str(el)+"\n"
    obs.call(requests.SetSourceSettings("Two", {"text": str(nickname)+"\n"}))

def obs_three(nick):
    nickname = ''
    for el in nick:
        nickname += str(el)+"\n"
    obs.call(requests.SetSourceSettings("Three", {"text": str(nickname)+"\n"}))

df = pd.read_excel(excel_file, usecols='A, E',skiprows=1)
for i, row in df.iterrows():
    authorname= row[df.columns[0]]
    message = row[df.columns[1]]
    if message == 'one' and authorname not in authorname_list_one:
        authorname_list_one.append(authorname)
    elif message == 'two'and authorname not in authorname_list_two:
        authorname_list_two.append(authorname)
    elif message == 'three'and authorname not in authorname_list_three:
        authorname_list_three.append(authorname)
    else:
        pass
obs_one(authorname_list_one)
obs_two(authorname_list_two)
obs_three(authorname_list_three)