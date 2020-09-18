import requests, bs4
def get_usernames(lobby_text):
    list_of_lobby = lobby_text.split('\n')
    usernames = []
    for sentence in list_of_lobby:
        usernames.append(sentence.split(' joined the lobby.')[0])
    if len(usernames) > 5:
        usernames.pop()
    return usernames

#takes a name and returns a bs4 object that can be searched
def create_bs(name):
    res = requests.get('https://u.gg/lol/profile/na1/' + name + '/overview?queueType=ranked_solo_5x5')
    raw_info = bs4.BeautifulSoup(res.text, 'html.parser')
    return raw_info

#takes a bs4 object and returns the u.gg rank string
def get_ugg_rank(bs_object):
    ranked_games = bs_object.find("div", class_='rank-text')
    rank, lp = ranked_games.text.split('/')
    return rank + ' : ' + lp

#takes a bs4 object and returns the u.gg overall wr
def get_ugg_overall_wr(bs_object):
    wins_games = bs_object.find("div", class_='rank-wins')
    winrate, games_played = wins_games.text.split(' WR')
    return winrate + ' WR in ' + games_played

#takes a bs4 object and returns the u.gg recent wr
def get_ugg_recent_wr(bs_object):
    recent_winrate = bs_object.find("div", class_='winrate text-1').text
    return recent_winrate


#takes a bs4 object and returns the u.gg recent kda
def get_ugg_recent_kda(bs_object):
    recent_kda_ratio = bs_object.find("div", class_='kda-ratio-text text-1').text
    recent_kda = bs_object.find("div", class_='kda-text text-2').text
    return recent_kda_ratio + ' (' + recent_kda + ')'
#takes a list of names and returns a dictionary of len 5 (one for each username)
#each key is the name of the player
#each value is an array of 5 -> [rank_string, WR_string, recent_WR_string, 1st_played_champ_string, 2nd_played_champ_string]
def scouting(names):
    report = {}
    for name in names:
        bs = create_bs(name)
        payload = []
        payload.append(get_ugg_rank(bs))
        payload.append(get_ugg_overall_wr(bs))
        payload.append(get_ugg_recent_wr(bs))
        payload.append(get_ugg_recent_kda(bs))
        report[name] = payload
    return report
def testing(lobby_string):
    list_of_names = get_usernames(lobby_string)
    d = scouting(list_of_names)
    return d

print(testing('''SenorHuang joined the lobby.
short4anderson joined the lobby.
n0th1ng2do joined the lobby.
FaYdeePpu joined the lobby.
Gnuxx joined the lobby.'''))
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


# res = requests.get('https://u.gg/lol/profile/na1/senorhuang/overview?queueType=ranked_solo_5x5')
# raw_info = bs4.BeautifulSoup(res.text, 'html.parser')
# def get_ugg_champ1_wr(bs_object):
#     champ1 = bs_object.find('div', class_='most-played-champions').text
#     return champ1

# print(get_ugg_champ1_wr(raw_info))

