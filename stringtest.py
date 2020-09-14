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

print(get_usernames(test))

