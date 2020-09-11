import os
import io
import csv
import pandas as pd
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

#helper functions
def ftoc(ftemp):
    return (ftemp - 32.0)*(5.0/9.0)

def ctof(ctemp):
    return ctemp*(9.0/5.0) + 32.0

def mitokm(miles):
    return miles * 5280.0 * 12.0 * 2.54 / 100.0 / 1000.0

def string_of_roster(csv_stream):
    sol = ''


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
def render_scouting_report():
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





if __name__ == "__main__":
    app.run(debug=False, port=54321)
