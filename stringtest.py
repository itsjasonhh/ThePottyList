def get_usernames(lobby_text):
    list_of_lobby = lobby_text.split('\n')
    usernames = []
    for sentence in list_of_lobby:
        usernames.append(sentence.split(' joined the lobby.')[0])
    return usernames


test = '''SenorHuang joined the lobby.
short4anderson joined the lobby.
n0th1ng2do joined the lobby.
FaYdeePpu joined the lobby.
Gnuxx joined the lobby.'''

#u.gg and op.gg work, league of graphs does not. Gonna use u.gg
import requests, bs4
# res = requests.get('https://u.gg/lol/profile/na1/senorhuang/overview?queueType=ranked_solo_5x5')
# res.raise_for_status()
# test = bs4.BeautifulSoup(res.text, 'html.parser')
#gets the Division and LP. Maybe don't use strong but use more specific search phrases (like class or something)
# search = test.find("div", class_="rank-text")
# print(search.text)
# search2 = test.find("div", class_="rank-wins")
# winrate, games_played = search2.text.split(" WR")
# print(winrate + " WR in " + games_played)

def get_ugg_info(name):
    res = requests.get('https://u.gg/lol/profile/na1/' + name + '/overview?queueType=ranked_solo_5x5')
    raw_info = bs4.BeautifulSoup(res.text, 'html.parser')
    rank, lp = raw_info.find("div", class_='rank-text').text.split('/')
    wins_games = raw_info.find("div", class_='rank-wins')
    winrate, games_played = wins_games.text.split(' WR')
    return rank + ' : ' + lp + ', ' + winrate + ' WR in ' + games_played
print(get_ugg_info('senorhuang'))
