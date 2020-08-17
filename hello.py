import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

#helper functions
def ftoc(ftemp):
    return (ftemp - 32.0)*(5.0/9.0)

def ctof(ctemp):
    return ctemp*(9.0/5.0) + 32.0

def mitokm(miles):
    return miles * 5280.0 * 12.0 * 2.54 / 100.0 / 1000.0

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

@app.route('/pottylist_result')
def render_pottylist_result():
    return render_template('pottylist_result.html')



if __name__ == "__main__":
    app.run(debug=False, port=54321)
