def get_usernames(lobby_text):
    list_of_lobby = lobby_text.split('\n')
    usernames = []
    for sentence in list_of_lobby:
        usernames.append(sentence.split(' joined the lobby.')[0])
    return usernames


test = '''SenorHuang joined the lobby.
short4anderson joined the lobby.
n0thingtod0 joined the lobby.
FaYdeePu joined the lobby.
Gnuxx joined the lobby.'''

#u.gg and op.gg work, league of graphs does not. Gonna use u.gg
import requests, bs4
res = requests.get('https://u.gg/lol/profile/na1/senorhuang/overview?queueType=ranked_solo_5x5')
res.raise_for_status()
test = bs4.BeautifulSoup(res.text, 'html.parser')


