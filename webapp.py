import os
import io
import csv
import pandas as pd
import requests
import bs4
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

#helper functions

#converts Fahrenheit to Celsius
def ftoc(ftemp):
    return (ftemp - 32.0)*(5.0/9.0)

#converts Celsius to Fahrenheit
def ctof(ctemp):
    return ctemp*(9.0/5.0) + 32.0

#converts miles to kilometers
def mitokm(miles):
    return miles * 5280.0 * 12.0 * 2.54 / 100.0 / 1000.0

#takes string of text from LoL client and outputs a list of 5 usernames
def get_usernames(lobby_text):
    list_of_lobby = lobby_text.split('\n')
    usernames = []
    for sentence in list_of_lobby:
        usernames.append(sentence.split(' joined the lobby.')[0])
    return usernames

#takes a username and returns the u.gg info
def get_ugg_info(name):
    res = requests.get('https://u.gg/lol/profile/na1/' + name + '/overview?queueType=ranked_solo_5x5')
    raw_info = bs4.BeautifulSoup(res.text, 'html.parser')
    rank, lp = raw_info.find("div", class_='rank-text').text.split('/')
    wins_games = raw_info.find("div", class_='rank-wins')
    winrate, games_played = wins_games.text.split(' WR')
    return rank + ' : ' + lp + ', ' + winrate + ' WR in ' + games_played

#takes a list of names and returns a dictionary of u.gg info
def scouting(names):
    list_of_stats = {}
    for name in names:
        list_of_stats[name] = get_ugg_info(name)
    return list_of_stats



#subsites of main website
@app.route('/')
def render_main():
    return render_template("home.html")

@app.route('/ftoc')
def render_ftoc():
    return render_template("ftoc.html")

@app.route('/ctof')
def render_ctof():
    return render_template("ctof.html")
 

@app.route('/mitokm')
def render_mitokm():
    return render_template("mitokm.html")

@app.route('/pottylist')
def render_potty_list():
    return render_template("pottylist.html")

@app.route('/scoutingreport')
def render_scoutingreport():
    return render_template("scoutingreport.html")


@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['fTemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html',fTemp=ftemp_result,cTemp=ctemp_result)
    except ValueError:
        return "Sorry, something went wrong."

@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['cTemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html',cTemp=ctemp_result,fTemp=ftemp_result)
    except ValueError:
        return "Sorry, something went wrong."

@app.route('/mitokm_result')
def render_mitokm_result():
    try:
        mitemp_result = float(request.args['miTemp'])
        kmtemp_result = mitokm(mitemp_result)
        return render_template('mitokm_result.html',miTemp=mitemp_result,kmTemp=kmtemp_result)
    except ValueError:
        return "Sorry, something went wrong."

@app.route('/pottylist_result', methods=['GET','POST'])
def render_pottylist_result():
    f = request.files["roster"]
    stream = io.StringIO(f.stream.read().decode("UTF-8"), newline=None)
    csv_input = csv.reader(stream)
    return render_template('pottylist_result.html', roster=csv_input)

@app.route('/scoutingreport_result')
def render_scoutingreport_result():
    try:
        lobby = str(request.args['lobbynames'])
        list_of_names = get_usernames(lobby)
        scouts = scouting(list_of_names)
        return render_template('scoutingreport_result.html', names=scouts)
    except:
        return "Sorry, something went wrong."


if __name__ == "__main__":
    app.run(debug=False, port=54321)
